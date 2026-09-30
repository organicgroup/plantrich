import frappe
import requests

from collections import defaultdict
from datetime import datetime, timedelta, time


# ================================================================
# CONFIGURATION
# ================================================================

API_URL = "https://plantrich.lanatime.in/api/RptTimecard/GetData"

DOCTYPE = "Lanatime Attendance Log"

# ---------------------------------------------------------------
# First ever synchronization starts from this date
# ---------------------------------------------------------------

INITIAL_SYNC_DATE = "2026-04-01"


# ---------------------------------------------------------------
# Special Gate Device
#
# This device always reports OUT.
#
# Therefore:
#     First punch = IN
#     Last punch  = OUT
#     Middle punches are ignored / removed.
# ---------------------------------------------------------------

GATE_DEVICE = "WED3254100742"


# ================================================================
# MAIN SYNC METHOD
# ================================================================

@frappe.whitelist()
def sync_lanatime_attendance_log(
    start_date=None,
    end_date=None
):
    """
    Sync Lanatime API data into:

        Lanatime Attendance Log


    AUTOMATIC DATE RANGE
    --------------------

    First sync:

        2026-04-01 -> Today


    Subsequent sync:

        Last Sync Date - 1 Day
                ->
        Today


    The one-day overlap is intentional because the attendance
    window is:

        05:00 AM -> next day 04:59:59 AM


    ATTENDANCE DAY
    --------------

    Every employee uses the same attendance day:

        05:00 AM
            ->
        Next day 04:59:59 AM


    NORMAL DEVICES
    --------------

    Keep IN / OUT exactly as received from Lanatime.


    SPECIAL GATE DEVICE
    -------------------

        WED3254100742

    API checktype is ignored.

    For each employee and attendance day:

        First punch  = IN
        Last punch   = OUT
        Middle punch = deleted / ignored
    """

    # ============================================================
    # 1. DETERMINE SYNC RANGE
    # ============================================================

    if not start_date or not end_date:

        auto_start_date, auto_end_date = get_sync_range()

        if not start_date:
            start_date = auto_start_date

        if not end_date:
            end_date = auto_end_date

    # Convert to date strings
    start_date = str(
        frappe.utils.getdate(start_date)
    )

    end_date = str(
        frappe.utils.getdate(end_date)
    )

    # ============================================================
    # VALIDATE DATE RANGE
    # ============================================================

    if frappe.utils.getdate(start_date) > frappe.utils.getdate(
        end_date
    ):
        frappe.throw(
            "Start Date cannot be greater than End Date."
        )

    # ============================================================
    # 2. FETCH DATA FROM LANATIME API
    # ============================================================

    try:

        response = requests.get(
            API_URL,
            params={
                "snName": "",
                "startDate": start_date,
                "endDate": end_date,
            },
            timeout=120
        )

        response.raise_for_status()

        payload = response.json()

    except Exception:

        frappe.log_error(
            frappe.get_traceback(),
            "Lanatime API Sync Failed"
        )

        frappe.throw(
            "Unable to fetch data from Lanatime API."
        )

    # ============================================================
    # NORMALIZE API RESPONSE
    # ============================================================

    api_data = normalize_api_response(
        payload
    )

    # ============================================================
    # NO DATA
    # ============================================================

    if not api_data:

        # Still advance the sync checkpoint if we already have
        # attendance records.
        mark_sync_completed()

        frappe.db.commit()

        return {
            "success": True,
            "message": "No Lanatime records found.",
            "start_date": start_date,
            "end_date": end_date,
            "inserted": 0,
            "updated": 0,
            "deleted": 0,
        }

    # ============================================================
    # 3. SEPARATE NORMAL DEVICES / GATE DEVICE
    # ============================================================

    normal_logs = []
    gate_logs = []

    for row in api_data:

        if not isinstance(row, dict):
            continue

        device_name = clean_value(
            row.get("snName")
        )

        if device_name == GATE_DEVICE:

            gate_logs.append(row)

        else:

            normal_logs.append(row)

    # ============================================================
    # COUNTERS
    # ============================================================

    inserted = 0
    updated = 0
    deleted = 0

    # ============================================================
    # 4. PROCESS NORMAL DEVICES
    # ============================================================
    #
    # Normal plant devices already report correct:
    #
    # IN
    # OUT
    #
    # So nothing is changed.
    # ============================================================

    for row in normal_logs:

        result = upsert_normal_attendance_log(
            row
        )

        if result == "inserted":

            inserted += 1

        elif result == "updated":

            updated += 1

    # ============================================================
    # 5. GROUP SPECIAL GATE DEVICE RECORDS
    # ============================================================
    #
    # Group:
    #
    # employee + attendance date
    #
    # Attendance day:
    #
    # 05:00 AM
    #     ->
    # next day 04:59:59 AM
    # ============================================================

    grouped_gate_logs = defaultdict(list)

    for row in gate_logs:

        # --------------------------------------------------------
        # Punch Time
        # --------------------------------------------------------

        check_time = parse_datetime(
            row.get("checktime")
        )

        if not check_time:
            continue

        # --------------------------------------------------------
        # Lanatime Employee ID
        # --------------------------------------------------------

        lanatime_id = clean_value(
            row.get("employeeID")
        )

        if not lanatime_id:
            continue

        # --------------------------------------------------------
        # Attendance Date
        # --------------------------------------------------------

        attendance_date = get_attendance_date(
            check_time
        )

        # --------------------------------------------------------
        # Group by Employee + Attendance Date
        # --------------------------------------------------------

        key = (
            lanatime_id,
            attendance_date
        )

        grouped_gate_logs[key].append(
            {
                "row": row,
                "check_time": check_time,
            }
        )

    # ============================================================
    # 6. PROCESS SPECIAL GATE DEVICE
    # ============================================================

    for key, punches in grouped_gate_logs.items():

        lanatime_id, attendance_date = key

        # --------------------------------------------------------
        # Sort earliest -> latest
        # --------------------------------------------------------

        punches.sort(
            key=lambda item: item["check_time"]
        )

        if not punches:
            continue

        # ========================================================
        # FIRST PUNCH
        # ========================================================

        first_punch = punches[0]

        # ========================================================
        # LAST PUNCH
        # ========================================================

        last_punch = None

        if len(punches) > 1:

            last_punch = punches[-1]

        # ========================================================
        # FIRST PUNCH = IN
        # ========================================================

        result = upsert_gate_attendance_log(
            row=first_punch["row"],
            log_type="IN"
        )

        if result == "inserted":

            inserted += 1

        elif result == "updated":

            updated += 1

        # ========================================================
        # LAST PUNCH = OUT
        # ========================================================

        if last_punch:

            result = upsert_gate_attendance_log(
                row=last_punch["row"],
                log_type="OUT"
            )

            if result == "inserted":

                inserted += 1

            elif result == "updated":

                updated += 1

        # ========================================================
        # FIRST + LAST ARE ALLOWED
        # ========================================================

        allowed_times = {
            first_punch["check_time"]
        }

        if last_punch:

            allowed_times.add(
                last_punch["check_time"]
            )

        # ========================================================
        # REMOVE MIDDLE GATE PUNCHES
        # ========================================================

        deleted += remove_middle_gate_punches(
            lanatime_id=lanatime_id,
            attendance_date=attendance_date,
            allowed_times=allowed_times
        )

    # ============================================================
    # 7. MARK SUCCESSFUL SYNC
    # ============================================================

    mark_sync_completed()

    # ============================================================
    # COMMIT
    # ============================================================

    frappe.db.commit()

    # ============================================================
    # RESPONSE
    # ============================================================

    return {
        "success": True,
        "message": (
            "Lanatime Attendance Log synchronized successfully."
        ),
        "start_date": start_date,
        "end_date": end_date,
        "inserted": inserted,
        "updated": updated,
        "deleted": deleted,
    }


# ================================================================
# GET AUTOMATIC SYNC RANGE
# ================================================================

def get_sync_range():
    """
    First ever sync:

        2026-04-01 -> Today


    Later syncs:

        Latest last_synced_on date - 1 day
                ->
        Today


    One-day overlap is required because attendance day is:

        05:00 AM -> next day 04:59:59 AM
    """

    end_date = frappe.utils.today()

    # ============================================================
    # GET LATEST SYNC TIMESTAMP
    # ============================================================

    last_synced_on = frappe.db.sql(
        f"""
        SELECT MAX(last_synced_on)
        FROM `tab{DOCTYPE}`
        WHERE last_synced_on IS NOT NULL
        """,
        as_list=True
    )

    latest_sync = None

    if (
        last_synced_on
        and last_synced_on[0]
        and last_synced_on[0][0]
    ):
        latest_sync = last_synced_on[0][0]

    # ============================================================
    # FIRST SYNC
    # ============================================================

    if not latest_sync:

        return (
            INITIAL_SYNC_DATE,
            end_date
        )

    # ============================================================
    # SUBSEQUENT SYNC
    # ============================================================

    last_sync_date = frappe.utils.getdate(
        latest_sync
    )

    # ------------------------------------------------------------
    # One-day overlap
    # ------------------------------------------------------------

    start_date = frappe.utils.add_days(
        last_sync_date,
        -1
    )

    # ------------------------------------------------------------
    # Never go earlier than 2026-04-01
    # ------------------------------------------------------------

    if (
        frappe.utils.getdate(start_date)
        <
        frappe.utils.getdate(INITIAL_SYNC_DATE)
    ):

        start_date = INITIAL_SYNC_DATE

    return (
        str(start_date),
        str(end_date)
    )


# ================================================================
# NORMAL DEVICE UPSERT
# ================================================================

def upsert_normal_attendance_log(row):
    """
    Normal devices already provide correct IN / OUT values.

    Store the API value directly.
    """

    # ============================================================
    # API VALUES
    # ============================================================

    lanatime_id = clean_value(
        row.get("employeeID")
    )

    employee_name = clean_value(
        row.get("employeeName")
    )

    department = clean_value(
        row.get("deptName")
    )

    device_name = clean_value(
        row.get("snName")
    )

    check_time = parse_datetime(
        row.get("checktime")
    )

    log_type = clean_value(
        row.get("checktype")
    ).upper()

    # ============================================================
    # VALIDATION
    # ============================================================

    if not lanatime_id:
        return None

    if not check_time:
        return None

    if log_type not in (
        "IN",
        "OUT"
    ):
        return None

    # ============================================================
    # GET ERPNext EMPLOYEE
    # ============================================================

    employee = get_employee(
        lanatime_id
    )

    if not employee:

        log_missing_employee(
            lanatime_id=lanatime_id,
            employee_name=employee_name
        )

        return None

    # ============================================================
    # CHECK EXISTING RECORD
    # ============================================================

    existing = frappe.db.get_value(
        DOCTYPE,
        {
            "employee": employee,
            "check_time": check_time,
            "device_name": device_name,
        },
        "name"
    )

    # ============================================================
    # UPDATE EXISTING RECORD
    # ============================================================

    if existing:

        doc = frappe.get_doc(
            DOCTYPE,
            existing
        )

        changed = False

        # --------------------------------------------------------
        # Log Type
        # --------------------------------------------------------

        if doc.log_type != log_type:

            doc.log_type = log_type

            changed = True

        # --------------------------------------------------------
        # Department
        # --------------------------------------------------------

        if doc.department != department:

            doc.department = department

            changed = True

        # --------------------------------------------------------
        # Lanatime ID
        # --------------------------------------------------------

        if doc.lanatime_id != lanatime_id:

            doc.lanatime_id = lanatime_id

            changed = True

        # --------------------------------------------------------
        # Employee Name
        # --------------------------------------------------------

        if doc.employee_name != employee_name:

            doc.employee_name = employee_name

            changed = True

        # --------------------------------------------------------
        # Device Name
        # --------------------------------------------------------

        if doc.device_name != device_name:

            doc.device_name = device_name

            changed = True

        # --------------------------------------------------------
        # Save only if something changed
        # --------------------------------------------------------

        if changed:

            doc.last_synced_on = frappe.utils.now()

            doc.save(
                ignore_permissions=True
            )

            return "updated"

        return None

    # ============================================================
    # INSERT
    # ============================================================

    create_attendance_log(
        employee=employee,
        employee_name=employee_name,
        lanatime_id=lanatime_id,
        check_time=check_time,
        log_type=log_type,
        device_name=device_name,
        department=department
    )

    return "inserted"


# ================================================================
# SPECIAL GATE DEVICE UPSERT
# ================================================================

def upsert_gate_attendance_log(
    row,
    log_type
):
    """
    Gate device API checktype is ignored.

    log_type is supplied by our logic:

        First = IN
        Last  = OUT
    """

    # ============================================================
    # API VALUES
    # ============================================================

    lanatime_id = clean_value(
        row.get("employeeID")
    )

    employee_name = clean_value(
        row.get("employeeName")
    )

    department = clean_value(
        row.get("deptName")
    )

    check_time = parse_datetime(
        row.get("checktime")
    )

    # ============================================================
    # VALIDATE
    # ============================================================

    if not lanatime_id:
        return None

    if not check_time:
        return None

    # ============================================================
    # EMPLOYEE
    # ============================================================

    employee = get_employee(
        lanatime_id
    )

    if not employee:

        log_missing_employee(
            lanatime_id=lanatime_id,
            employee_name=employee_name
        )

        return None

    # ============================================================
    # CHECK EXISTING RECORD
    # ============================================================

    existing = frappe.db.get_value(
        DOCTYPE,
        {
            "employee": employee,
            "check_time": check_time,
            "device_name": GATE_DEVICE,
        },
        "name"
    )

    # ============================================================
    # UPDATE EXISTING
    # ============================================================

    if existing:

        doc = frappe.get_doc(
            DOCTYPE,
            existing
        )

        changed = False

        # --------------------------------------------------------
        # Correct IN / OUT
        # --------------------------------------------------------

        if doc.log_type != log_type:

            doc.log_type = log_type

            changed = True

        # --------------------------------------------------------
        # Department
        # --------------------------------------------------------

        if doc.department != department:

            doc.department = department

            changed = True

        # --------------------------------------------------------
        # Lanatime ID
        # --------------------------------------------------------

        if doc.lanatime_id != lanatime_id:

            doc.lanatime_id = lanatime_id

            changed = True

        # --------------------------------------------------------
        # Employee Name
        # --------------------------------------------------------

        if doc.employee_name != employee_name:

            doc.employee_name = employee_name

            changed = True

        # --------------------------------------------------------
        # Save
        # --------------------------------------------------------

        if changed:

            doc.last_synced_on = frappe.utils.now()

            doc.save(
                ignore_permissions=True
            )

            return "updated"

        return None

    # ============================================================
    # INSERT NEW GATE RECORD
    # ============================================================

    create_attendance_log(
        employee=employee,
        employee_name=employee_name,
        lanatime_id=lanatime_id,
        check_time=check_time,
        log_type=log_type,
        device_name=GATE_DEVICE,
        department=department
    )

    return "inserted"


# ================================================================
# CREATE ATTENDANCE LOG
# ================================================================

def create_attendance_log(
    employee,
    employee_name,
    lanatime_id,
    check_time,
    log_type,
    device_name,
    department
):
    """
    Create a Lanatime Attendance Log document.
    """

    doc = frappe.new_doc(
        DOCTYPE
    )

    doc.employee = employee

    doc.employee_name = employee_name

    doc.lanatime_id = lanatime_id

    doc.check_time = check_time

    doc.log_type = log_type

    doc.device_name = device_name

    doc.department = department

    doc.last_synced_on = frappe.utils.now()

    doc.insert(
        ignore_permissions=True
    )


# ================================================================
# REMOVE MIDDLE GATE PUNCHES
# ================================================================

def remove_middle_gate_punches(
    lanatime_id,
    attendance_date,
    allowed_times
):
    """
    For device WED3254100742:

    Keep only:

        First punch
        Last punch

    Delete all other gate punches for that employee
    inside the 05:00 -> 04:59 attendance window.
    """

    # ============================================================
    # GET WINDOW
    # ============================================================

    start_datetime, end_datetime = get_attendance_window(
        attendance_date
    )

    # ============================================================
    # GET EXISTING GATE RECORDS
    # ============================================================

    records = frappe.get_all(
        DOCTYPE,
        filters={
            "lanatime_id": lanatime_id,
            "device_name": GATE_DEVICE,
            "check_time": [
                "between",
                [
                    start_datetime,
                    end_datetime
                ]
            ]
        },
        fields=[
            "name",
            "check_time"
        ]
    )

    deleted = 0

    # ============================================================
    # DELETE MIDDLE RECORDS
    # ============================================================

    for record in records:

        record_time = frappe.utils.get_datetime(
            record.check_time
        )

        if record_time not in allowed_times:

            frappe.delete_doc(
                DOCTYPE,
                record.name,
                ignore_permissions=True,
                force=True
            )

            deleted += 1

    return deleted


# ================================================================
# GET ATTENDANCE DATE
# ================================================================

def get_attendance_date(check_time):
    """
    Universal attendance day:

        05:00:00 AM
            ->
        Next day 04:59:59 AM


    Examples:

        Sep 29 05:00 -> Sep 29
        Sep 29 08:00 -> Sep 29
        Sep 29 23:00 -> Sep 29

        Sep 30 00:30 -> Sep 29
        Sep 30 04:59 -> Sep 29

        Sep 30 05:00 -> Sep 30
    """

    if check_time.time() < time(
        5,
        0,
        0
    ):

        return (
            check_time.date()
            - timedelta(days=1)
        )

    return check_time.date()


# ================================================================
# GET ATTENDANCE WINDOW
# ================================================================

def get_attendance_window(
    attendance_date
):
    """
    Returns:

        attendance_date 05:00:00

                to

        next day 04:59:59
    """

    start_datetime = datetime.combine(
        attendance_date,
        time(
            5,
            0,
            0
        )
    )

    end_datetime = (
        start_datetime
        + timedelta(days=1)
        - timedelta(seconds=1)
    )

    return (
        start_datetime,
        end_datetime
    )


# ================================================================
# GET ERPNext EMPLOYEE
# ================================================================

def get_employee(
    lanatime_id
):
    """
    Match Lanatime employeeID against:

        Employee.custom_lanatime_id
    """

    return frappe.db.get_value(
        "Employee",
        {
            "custom_lanatime_id": lanatime_id
        },
        "name"
    )


# ================================================================
# MARK SYNC COMPLETED
# ================================================================

def mark_sync_completed():
    """
    last_synced_on is being used as the API synchronization
    checkpoint.

    We update the latest attendance record after every successful
    API call.

    This ensures the checkpoint advances even when the API returns
    only records that already exist.
    """

    records = frappe.get_all(
        DOCTYPE,
        fields=[
            "name"
        ],
        order_by="check_time desc",
        limit_page_length=1
    )

    if not records:
        return

    frappe.db.set_value(
        DOCTYPE,
        records[0].name,
        "last_synced_on",
        frappe.utils.now(),
        update_modified=False
    )


# ================================================================
# NORMALIZE API RESPONSE
# ================================================================

def normalize_api_response(payload):
    """
    Supports a direct list response and common wrapped responses.

    Expected Lanatime record fields:

        employeeID
        employeeName
        deptName
        checktime
        checktype
        snName
    """

    # ------------------------------------------------------------
    # API directly returned a list
    # ------------------------------------------------------------

    if isinstance(
        payload,
        list
    ):
        return payload

    # ------------------------------------------------------------
    # Wrapped response
    # ------------------------------------------------------------

    if isinstance(
        payload,
        dict
    ):

        # data
        if isinstance(
            payload.get("data"),
            list
        ):
            return payload.get("data")

        # message
        if isinstance(
            payload.get("message"),
            list
        ):
            return payload.get("message")

        # result
        if isinstance(
            payload.get("result"),
            list
        ):
            return payload.get("result")

    return []


# ================================================================
# CLEAN STRING
# ================================================================

def clean_value(value):
    """
    Safely convert API values to stripped strings.
    """

    if value is None:
        return ""

    return str(
        value
    ).strip()


# ================================================================
# PARSE DATETIME
# ================================================================

def parse_datetime(value):
    """
    Convert Lanatime checktime into Python datetime.
    """

    if not value:
        return None

    # ------------------------------------------------------------
    # Already datetime
    # ------------------------------------------------------------

    if isinstance(
        value,
        datetime
    ):
        return value

    # ------------------------------------------------------------
    # Frappe parser
    # ------------------------------------------------------------

    try:

        return frappe.utils.get_datetime(
            value
        )

    except Exception:

        frappe.log_error(
            (
                "Invalid Lanatime datetime: "
                f"{value}"
            ),
            "Lanatime Invalid Datetime"
        )

        return None


# ================================================================
# LOG MISSING EMPLOYEE
# ================================================================

def log_missing_employee(
    lanatime_id,
    employee_name
):
    """
    Record employees received from Lanatime that cannot be matched
    against Employee.custom_lanatime_id.
    """

    frappe.log_error(
        (
            f"Lanatime ID: {lanatime_id}\n"
            f"Employee: {employee_name}"
        ),
        "Lanatime Employee Not Found"
    )



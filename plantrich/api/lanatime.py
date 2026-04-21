import requests
import frappe
from frappe.utils import now_datetime, add_to_date
from datetime import datetime


@frappe.whitelist()
def fetch_lanatime_logs():

    # 🔹 Get last synced time from latest document
    last_synced = frappe.db.sql("""
        SELECT last_synced_on 
        FROM `tabLanatime Checkin`
        WHERE last_synced_on IS NOT NULL
        ORDER BY last_synced_on DESC
        LIMIT 1
    """, as_dict=True)

    if last_synced:
        last_synced = last_synced[0].get("last_synced_on")

    # 🔹 Start date with buffer
    if last_synced:
        start_dt = add_to_date(last_synced, minutes=-2)
        start_date = start_dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        start_date = "2026-04-01 00:00:00"

    end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 🔹 API call
    url = "https://plantrich.lanatime.in/api/RptTimecard/GetData"

    response = requests.get(
        url,
        params={
            "snName": "",
            "startDate": start_date,
            "endDate": end_date
        },
        auth=("it@plantrich.com", "ITpak@346"),
        timeout=30
    )

    if response.status_code != 200:
        frappe.throw(f"API Error: {response.text}")

    data = response.json()

    if not data:
        return "No new data"

    # 🔥 Sort by checktime
    data = sorted(data, key=lambda x: x.get("checktime"))

    DEVICE_LOG_TYPE = {
        "VGU6255300376": "IN",
        "VGU6255300293": "OUT",
        "WED3254100742": "OUT"
    }

    inserted = 0
    skipped = 0
    latest_time = None

    for row in data:

        lan_id = row.get("employeeID")
        check_time_raw = row.get("checktime")
        device = row.get("snName")

        if not lan_id or not check_time_raw:
            skipped += 1
            continue

        # Remove milliseconds
        check_time = check_time_raw.split(".")[0]

        check_time_dt = datetime.strptime(check_time, "%Y-%m-%d %H:%M:%S")

        # 🔁 Avoid duplicates
        if frappe.db.exists("Lanatime Checkin", {
            "lanatime_id": lan_id,
            "check_time": check_time
        }):
            skipped += 1
            continue

        # 🔗 Employee mapping
        employee = frappe.db.get_value(
            "Employee",
            {"custom_lanatime_id": lan_id},
            "name"
        )

        if not employee:
            skipped += 1
            continue

        log_type = DEVICE_LOG_TYPE.get(device, "IN")

        # 📥 Insert record
        doc = frappe.get_doc({
            "doctype": "Lanatime Checkin",
            "employee": employee,
            "employee_name": row.get("employeeName"),
            "lanatime_id": lan_id,
            "check_time": check_time,
            "log_type": log_type,
            "device_name": device,
            "department": row.get("deptName"),

            # 🔹 Store sync time in each record
            "last_synced_on": check_time_dt
        })

        doc.insert(ignore_permissions=True)
        inserted += 1

        # Track latest
        if not latest_time or check_time_dt > latest_time:
            latest_time = check_time_dt

    frappe.db.commit()

    return f"Inserted: {inserted}, Skipped: {skipped}"                                                                                                                     


# import requests
# import frappe
# from datetime import datetime
# from frappe.utils import add_to_date


# @frappe.whitelist()
# def fetch_lanatime_logs():

#     last_synced = frappe.db.sql("""
#         SELECT last_synced_on 
#         FROM `tabLanatime Checkin`
#         WHERE last_synced_on IS NOT NULL
#         ORDER BY last_synced_on DESC
#         LIMIT 1
#     """, as_dict=True)

#     if last_synced:
#         last_synced = last_synced[0].get("last_synced_on")

#     if last_synced:
#         start_dt = add_to_date(last_synced, minutes=-2)
#         start_date = start_dt.strftime("%Y-%m-%d %H:%M:%S")
#     else:
#         start_date = "2026-04-01 00:00:00"

#     end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     url = "https://plantrich.lanatime.in/api/RptTimecard/GetData"

#     response = requests.get(
#         url,
#         params={
#             "snName": "",
#             "startDate": start_date,
#             "endDate": end_date
#         },
#         auth=("it@plantrich.com", "ITpak@346"),
#         timeout=30
#     )

#     if response.status_code != 200:
#         frappe.throw(f"API Error: {response.text}")

#     data = response.json()

#     if not data:
#         return "No new data"

#     data = sorted(data, key=lambda x: x.get("checktime"))

#     DEVICE_LOG_TYPE = {
#         "VGU6255300376": "IN",
#         "VGU6255300293": "OUT",
#         "WED3254100742": "OUT"
#     }

#     created = 0
#     updated = 0
#     skipped = 0

#     for row in data:

#         lan_id = row.get("employeeID")
#         check_time_raw = row.get("checktime")
#         device = row.get("snName")

#         if not lan_id or not check_time_raw:
#             skipped += 1
#             continue

#         check_time = check_time_raw.split(".")[0]
#         check_time_dt = datetime.strptime(check_time, "%Y-%m-%d %H:%M:%S")
#         log_date = check_time_dt.date()

#         employee = frappe.db.get_value(
#             "Employee",
#             {"lanatime_id": lan_id},
#             "name"
#         )

#         if not employee:
#             skipped += 1
#             continue

#         log_type = DEVICE_LOG_TYPE.get(device, "IN")

#         # 🔍 Find existing record for same employee + type + same day
#         existing = frappe.db.sql("""
#             SELECT name, check_time 
#             FROM `tabLanatime Checkin`
#             WHERE employee = %s
#               AND log_type = %s
#               AND DATE(check_time) = %s
#             LIMIT 1
#         """, (employee, log_type, log_date), as_dict=True)

#         if not existing:
#             # ✅ CREATE
#             doc = frappe.get_doc({
#                 "doctype": "Lanatime Checkin",
#                 "employee": employee,
#                 "employee_name": row.get("employeeName"),
#                 "lanatime_id": lan_id,
#                 "check_time": check_time_dt,
#                 "log_type": log_type,
#                 "device_name": device,
#                 "department": row.get("deptName"),
#                 "last_synced_on": check_time_dt
#             })

#             doc.insert(ignore_permissions=True)
#             created += 1

#         else:
#             # 🔄 UPDATE
#             existing_doc = existing[0]
#             doc = frappe.get_doc("Lanatime Checkin", existing_doc.name)

#             if log_type == "IN":
#                 # keep earliest
#                 if check_time_dt < existing_doc.check_time:
#                     doc.check_time = check_time_dt
#                     updated += 1

#             elif log_type == "OUT":
#                 # keep latest
#                 if check_time_dt > existing_doc.check_time:
#                     doc.check_time = check_time_dt
#                     updated += 1

#             # update sync time
#             if not doc.last_synced_on or check_time_dt > doc.last_synced_on:
#                 doc.last_synced_on = check_time_dt

#             doc.save(ignore_permissions=True)

#     frappe.db.commit()

#     return f"Created: {created}, Updated: {updated}, Skipped: {skipped}"
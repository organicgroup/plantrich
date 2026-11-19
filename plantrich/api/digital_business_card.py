import json
from io import BytesIO

import frappe
import qrcode
from frappe.utils.file_manager import save_file


DOCTYPE = "Digital Business Card"

EDITABLE_FIELDS = [
    "full_name",
    "designation",
    "department",
    "profile_photo",
    "company",
    "email",
    "mobile_number",
    "alternatenumber",
    "office_phone",
    "website",
    "office_address",
    "google_map_link",
    "linkedin",
    "instagram",
    "facebook",
    "twitter",
    "whatsapp",
]

CARD_FIELDS = EDITABLE_FIELDS + ["qr_code"]


def get_request_data():
    """Read JSON or form data from the API request."""
    payload = frappe.request.get_json(silent=True) or {}

    if not isinstance(payload, dict):
        payload = {}

    if not payload:
        payload = dict(frappe.form_dict)

    device_id = payload.get("device_id")
    data = payload.get("data") or {}

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            frappe.throw("Invalid JSON in data parameter.")

    if not isinstance(data, dict):
        frappe.throw("The data parameter must be a JSON object.")

    if not device_id:
        frappe.throw("Device ID is required.")

    device_id = str(device_id).strip()

    if len(device_id) > 140:
        frappe.throw("Device ID cannot exceed 140 characters.")

    return device_id, data


def get_card_response(doc):
    """Return the business card fields for the frontend."""
    result = {
        "name": doc.name,
    }

    for field in CARD_FIELDS:
        result[field] = doc.get(field)

    return result


def generate_qr_code(doc):
    """
    Generate a QR PNG containing the unique Frappe document name
    and attach the image to the qr_code field.
    """

    # The QR contains the stable document ID, not the contact details.
    qr_content = doc.name

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(qr_content)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white",
    )

    image_buffer = BytesIO()
    image.save(image_buffer, format="PNG")

    image_content = image_buffer.getvalue()

    file_doc = save_file(
        fname=f"Business-Card-QR-{doc.name}.png",
        content=image_content,
        dt=DOCTYPE,
        dn=doc.name,
        is_private=0,
    )

    # Save the generated image URL in the Attach Image field.
    doc.db_set(
        "qr_code",
        file_doc.file_url,
        update_modified=False,
    )

    return file_doc.file_url


def find_card_by_device(device_id):
    """Find the card belonging to this device."""
    card_name = frappe.db.get_value(
        DOCTYPE,
        {"device_id": device_id},
        "name",
    )

    if card_name:
        return frappe.get_doc(DOCTYPE, card_name)

    return None


@frappe.whitelist(allow_guest=True)
def create_card():
    """
    Create a business card for a device.
    If the device already has a card, return the existing card.
    """

    device_id, data = get_request_data()

    existing_card = find_card_by_device(device_id)

    if existing_card:
        # Also repair the QR image if an existing card has no QR.
        if not existing_card.qr_code:
            generate_qr_code(existing_card)
            existing_card.reload()

        return {
            "success": True,
            "created": False,
            "message": "Business card already exists.",
            "card": get_card_response(existing_card),
        }

    doc = frappe.new_doc(DOCTYPE)
    doc.device_id = device_id

    for field in EDITABLE_FIELDS:
        if field in data:
            doc.set(field, data[field])

    doc.insert(ignore_permissions=True)

    # Generate and attach QR image after the document has a name.
    generate_qr_code(doc)

    doc.reload()

    return {
        "success": True,
        "created": True,
        "message": "Business card created successfully.",
        "card": get_card_response(doc),
    }


@frappe.whitelist(allow_guest=True)
def get_my_card(device_id=None):
    """Retrieve the business card belonging to a device."""

    device_id = device_id or frappe.form_dict.get("device_id")

    if not device_id:
        frappe.throw("Device ID is required.")

    doc = find_card_by_device(str(device_id).strip())

    if not doc:
        return {
            "success": True,
            "exists": False,
            "message": "No business card found for this device.",
            "card": None,
        }

    return {
        "success": True,
        "exists": True,
        "card": get_card_response(doc),
    }


@frappe.whitelist(allow_guest=True)
def update_card():
    """Update an existing business card using its device ID."""

    device_id, data = get_request_data()

    doc = find_card_by_device(device_id)

    if not doc:
        frappe.throw("No business card found for this device.")

    for field in EDITABLE_FIELDS:
        if field in data:
            doc.set(field, data[field])

    doc.save(ignore_permissions=True)

    # QR is not regenerated because the document name remains unchanged.
    doc.reload()

    return {
        "success": True,
        "message": "Business card updated successfully.",
        "card": get_card_response(doc),
    }

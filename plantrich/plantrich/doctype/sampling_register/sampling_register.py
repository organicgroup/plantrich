# Copyright (c) 2025, sammish and contributors
# For license information, please see license.txt

# import frappe
import json
import io
import os
import frappe
from frappe.utils import get_url
from pyqrcode import create as qr_create
from frappe.model.document import Document

class SamplingRegister(Document):
    def validate(self):
        self.generate_qr_code()

    def generate_qr_code(self):
        """Generate QR code for Sampling Register child table details and save it as a file."""

        if self.qr_code:
            return

        qr_image = io.BytesIO()
        
        # Collect child table data in JSON format
        qr_data_list = []
        if self.details:
            for child in self.details:
                qr_data_list.append({
                    "Sample Type": child.sample_type,
                    "Product": child.product_name,
					"Certifications": child.certifications,
                    "Lot/Batch": child.lotbatch_no,
                    "Sample Qty": child.sampling_qty,
                    
                    "Sampling Date": child.sampling_date,
                    "Sending Date": child.sending_date,
                    "Sent To": child.sent_to,
                    "Courier/Tracking No.": child.courier_name,
                    "Delivered Date": child.delivered_date,
					"Status": child.status,
                    "Remarks": child.remarksupdation
                })
        else:
            qr_data_list.append({"Message": "No Sampling Details Available"})

        qr_data = json.dumps(qr_data_list, indent=2)  # Convert to JSON format
        
        # Generate QR code using pyqrcode
        qr = qr_create(qr_data, error='H')  # High error correction
        qr.png(qr_image, scale=5, quiet_zone=1)  # Increase scale for better clarity

        # Generate a unique filename for the QR code image
        name = frappe.generate_hash(self.name, 13)
        filename = f"Sampling_QRCode-{name}.png".replace(os.path.sep, "__")

        # Save the file in the Frappe file system
        _file = frappe.get_doc({
            "doctype": "File",
            "file_name": filename,
            "attached_to_doctype": self.doctype,
            "attached_to_name": self.name,
            "attached_to_field": "qr_code",
            "is_private": 0,
            "content": qr_image.getvalue()
        })
        _file.save(ignore_permissions=True)

        # Set the QR code URL to the qr_code field
        self.qr_code = _file.file_url

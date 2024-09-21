# Copyright (c) 2024, sammish and contributors
# For license information, please see license.txt

import io
import os
import frappe
from frappe.utils import get_url
from pyqrcode import create as qr_create
from frappe.model.document import Document
import requests

class SecurityTracker(Document):
    def validate(self):
        self.create_driver_qr_code()
        self.create_visitor_qr_code()

    @frappe.whitelist()
    def get_elevation(self, latitude, longitude):
        # Fetch elevation from Open Elevation API
        url = f"https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}"
        response = requests.get(url)
        data = response.json()
        if data and 'results' in data and len(data['results']) > 0:
            return data['results'][0]['elevation']
        else:
            frappe.throw("Could not fetch elevation data.")
   
    def create_driver_qr_code(self):
        if not self.driver_qr_code:
            print_format = 'ST Print Driver'
            qr_image = io.BytesIO()
            link = f"{get_url()}/{self.doctype}/{self.name}?format={print_format}&key={self.get_signature()}"
            url = qr_create(link, error='L')
            url.png(qr_image, scale=2, quiet_zone=1)
            
            # Generate a unique filename for the QR code image
            name = frappe.generate_hash(self.name, 5)
            filename = f"Driver_QRCode-{name}.png".replace(os.path.sep, "__")
            
            # Save the file in the Frappe file system
            _file = frappe.get_doc({
                "doctype": "File",
                "file_name": filename,
                "attached_to_doctype": self.doctype,
                "attached_to_name": self.name,
                "attached_to_field": "driver_qr_code",
                "is_private": 0,
                "content": qr_image.getvalue()
            })
            _file.save(ignore_permissions=True)
            
            # Set the QR code URL to the driver_qr_code field
            self.db_set('driver_qr_code', _file.file_url)
    
    def create_visitor_qr_code(self):
        if not self.visitor_qr_code:
            print_format = 'ST Print Visitor'
            qr_image = io.BytesIO()
            link = f"{get_url()}/{self.doctype}/{self.name}?format={print_format}&key={self.get_signature()}"
            url = qr_create(link, error='L')
            url.png(qr_image, scale=2, quiet_zone=1)
            
            # Generate a unique filename for the QR code image
            name = frappe.generate_hash(self.name, 5)
            filename = f"Visitor_QRCode-{name}.png".replace(os.path.sep, "__")
            
            # Save the file in the Frappe file system
            _file = frappe.get_doc({
                "doctype": "File",
                "file_name": filename,
                "attached_to_doctype": self.doctype,
                "attached_to_name": self.name,
                "attached_to_field": "visitor_qr_code",
                "is_private": 0,
                "content": qr_image.getvalue()
            })
            _file.save(ignore_permissions=True)
            
            # Set the QR code URL to the visitor_qr_code field
            self.db_set('visitor_qr_code', _file.file_url)


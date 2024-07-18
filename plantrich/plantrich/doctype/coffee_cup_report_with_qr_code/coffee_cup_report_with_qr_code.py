
import io
import os

import frappe
from frappe.utils import get_url
from pyqrcode import create as qr_create
from frappe.model.document import Document

class CoffeeCupReportwithQRcode(Document):
	def validate(self):
		self.create_coffee_qr_code()

	def create_coffee_qr_code(self):
		if not self.coffee_qr_code:
			print_format = 'Coffee Cup Report Print Format'
			qr_image = io.BytesIO()
			link = get_url(self.doctype)+"/"+self.name+"?format=" + \
				print_format+"&key="+self.get_signature()
			url = qr_create(link, error='L')
			url.png(qr_image, scale=2, quiet_zone=1)
			name = frappe.generate_hash(self.name, 5)
			filename = f"Cup_Profile_QRCode-{name}.png".replace(os.path.sep, "__")
			_file = frappe.get_doc({
				"doctype": "File",
				"file_name": filename,
				"attached_to_doctype": self.get("doctype"),
				"attached_to_name": self.get("name"),
				"attached_to_field": "coffee_qr_code",
				"is_private": 0,
				"content": qr_image.getvalue()
			})
			_file.save(ignore_permissions=True)
			self.db_set('coffee_qr_code', _file.file_url)



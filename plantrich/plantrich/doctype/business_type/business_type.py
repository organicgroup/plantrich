# Copyright (c) 2023, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BusinessType(Document):
	def autoname(self):
		if self.business_type and self.company:
			self.business_type = self.business_type + "-" + frappe.db.get_value("Company", self.company, ["abbr"])

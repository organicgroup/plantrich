# Copyright (c) 2024, sammish and contributors
# For license information, please see license.txt

import frappe
# from frappe.model.document import Document

# In your main doctype file (machinery_operation_tracker.py)

from frappe.model.document import Document

class MachineryOperationTracker(Document):
    
    def validate(self):
        self.update_totals()

    def update_totals(self):
        total_diesel = 0
        total_electricity = 0
        total_biofuel = 0

        # Iterate through the child doctype records
        for detail in self.machinery_details:
            total_diesel += detail.diesel_consumed_liters or 0
            total_electricity += detail.electricity_consumedkw or 0
            total_biofuel += detail.biofuel_consumed or 0

        # Update main doctype fields
        self.total_diesel_consumed = total_diesel
        self.total_electricity_consumed = total_electricity
        self.total_biofuel_consumed = total_biofuel


# Copyright (c) 2024, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class COFFEECUPREPORT(Document):
    pass

@frappe.whitelist()
def get_chart_data(docname):
    doc = frappe.get_doc('COFFEE CUP REPORT', docname)

    # Labels for the chart display
    labels = [
        'Fragrance/Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body',
        'Balance', 'Overall', 'Sweetness', 'Uniformity', 'Clean Cup'
    ]
    
    # Values fetched from the doctype fields
    values = [
        doc.fragrancearoma,          # Ensure this matches the doctype field name
        doc.flavor_out_of_10,        # Ensure this matches the doctype field name
        doc.after_taste_out_of_10,   # Ensure this matches the doctype field name
        doc.acidity_out_of_10,       # Ensure this matches the doctype field name
        doc.bodyout_of_10,           # Ensure this matches the doctype field name
        doc.balance_out_of_10,       # Ensure this matches the doctype field name
        doc.overallout_of_10,        # Ensure this matches the doctype field name
        doc.sweetnessout_of_10,      # Ensure this matches the doctype field name
        doc.uniformityout_of_10,     # Ensure this matches the doctype field name
        doc.clean_cupout_of_10,      # Ensure this matches the doctype field name
    #doc.defectsout_of_10         # Ensure this matches the doctype field name
    ]

    return {
        'labels': labels,
        'values': values
    }
    
# def calculate_total_points(doc, method):
#     # Ensure all fields are not None and are numeric
#     fields = [
#         doc.fragrancearoma,
#         doc.flavor_out_of_10,
#         doc.after_taste_out_of_10,
#         doc.acidity_out_of_10,
#         doc.bodyout_of_10,
#         doc.balance_out_of_10,
#         doc.overallout_of_10,
#         doc.sweetnessout_of_10,
#         doc.uniformityout_of_10,
#         doc.clean_cupout_of_10
#     ]
    
#     total_points = sum(f or 0 for f in fields)  # Use 0 if any field is None

#     doc.total_points_sca = total_points

# def calculate_total_points(doc, method):
    if not frappe.has_permission("COFFEE CUP REPORT", "write"):
        frappe.throw(_("You do not have permission to perform this action"), frappe.PermissionError)
    
    fields = [
        doc.fragrancearoma,
        doc.flavor_out_of_10,
        doc.after_taste_out_of_10,
        doc.acidity_out_of_10,
        doc.bodyout_of_10,
        doc.balance_out_of_10,
        doc.overallout_of_10,
        doc.sweetnessout_of_10,
        doc.uniformityout_of_10,
        doc.clean_cupout_of_10
    ]
    
    total_points = sum(f or 0 for f in fields)  # Use 0 if any field is None

    doc.total_points_sca = total_points

import frappe

def get_item_total(doc, method):
    total_amount = 0
    for row in doc.custom_item:
        if row.rate == 0:
            row.rate = frappe.db.get_value("Item Price", {"item_code": row.item_code, "price_list": "Standard Selling", "selling":1}, ["price_list_rate"]) or 0
            row.amount = row.rate * row.qty
        total_amount += row.amount
    doc.custom_total_amount = total_amount

// Copyright (c) 2025, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Sampling Register", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Sampling Register Details', {
    no_of_bags: function(frm, cdt, cdn) {
        calculate_total(frm, cdt, cdn);
    },

    bulk_sample: function(frm, cdt, cdn) {
        calculate_total(frm, cdt, cdn);
    }
});

function calculate_total(frm, cdt, cdn) {
    let row = locals[cdt][cdn];

    let no_of_bags = row.no_of_bags || 0;
    let bulk_sample = row.bulk_sample || 0;

    frappe.model.set_value(cdt, cdn, 'total_qty_of_sample', no_of_bags * bulk_sample);
}
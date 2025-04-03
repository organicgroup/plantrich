// Copyright (c) 2025, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Bonus Receipt", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Bonus Receipt', {
    refresh(frm) {
        // Auto calculate when form loads (if needed)
        update_total_amount(frm);
    },
    before_save: function(frm) {
        // Calculate amounts before saving
        update_total_amount(frm);
    }
});

// Trigger calculation when fields change in the child table
frappe.ui.form.on('Bonus Receipt Details', {
    total_purchase_qty: function(frm, cdt, cdn) {
        calculate_bonus_amount(frm, cdt, cdn);
    },
    bonus_amout_per_kgnos: function(frm, cdt, cdn) {
        calculate_bonus_amount(frm, cdt, cdn);
    }
});

// Function to calculate bonus amount in INR per row and update total
function calculate_bonus_amount(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.total_purchase_qty && row.bonus_amout_per_kgnos) {
        row.bonus_amount_inr = row.total_purchase_qty * row.bonus_amout_per_kgnos;
        frappe.model.set_value(cdt, cdn, 'bonus_amount_inr', row.bonus_amount_inr);
    }
    update_total_amount(frm);
}

// Function to calculate and update the total bonus amount
function update_total_amount(frm) {
    let totalamt = 0;

    frm.doc.bonus_receipt_details.forEach(function(row) {
        if (row.bonus_amount_inr) {
            totalamt += row.bonus_amount_inr;
        }
    });

    let roundedTotalAmt = Math.round(totalamt);
    frm.set_value('total_amount', roundedTotalAmt);
    frm.refresh_field('total_amount');
}


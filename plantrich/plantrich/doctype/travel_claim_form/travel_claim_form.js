// Copyright (c) 2025, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Travel Claim Form", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Claim Breakdown Table', {
    quantity(frm, cdt, cdn) {
        calculate_amount_and_total(frm, cdt, cdn);
    },
    rate(frm, cdt, cdn) {
        calculate_amount_and_total(frm, cdt, cdn);
    },
    amount(frm, cdt, cdn) {
        update_total_amount(frm);
    }
});

function calculate_amount_and_total(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    let amount = flt(row.quantity) * flt(row.rate);
    frappe.model.set_value(cdt, cdn, 'amount', amount);
    update_total_amount(frm);
}

function update_total_amount(frm) {
    let total = 0;
    frm.doc.claim_breakdown_table.forEach(row => {
        total += flt(row.amount);
    });
    frm.set_value('total_amount', total);
}
///////////////////////////////////////////////////////////////////////////////////


frappe.ui.form.on('Travel Claim Form', {
    date_of_visit_from(frm) {
        calculate_number_of_days_excluding_sundays(frm);
    },
    date_of_visit_to(frm) {
        calculate_number_of_days_excluding_sundays(frm);
    }
});

function calculate_number_of_days_excluding_sundays(frm) {
    const from = frm.doc.date_of_visit_from;
    const to = frm.doc.date_of_visit_to;

    if (from && to) {
        const from_date = frappe.datetime.str_to_obj(from);
        const to_date = frappe.datetime.str_to_obj(to);

        if (to_date < from_date) {
            frm.set_value('number_of_days', 0);
            frappe.msgprint(__('End date must be after or equal to start date'));
            return;
        }

        let count = 0;
        let current = new Date(from_date);

        while (current <= to_date) {
            if (current.getDay() !== 0) {  // 0 = Sunday
                count++;
            }
            current.setDate(current.getDate() + 1);
        }

        frm.set_value('number_of_days', count);
    }
}

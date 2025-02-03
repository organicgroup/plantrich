// Copyright (c) 2025, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Funding Plan", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Funding Plan Details', {
    onload: function(frm) {
        set_opening_balance(frm);
        frm.refresh_field('funding_plan_details');
    },

    purchasesales: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        if (row.purchasesales === 'Sales' || row.purchasesales === 'Loan') {
            row.receipt = row.quantity_kg * row.amountkg;
            row.payment = 0;
        } else if (row.purchasesales === 'Purchase' || row.purchasesales === 'Expenses') {
            row.payment = row.quantity_kg * row.amountkg;
            row.receipt = 0;
        }

        update_balance(frm, cdt, cdn);
        set_opening_balance(frm);
        frm.refresh_field('funding_plan_details');
    },

    quantity_kg: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        if (row.purchasesales === 'Sales' || row.purchasesales === 'Loan') {
            row.receipt = row.quantity_kg * row.amountkg;
        } else if (row.purchasesales === 'Purchase' || row.purchasesales === 'Expenses') {
            row.payment = row.quantity_kg * row.amountkg;
        }

        update_balance(frm, cdt, cdn);
        set_opening_balance(frm);
        frm.refresh_field('funding_plan_details');
    },

    amountkg: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        if (row.purchasesales === 'Sales' || row.purchasesales === 'Loan') {
            row.receipt = row.quantity_kg * row.amountkg;
        } else if (row.purchasesales === 'Purchase' || row.purchasesales === 'Expenses') {
            row.payment = row.quantity_kg * row.amountkg;
        }

        update_balance(frm, cdt, cdn);
        set_opening_balance(frm);
        frm.refresh_field('funding_plan_details');
    },

    opening_balance: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        if (row.__index > 0) {
            const prev_row = locals[cdt][cdn - 1];
            row.opening_balance = prev_row.balance;
        }

        update_balance(frm, cdt, cdn);
        frm.refresh_field('funding_plan_details');
    }
});

// Function to calculate balance
function update_balance(frm, cdt, cdn) {
    const row = locals[cdt][cdn];

    if (!row.opening_balance) {
        return;
    }

    if (row.purchasesales === 'Sales' || row.purchasesales === 'Loan') {
        row.balance = row.opening_balance + row.receipt;
    } else if (row.purchasesales === 'Purchase' || row.purchasesales === 'Expenses') {
        row.balance = row.opening_balance - row.payment;
    }

    frm.refresh_field('funding_plan_details');
}

// Function to set opening balance
function set_opening_balance(frm) {
    const rows = frm.doc.funding_plan_details;

    for (let i = 1; i < rows.length; i++) {
        const current_row = rows[i];
        const previous_row = rows[i - 1];

        current_row.opening_balance = previous_row.balance || 0;

        update_balance(frm, current_row.doctype, current_row.name);
    }

    frm.refresh_field('funding_plan_details');
}

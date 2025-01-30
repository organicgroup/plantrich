// Copyright (c) 2025, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Funding Plan", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Funding Plan Details', {
    onload: function(frm) {
        // Loop through all the rows on load to set the opening_balance for each row
        set_opening_balance(frm);
        frm.refresh_field('funding_plan_details');
    },

    purchasesales: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        // Handle the 'purchasesales' change to calculate 'receipt' and 'payment' values
        if (row.purchasesales === 'Sales') {
            row.receipt = row.quantity_kg * row.amountkg;
            row.payment = 0;
        } else if (row.purchasesales === 'Purchase') {
            row.payment = row.quantity_kg * row.amountkg;
            row.receipt = 0;
        }

        // Call the function to update the balance after calculations
        update_balance(frm, cdt, cdn);
        set_opening_balance(frm);  // Ensure opening_balance is set dynamically
        frm.refresh_field('funding_plan_details');
    },

    quantity_kg: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        // Recalculate receipt or payment based on quantity_kg change
        if (row.purchasesales === 'Sales') {
            row.receipt = row.quantity_kg * row.amountkg;
        } else if (row.purchasesales === 'Purchase') {
            row.payment = row.quantity_kg * row.amountkg;
        }

        // Call the function to update the balance after calculations
        update_balance(frm, cdt, cdn);
        set_opening_balance(frm);  // Ensure opening_balance is set dynamically
        frm.refresh_field('funding_plan_details');
    },

    amountkg: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        // Recalculate receipt or payment based on amountkg change
        if (row.purchasesales === 'Sales') {
            row.receipt = row.quantity_kg * row.amountkg;
        } else if (row.purchasesales === 'Purchase') {
            row.payment = row.quantity_kg * row.amountkg;
        }

        // Call the function to update the balance after calculations
        update_balance(frm, cdt, cdn);
        set_opening_balance(frm);  // Ensure opening_balance is set dynamically
        frm.refresh_field('funding_plan_details');
    },

    opening_balance: function (frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        // Ensure that opening_balance for rows after the first is set to the balance of the previous row
        if (row.__index > 0) {
            const prev_row = locals[cdt][cdn - 1];  
            row.opening_balance = prev_row.balance;
        }

        // Call the function to update the balance after calculations
        update_balance(frm, cdt, cdn);
        frm.refresh_field('funding_plan_details');
    }
});

// Function to calculate the balance based on purchasesales, payment, and receipt
function update_balance(frm, cdt, cdn) {
    const row = locals[cdt][cdn];

    // Check if the row has a valid opening_balance before proceeding with the calculation
    if (!row.opening_balance) {
        return;
    }

    // Calculate balance for 'Sales' or 'Purchase'
    if (row.purchasesales === 'Sales') {
        row.balance = row.opening_balance + row.receipt;  // Sales: balance = opening_balance + receipt
    } else if (row.purchasesales === 'Purchase') {
        row.balance = row.opening_balance - row.payment;  // Purchase: balance = opening_balance - payment
    }

    frm.refresh_field('funding_plan_details');
}

// Function to set the opening_balance for each row based on the previous row's balance
function set_opening_balance(frm) {
    const rows = frm.doc.funding_plan_details;

    for (let i = 1; i < rows.length; i++) {
        const current_row = rows[i];
        const previous_row = rows[i - 1];

        // Set the opening_balance for the current row to the previous row's balance
        current_row.opening_balance = previous_row.balance || 0;

        // After setting opening_balance, update the balance for the current row
        update_balance(frm, current_row.doctype, current_row.name);
    }
    
    frm.refresh_field('funding_plan_details');
}

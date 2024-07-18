// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Civil Contract Bill Preparation', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Civil Contract Bill Preparation', {
	refresh(frm) {
		// your code here
	},
	 before_save: function(frm) {
        // Calculate amounts before saving
        calculateAmounts(frm);
        calculateBalance(frm);
       //calculateBalChild(frm);
    }
});


function calculateAmounts(frm)
{
    var totalAmount = 0;
    // Iterate over each row in the child table
    frm.doc.civil_details.forEach(function(row) {
        // Calculate the amount for the row
        var amount = row.quantity * row.rateunit;
        // Set the calculated amount in the row
        frappe.model.set_value(row.doctype, row.name, 'amount', amount);
        // Add the amount to the total
        totalAmount += amount;
    });
    // Set the total amount in a field on the parent form
    frappe.model.set_value(frm.doctype, frm.docname, 'total_amount', totalAmount);
    // Refresh the form to update the displayed amounts
    frm.refresh_field('civil_details');
    frm.refresh_field('total_amount');
}


function calculateBalance(frm)
{
     frm.doc.balance_to_be_paid = frm.doc.total_amount+frm.doc.previous_balance;
     frm.refresh_field('balance_to_be_paid');
}

/*function calculateBalChild(frm)
{
    //var totalAmount = 0;
    // Iterate over each row in the child table
    frm.doc.civil_contract_bill_child.forEach(function(row) {
        // Calculate the amount for the row
        row.balance_quantity_to_be_completed = row.total_estimated_quantity - row.billed_quantity;
        
    });
    
    frm.refresh_field('civil_contract_bill_child');
    frm.refresh_field('balance_quantity_to_be_completed');
}*/
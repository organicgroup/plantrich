// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('WORK STATEMENT', {
	//onload(frm) {
		// frappe.msgprint("On Load")
	//}
})

/*frappe.ui.form.on('LABOUR WORK DETAILS', {
	quantity(frm, cdt, cdn) {
		let row = locals[cdt][cdn]
		if(row.quantity && row.rateunit)
		row.amount = row.rateunit * row.quantity
		frm.refresh_field('labour_work_details')
	}
})

*/
frappe.ui.form.on('WORK STATEMENT', {
   /* refresh: function(frm) {
        // Add a custom button to calculate amounts
        frm.add_custom_button(__('Calculate Amounts'), function() {
            calculateAmounts(frm);
        });
    },*/

    before_save: function(frm) {
        // Calculate amounts before saving
        calculateAmounts(frm);
        calculateBalance(frm);
    }
});

function calculateAmounts(frm) {
    var totalAmount = 0;
    // Iterate over each row in the child table
    frm.doc.labour_work_details.forEach(function(row) {
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
    frm.refresh_field('labour_work_details');
    frm.refresh_field('total_amount');
}

function calculateBalance(frm)
{
    frm.doc.balance_amount_payable = frm.doc.total_amount - frm.doc.paid_amount;
     frm.refresh_field('balance_amount_payable');
}


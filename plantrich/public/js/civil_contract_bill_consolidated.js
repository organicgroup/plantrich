// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Civil Contract Bill Consolidated', {
    refresh(frm) {
        // Your code here
    },
    before_save(frm) {
        // Calculate amounts before saving
        calculateAmounts(frm);
        calculateBalChild(frm);
    }
});

function calculateAmounts(frm) {
    let totalAmount = 0;
    let subTotalRaftSlab = 0;
    let subTotalTopSlab = 0;
    let subTotalWall = 0;
    let subTotalRetainingWall = 0;
    let subTotalBrickWork = 0;
    let subTotalPlastering = 0;
    let subTotalSteelWork = 0;
    let subTotalOthers = 0;

    const calculateAmountForRows = (rows) => {
        let subTotal = 0;
        rows.forEach(row => {
            const amount = row.quantity * row.rateunit;
            frappe.model.set_value(row.doctype, row.name, 'amount', amount);
            subTotal += amount;
        });
        return subTotal;
    };

    if (frm.doc.civil_details_revised) totalAmount = calculateAmountForRows(frm.doc.civil_details_revised);
    if (frm.doc.civil_details_revised_raft_slab) subTotalRaftSlab = calculateAmountForRows(frm.doc.civil_details_revised_raft_slab);
    if (frm.doc.civil_details_revised_top_slab) subTotalTopSlab = calculateAmountForRows(frm.doc.civil_details_revised_top_slab);
    if (frm.doc.civil_details_revised_wall) subTotalWall = calculateAmountForRows(frm.doc.civil_details_revised_wall);
    if (frm.doc.civil_details_revised_retaining_wall) subTotalRetainingWall = calculateAmountForRows(frm.doc.civil_details_revised_retaining_wall);
    if (frm.doc.civil_details_revised_brick_work) subTotalBrickWork = calculateAmountForRows(frm.doc.civil_details_revised_brick_work);
    if (frm.doc.civil_details_revised_plastering) subTotalPlastering = calculateAmountForRows(frm.doc.civil_details_revised_plastering);
    if (frm.doc.civil_details_revised_steel_work) subTotalSteelWork = calculateAmountForRows(frm.doc.civil_details_revised_steel_work);
    if (frm.doc.civil_details_revised_others) subTotalOthers = calculateAmountForRows(frm.doc.civil_details_revised_others);

    const subTotalOfAllWorks = totalAmount + subTotalRaftSlab + subTotalTopSlab + subTotalWall + subTotalRetainingWall + subTotalBrickWork + subTotalPlastering + subTotalSteelWork + subTotalOthers;

    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_pcc', totalAmount);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_raft_slab', subTotalRaftSlab);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_top_slab', subTotalTopSlab);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_wall', subTotalWall);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_retaining_wall', subTotalRetainingWall);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_brick_work', subTotalBrickWork);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_plastering', subTotalPlastering);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_steel_work', subTotalSteelWork);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_others', subTotalOthers);
    frappe.model.set_value(frm.doctype, frm.docname, 'sub_total_of_all_works', subTotalOfAllWorks);

    frm.doc.balance_to_be_paid = subTotalOfAllWorks + frm.doc.previous_balance - frm.doc.paid_amount;
    frm.refresh_field('balance_to_be_paid');
    frm.refresh_field('civil_details_revised');
    frm.refresh_field('civil_details_revised_raft_slab');
    frm.refresh_field('civil_details_revised_wall');
    frm.refresh_field('civil_details_revised_top_slab');
    frm.refresh_field('civil_details_revised_retaining_wall');
    frm.refresh_field('civil_details_revised_brick_work');
    frm.refresh_field('civil_details_revised_plastering');
    frm.refresh_field('civil_details_revised_steel_work');
    frm.refresh_field('civil_details_revised_others');
    frm.refresh_field('sub_total_pcc');
    frm.refresh_field('sub_total_raft_slab');
    frm.refresh_field('sub_total_top_slab');
    frm.refresh_field('sub_total_wall');
    frm.refresh_field('sub_total_retaining_wall');
    frm.refresh_field('sub_total_brick_work');
    frm.refresh_field('sub_total_plastering');
    frm.refresh_field('sub_total_steel_work');
    frm.refresh_field('sub_total_others');
    frm.refresh_field('sub_total_of_all_works');
}

function calculateBalChild(frm) {
    if (frm.doc.civil_contract_bill_child) {
        frm.doc.civil_contract_bill_child.forEach(row => {
            row.balance_quantity_to_be_completed = row.total_estimated_quantity - row.billed_quantity;
        });
        frm.refresh_field('civil_contract_bill_child');
        frm.refresh_field('balance_quantity_to_be_completed');
    }
}

// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on('BMR REPORT', {
// 	// refresh: function(frm) {

// 	// }
// });

frappe.ui.form.on('BMR REPORT', {
    onload: function(frm) {
        if (frm.doc.processing_details) {
            frm.doc.processing_details.forEach(row => {
                calculate_losses(frm, row);
            });
            update_despatched_qty(frm); // Update parent field
            frm.refresh_field('processing_details');
        }
    },
    validate: function(frm) {
        if (frm.doc.processing_details) {
            frm.doc.processing_details.forEach(row => {
                calculate_losses(frm, row);
            });
            update_despatched_qty(frm); // Update parent field
            frm.refresh_field('processing_details');
        }
    }
});

frappe.ui.form.on('Processing Details', {
    hulling_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    roasting_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    grinding_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    sterilization_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    extraction_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    drying_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    powdering_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    other_process_loss: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    },
    processed_qty_from_inward_tc: function(frm, cdt, cdn) {
        calculate_losses(frm, locals[cdt][cdn]);
        update_despatched_qty(frm);
    }
});

function calculate_losses(frm, row) {
    if (!row) return;

    // Ensure all fields have valid numerical values
    row.hulling_loss = row.hulling_loss || 0;
    row.loss = row.loss || 0;
    row.roasting_loss = row.roasting_loss || 0;
    row.grinding_loss = row.grinding_loss || 0;
    row.sterilization_loss = row.sterilization_loss || 0;
    row.extraction_loss = row.extraction_loss || 0;
    row.drying_loss = row.drying_loss || 0;
    row.powdering_loss = row.powdering_loss || 0;
    row.other_process_loss = row.other_process_loss || 0;
    row.processed_qty_from_inward_tc = row.processed_qty_from_inward_tc || 0;

    // Calculate total loss
    row.total_loss = row.hulling_loss + row.loss 
                     + row.roasting_loss + row.grinding_loss 
                     + row.sterilization_loss + row.extraction_loss 
                     + row.drying_loss + row.powdering_loss 
                     + row.other_process_loss;

    // Calculate final quantity
    row.fg_qty = row.processed_qty_from_inward_tc - row.total_loss;

    frm.refresh_field('processing_details');
}

// Function to update parent field `despatched_qty`
function update_despatched_qty(frm) {
    let total_fg_qty = 0;

    if (frm.doc.processing_details) {
        frm.doc.processing_details.forEach(row => {
            total_fg_qty += flt(row.fg_qty || 0);
        });
    }

    frm.set_value('despatched_qty', total_fg_qty);
    frm.refresh_field('despatched_qty');
}


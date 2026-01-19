// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on('BMR REPORT', {
// 	// refresh: function(frm) {

// 	// }
// });

// frappe.ui.form.on('BMR REPORT', {
//     onload: function(frm) {
//         if (frm.doc.processing_details) {
//             frm.doc.processing_details.forEach(row => {
//                 calculate_losses(frm, row);
//             });
//             update_despatched_qty(frm); // Update parent field
//             frm.refresh_field('processing_details');
//         }
//     },
//     validate: function(frm) {
//         if (frm.doc.processing_details) {
//             frm.doc.processing_details.forEach(row => {
//                 calculate_losses(frm, row);
//             });
//             update_despatched_qty(frm); // Update parent field
//             frm.refresh_field('processing_details');
//         }
//     }
// });

// frappe.ui.form.on('Processing Details', {
//     hulling_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     pulping_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     roasting_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     grinding_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     sterilization_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     extraction_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     drying_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     powdering_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     other_process_loss: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     sample_qty: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     },
//     processed_qty_from_inward_tc: function(frm, cdt, cdn) {
//         calculate_losses(frm, locals[cdt][cdn]);
//         update_despatched_qty(frm);
//     }
// });

// function calculate_losses(frm, row) {
//     if (!row) return;

//     // Ensure all fields have valid numerical values
//     row.hulling_loss = row.hulling_loss || 0;
//     row.pulping_loss = row.pulping_loss || 0;
//     row.roasting_loss = row.roasting_loss || 0;
//     row.grinding_loss = row.grinding_loss || 0;
//     row.sterilization_loss = row.sterilization_loss || 0;
//     row.extraction_loss = row.extraction_loss || 0;
//     row.drying_loss = row.drying_loss || 0;
//     row.powdering_loss = row.powdering_loss || 0;
//     row.other_process_loss = row.other_process_loss || 0;

//     row.sample_qty = row.sample_qty || 0;
//     row.processed_qty_from_inward_tc = row.processed_qty_from_inward_tc || 0;
//     row.loss = row.loss || 0; // this is your additional loss field

//     // Calculate total loss (process losses only)
//     row.total_loss =
//         row.hulling_loss +
//         row.pulping_loss +
//         row.roasting_loss +
//         row.grinding_loss +
//         row.sterilization_loss +
//         row.extraction_loss +
//         row.drying_loss +
//         row.powdering_loss +
//         row.other_process_loss;

//     // total_qty = processed_qty_from_inward_tc - total_loss - loss
//     row.total_qty = row.processed_qty_from_inward_tc - row.total_loss - row.loss;

//     // fg_qty = total_qty - sample_qty
//     row.fg_qty = row.total_qty - row.sample_qty;

//     frm.refresh_field('processing_details');
// }

// // Function to update parent field `despatched_qty`
// function update_despatched_qty(frm) {
//     let total_fg_qty = 0;

//     if (frm.doc.processing_details) {
//         frm.doc.processing_details.forEach(row => {
//             total_fg_qty += flt(row.fg_qty || 0);
//         });
//     }

//     frm.set_value('despatched_qty', total_fg_qty);
//     frm.refresh_field('despatched_qty');
// }


frappe.ui.form.on('BMR REPORT', {
    onload: function (frm) {
        recalc_all_rows(frm);
    },
    refresh: function (frm) {
        recalc_all_rows(frm);
    },
    validate: function (frm) {
        recalc_all_rows(frm);
    }
});

function recalc_all_rows(frm) {
    if (frm.doc.processing_details && frm.doc.processing_details.length) {
        frm.doc.processing_details.forEach(row => {
            calculate_losses(frm, row);
        });
        update_despatched_qty(frm);
        frm.refresh_field('processing_details');
    }
}

frappe.ui.form.on('Processing Details', {
    hulling_loss: trigger_calc,
    pulping_loss: trigger_calc,
    roasting_loss: trigger_calc,
    grinding_loss: trigger_calc,
    sterilization_loss: trigger_calc,
    extraction_loss: trigger_calc,
    drying_loss: trigger_calc,
    powdering_loss: trigger_calc,
    other_process_loss: trigger_calc,
    processed_qty_from_inward_tc: trigger_calc,
    loss: trigger_calc,
    sample_qty: trigger_calc,

    processing_details_add: function (frm, cdt, cdn) {
        trigger_calc(frm, cdt, cdn);
    }
});

function trigger_calc(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    calculate_losses(frm, row);
    update_despatched_qty(frm);
}

function calculate_losses(frm, row) {
    if (!row) return;

    // Force numeric values
    row.hulling_loss = flt(row.hulling_loss);
    row.pulping_loss = flt(row.pulping_loss);
    row.roasting_loss = flt(row.roasting_loss);
    row.grinding_loss = flt(row.grinding_loss);
    row.sterilization_loss = flt(row.sterilization_loss);
    row.extraction_loss = flt(row.extraction_loss);
    row.drying_loss = flt(row.drying_loss);
    row.powdering_loss = flt(row.powdering_loss);
    row.other_process_loss = flt(row.other_process_loss);

    row.processed_qty_from_inward_tc = flt(row.processed_qty_from_inward_tc);
    row.loss = flt(row.loss);
    row.sample_qty = flt(row.sample_qty);

    // Calculate total process loss
    row.total_loss =
        row.hulling_loss +
        row.pulping_loss +
        row.roasting_loss +
        row.grinding_loss +
        row.sterilization_loss +
        row.extraction_loss +
        row.drying_loss +
        row.powdering_loss +
        row.other_process_loss;

    // total_qty = processed - total_loss - loss
    row.total_qty = row.processed_qty_from_inward_tc - row.total_loss - row.loss;

    // fg_qty = total_qty - sample_qty
    row.fg_qty = row.total_qty - row.sample_qty;

    frm.refresh_field('processing_details');
}

function update_despatched_qty(frm) {
    let total_fg_qty = 0;

    if (frm.doc.processing_details) {
        frm.doc.processing_details.forEach(row => {
            total_fg_qty += flt(row.fg_qty);
        });
    }

    frm.set_value('despatched_qty', total_fg_qty);
}

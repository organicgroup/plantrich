// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt


// frappe.ui.form.on('BMR REPORT', {
//     onload: function (frm) {
//         recalc_all_rows(frm);
//     },
//     refresh: function (frm) {
//         recalc_all_rows(frm);
//     },
//     validate: function (frm) {
//         recalc_all_rows(frm);
//     }
// });

// function recalc_all_rows(frm) {
//     if (frm.doc.processing_details && frm.doc.processing_details.length) {
//         frm.doc.processing_details.forEach(row => {
//             calculate_losses(frm, row);
//         });
//         update_despatched_qty(frm);
//         frm.refresh_field('processing_details');
//     }
// }

// frappe.ui.form.on('Processing Details', {
//     hulling_loss: trigger_calc,
//     pulping_loss: trigger_calc,
//     roasting_loss: trigger_calc,
//     grinding_loss: trigger_calc,
//     sterilization_loss: trigger_calc,
//     extraction_loss: trigger_calc,
//     drying_loss: trigger_calc,
//     powdering_loss: trigger_calc,
//     other_process_loss: trigger_calc,
//     processed_qty_from_inward_tc: trigger_calc,
//     loss: trigger_calc,
//     sample_qty: trigger_calc,

//     processing_details_add: function (frm, cdt, cdn) {
//         trigger_calc(frm, cdt, cdn);
//     }
// });

// function trigger_calc(frm, cdt, cdn) {
//     let row = locals[cdt][cdn];
//     calculate_losses(frm, row);
//     update_despatched_qty(frm);
// }

// function calculate_losses(frm, row) {
//     if (!row) return;

//     // Force numeric values
//     row.hulling_loss = flt(row.hulling_loss);
//     row.pulping_loss = flt(row.pulping_loss);
//     row.roasting_loss = flt(row.roasting_loss);
//     row.grinding_loss = flt(row.grinding_loss);
//     row.sterilization_loss = flt(row.sterilization_loss);
//     row.extraction_loss = flt(row.extraction_loss);
//     row.drying_loss = flt(row.drying_loss);
//     row.powdering_loss = flt(row.powdering_loss);
//     row.other_process_loss = flt(row.other_process_loss);

//     row.processed_qty_from_inward_tc = flt(row.processed_qty_from_inward_tc);
//     row.loss = flt(row.loss);
//     row.sample_qty = flt(row.sample_qty);

//     // Calculate total process loss
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

//     // total_qty = processed - total_loss - loss
//     row.total_qty = row.processed_qty_from_inward_tc - row.total_loss - row.loss;

//     // fg_qty = total_qty - sample_qty
//     row.fg_qty = row.total_qty - row.sample_qty;

//     frm.refresh_field('processing_details');
// }

// function update_despatched_qty(frm) {
//     let total_fg_qty = 0;

//     if (frm.doc.processing_details) {
//         frm.doc.processing_details.forEach(row => {
//             total_fg_qty += flt(row.fg_qty);
//         });
//     }

//     frm.set_value('despatched_qty', total_fg_qty);
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


frappe.ui.form.on('Processing Details', {

    // Whenever any field in Processing Details is changed
    onchange: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        calculate_losses(frm, row);
        update_despatched_qty(frm);
    },

    processing_details_add: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        calculate_losses(frm, row);
        update_despatched_qty(frm);
    },

    processing_details_remove: function (frm) {
        update_despatched_qty(frm);
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


function calculate_losses(frm, row) {

    if (!row) return;

    // Existing loss fields
    row.hulling_loss = flt(row.hulling_loss);
    row.pulping_loss = flt(row.pulping_loss);
    row.roasting_loss = flt(row.roasting_loss);
    row.grinding_loss = flt(row.grinding_loss);
    row.sterilization_loss = flt(row.sterilization_loss);
    row.extraction_loss = flt(row.extraction_loss);
    row.drying_loss = flt(row.drying_loss);
    row.powdering_loss = flt(row.powdering_loss);
    row.other_process_loss = flt(row.other_process_loss);

    // New loss fields
    row.colour_sorting = flt(row.colour_sorting);
    row.pb_bold = flt(row.pb_bold);
    row.bits = flt(row.bits);
    row.cadoor_rejection = flt(row.cadoor_rejection);
    row.md = flt(row.md);
    row.bleed_run = flt(row.bleed_run);

    // Quantity fields
    row.processed_qty_from_inward_tc =
        flt(row.processed_qty_from_inward_tc);

    row.loss = flt(row.loss);

    row.sample_qty = flt(row.sample_qty);


    // ==========================================
    // TOTAL LOSS
    // ==========================================

    row.total_loss =
        row.hulling_loss +
        row.pulping_loss +
        row.roasting_loss +
        row.grinding_loss +
        row.sterilization_loss +
        row.extraction_loss +
        row.drying_loss +
        row.powdering_loss +
        row.other_process_loss +
        row.colour_sorting +
        row.pb_bold +
        row.bits +
        row.cadoor_rejection +
        row.md +
        row.bleed_run;


    // ==========================================
    // TOTAL QTY
    // ==========================================

    row.total_qty =
        row.processed_qty_from_inward_tc -
        row.total_loss -
        row.loss;


    // ==========================================
    // FG QTY
    // ==========================================

    row.fg_qty =
        row.total_qty -
        row.sample_qty;


    // Refresh child table
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
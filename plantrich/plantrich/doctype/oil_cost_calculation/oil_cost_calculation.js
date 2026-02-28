frappe.ui.form.on('Oil Cost Calculation', {

    raw_material_qty: function(frm) {
        frm.trigger('calculate_all');
    },

    raw_material_rate: function(frm) {
        frm.trigger('calculate_all');
    },

    running_hr: function(frm) {
        frm.trigger('calculate_all');
    },

    diesel: function(frm) {
        frm.trigger('calculate_all');
    },

    other_cost: function(frm) {
        frm.trigger('calculate_all');
    },

    calculate_all: function(frm) {

        let running_hr = frm.doc.running_hr || 0;
        let raw_material_qty = frm.doc.raw_material_qty || 0;
        let raw_material_rate = frm.doc.raw_material_rate || 0;
        let other_cost = frm.doc.other_cost || 0;
        let diesel = frm.doc.diesel || 0;

        // Running hour based costs
        let firewood = running_hr * 579;
        let electricity = running_hr * 570;
        let manpower = running_hr * 140;
        let supervision = running_hr * 375;

        frm.set_value('firewood', firewood);
        frm.set_value('electricity', electricity);
        frm.set_value('manpower', manpower);
        frm.set_value('supervision', supervision);

        // Raw material cost
        let raw_total_cost = raw_material_qty * raw_material_rate;
        frm.set_value('raw_total_cost', raw_total_cost);

        // Total production cost
        let total_production_cost =
            raw_total_cost +
            other_cost +
            diesel +
            supervision +
            manpower +
            electricity +
            firewood;

        frm.set_value('total_production_cost', total_production_cost);
    }
});
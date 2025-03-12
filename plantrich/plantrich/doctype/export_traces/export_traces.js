// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Export Traces', {
    onload: function(frm) {
        check_dates(frm);
    },

    before_save: function(frm) {
        const messages = [];
        messages.push(...check_dates(frm));
        messages.push(...validate_date_fields(frm));

        if (messages.length > 0) {
            frappe.msgprint({
                title: __('Alert Messages'),
                indicator: 'red',
               // message: messages.join('<br>')
            });
            frappe.validated = false;
        }
    },

    qty_in_kg: function(frm) {
        calculate_total_amount(frm);
    },

    price_kg_inr: function(frm) {
        calculate_total_amount(frm);
    },

    pricekg_euro: function(frm) {
        calculate_total_amount(frm);
    },

    pricekg_usd: function(frm) {
        calculate_total_amount(frm);
    },

    currency: function(frm) {
        calculate_total_amount(frm);
    }
});

function check_dates(frm) {
    const dateFields = {
        'date_ptc': 'Provisional Transaction Certificate',
        'spice_board_test_approved_date': 'Spice Board Test Approved Date'
    };

    let current_date = new Date();
    current_date.setHours(0, 0, 0, 0);

    let messages = [];

    Object.keys(dateFields).forEach(field => {
        if (frm.doc[field]) {
            let field_date = frappe.datetime.str_to_obj(frm.doc[field]);
            let diffDays = frappe.datetime.get_day_diff(current_date, field_date);

            if (diffDays >= 30) {
                let field_label = dateFields[field];
                messages.push(__(`The ${field_label} is overdue.`));
            }
        }
    });

    return messages;
}

function validate_date_fields(frm) {
    let messages = [];
    if (frm.doc.batch_creation_date) {
        let batch_creation_date = frappe.datetime.str_to_obj(frm.doc.batch_creation_date);
        console.log('Batch Creation Date:', batch_creation_date);

        const fieldsToCheck = [
            'sales_invoice_date',
            'e_way_bill_date',
            'ico_date',
            'do_date',
            'coi_no_and_date',
            'shipping_bill_date',
            'coi_date'
        ];

        fieldsToCheck.forEach(field => {
            if (frm.doc[field]) {
                let field_date = frappe.datetime.str_to_obj(frm.doc[field]);
                console.log('Field:', field, 'Field Date:', field_date);

                if (field_date && field_date < batch_creation_date) {
                    let field_label = frappe.meta.get_docfield(frm.doc.doctype, field, frm.doc.name).label;
                    messages.push(__(`The ${field_label} cannot be earlier than the Batch Creation Date.`));
                }
            }
        });
    }
    return messages;
}

function calculate_total_amount(frm) {
    let qty = frm.doc.qty_in_kg || 0;
    let total = 0;

    switch (frm.doc.currency) {
        case 'INR':
            total = qty * (frm.doc.price_kg_inr || 0);
            break;
        case 'EUR':
            total = qty * (frm.doc.pricekg_euro || 0);
            break;
        case 'USD':
            total = qty * (frm.doc.pricekg_usd || 0);
            break;
        default:
            total = 0;
    }

    frm.set_value('total_amount', total);
}


frappe.ui.form.on('Export Traces', {
    total_amount: function(frm) {
        calculate_total_amount_inr(frm);
    },
    usd_value: function(frm) {
        calculate_total_amount_inr(frm);
    },
    currency: function(frm) {
        calculate_total_amount_inr(frm);
    }
});

function calculate_total_amount_inr(frm) {
    if (frm.doc.currency === 'USD') {
        frm.set_value('total_amount_inr', frm.doc.total_amount * frm.doc.usd_value);
    } else {
        frm.set_value('total_amount_inr', 0); // Reset if not USD
    }
}

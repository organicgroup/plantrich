



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
                message: messages.join('<br>')
            });
            frappe.validated = false;  
        }
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
        console.log('Batch Creation Date:', batch_creation_date);  // Debugging log

        const fieldsToCheck = [
            'sales_invoice_date',
            'e_way_bill_date',
            'ico_date',
            'do_date',
            'coi_no_and_date',
            'shipping_bill_date'
        ];

        fieldsToCheck.forEach(field => {
            if (frm.doc[field]) {
                let field_date = frappe.datetime.str_to_obj(frm.doc[field]);
                console.log('Field:', field, 'Field Date:', field_date);  // Debugging log

                if (field_date && field_date < batch_creation_date) {
                    let field_label = frappe.meta.get_docfield(frm.doc.doctype, field, frm.doc.name).label;
                    messages.push(__(`The ${field_label} cannot be earlier than the Batch Creation Date.`));
                }
            }
        });
    }
    return messages;
}






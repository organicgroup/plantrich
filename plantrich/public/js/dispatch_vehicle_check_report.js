// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('DISPATCH VEHICLE CHECK REPORT', {
    refresh: function(frm) {
        // Add custom CSS for the buttons
        let style = document.createElement('style');
        style.innerHTML = `
            .btn-custom-add {
                background-color: #4CAF50; /* Green */
                color: white;
                margin-top: 10px;
                margin-right: 10px;
            }
            .btn-custom-subtract {
                background-color: #f44336; /* Red */
                color: white;
                margin-top: 10px;
            }
        `;
        document.head.appendChild(style);

        // Function to create buttons and append them below the specific field
        function create_buttons() {
            // Create Add button
            let addButton = $('<button/>', {
                text: 'Add',
                class: 'btn btn-custom-add',
                click: function() {
                    let count = frm.doc.total || 0;
                    count += 1;
                    frm.set_value('total', count);
                    frm.refresh_field('total');
                }
            });

            // Create Subtract button
            let subtractButton = $('<button/>', {
                text: 'Subtract',
                class: 'btn btn-custom-subtract',
                click: function() {
                    let count = frm.doc.total || 0;
                    if (count > 0) { // Prevent negative values
                        count -= 1;
                    }
                    frm.set_value('total', count);
                    frm.refresh_field('total');
                }
            });

            // Append buttons to the specific field
            frm.fields_dict.boxsack_loading_tracker.$wrapper.append(addButton);
            frm.fields_dict.boxsack_loading_tracker.$wrapper.append(subtractButton);
        }

        // Ensure buttons are created only once
        if (!frm.custom_buttons_added) {
            create_buttons();
            frm.custom_buttons_added = true;
        }

        // Initialize the value field to 1 if it is undefined
        if (frm.doc.value === undefined) {
            frm.set_value('value', 1);
        }
        // Initialize the total field to 0 if it is undefined
        if (frm.doc.total === undefined) {
            frm.set_value('total', 0);
        }

        // Refresh the fields to update status
        frm.refresh_field('value');
        frm.refresh_field('total');
    }
});


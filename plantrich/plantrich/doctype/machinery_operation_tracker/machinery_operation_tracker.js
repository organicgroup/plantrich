// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Machinery Operation Tracker', {
// 	// refresh: function(frm) {

// 	// }
// });

// frappe.ui.form.on('Machinery Operation Details', {
//     // Trigger when the start_time or end_time fields are changed in the child table
//     start_time: function(frm, cdt, cdn) {
//         calculate_hours(frm, cdt, cdn);
//     },
//     end_time: function(frm, cdt, cdn) {
//         calculate_hours(frm, cdt, cdn);
//     }
// });

// function calculate_hours(frm, cdt, cdn) {
//     // Get the row data for the current child row
//     var row = locals[cdt][cdn];

//     if (row.start_time && row.end_time) {
//         // Use moment.js to calculate the difference between start_time and end_time
//         let start_time = moment(row.start_time, "HH:mm:ss");
//         let end_time = moment(row.end_time, "HH:mm:ss");

//         // Calculate the duration in hours
//         let duration = moment.duration(end_time.diff(start_time));
//         let hours = duration.asHours();

//         // Handle the case where the end time is past midnight (negative duration)
//         if (hours < 0) {
//             hours += 24;
//         }

//         // Set the calculated hours into the hours_operated field
//         frappe.model.set_value(cdt, cdn, 'hours_operated', hours);
//     }
// }

frappe.ui.form.on('Machinery Operation Details', {
    start_time: function(frm, cdt, cdn) {
        calculate_hours(frm, cdt, cdn);
    },
    end_time: function(frm, cdt, cdn) {
        calculate_hours(frm, cdt, cdn);
    }
});

function calculate_hours(frm, cdt, cdn) {
    var row = locals[cdt][cdn];

    if (row.start_time && row.end_time) {
        // Parse start and end times
        let start_time = moment(row.start_time, "HH:mm:ss");
        let end_time = moment(row.end_time, "HH:mm:ss");

        // Calculate total duration in minutes
        let duration = moment.duration(end_time.diff(start_time));
        let total_minutes = duration.asMinutes();

        // Adjust for negative time differences (if end_time is after midnight)
        if (total_minutes < 0) {
            total_minutes += 1440;  // Add 24 hours (in minutes)
        }

        // Convert total minutes to hours and remaining minutes
        let hours = Math.floor(total_minutes / 60);  // Full hours
        let minutes = Math.floor(total_minutes % 60);  // Remaining minutes

        // Combine hours and minutes in H.MM format
        let total_hours_operated = hours + "." + (minutes < 10 ? '0' : '') + minutes;

        // Set the value of hours_operated field
        frappe.model.set_value(cdt, cdn, 'hours_operated', total_hours_operated);
    }
}



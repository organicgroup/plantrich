// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Security Tracker', {
    fetch_location: function(frm) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                let latitude = position.coords.latitude;
                let longitude = position.coords.longitude;

                // Optionally, you can use an API to fetch elevation
                // For simplicity, we're just setting lat/long
                frm.set_value('latitude', latitude);
                frm.set_value('longitude', longitude);

                // If you have an API to get the elevation, fetch and set the elevation here
                // For example, using Open Elevation API (pseudo-code):
                // frappe.call({
                //     method: 'your_custom_method_to_fetch_elevation',
                //     args: { latitude: latitude, longitude: longitude },
                //     callback: function(r) {
                //         if(r.message) {
                //             frm.set_value('elevation', r.message.elevation);
                //         }
                //     }
                // });

                frappe.msgprint(`Location fetched successfully: Latitude: ${latitude}, Longitude: ${longitude}`);
                frm.refresh_field('latitude');
                frm.refresh_field('longitude');
                frm.refresh_field('elevation');
            }, function(error) {
                frappe.msgprint("Error fetching location: " + error.message);
            });
        } else {
            frappe.msgprint("Geolocation is not supported by this browser.");
        }
    }
});


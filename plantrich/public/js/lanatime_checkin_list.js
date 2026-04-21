frappe.listview_settings['Lanatime Checkin'] = {
    onload: function(listview) {

        listview.page.add_button(__('Sync Lanatime'), function() {
            frappe.call({
                method: "plantrich.api.lanatime.fetch_lanatime_logs",
                freeze: true,
                freeze_message: "Syncing Lanatime Data...",
                callback: function(r) {
                    frappe.msgprint(r.message || "Sync Completed");
                    listview.refresh();
                }
            });
        });

    }
};
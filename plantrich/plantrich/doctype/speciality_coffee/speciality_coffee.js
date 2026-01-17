// Copyright (c) 2026, sammish and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Speciality Coffee", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('SC Berry Harvest', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}

frappe.ui.form.on('SC Cherry Reception', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}

frappe.ui.form.on('SC Processing Selection', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}

frappe.ui.form.on('SC Fermentation Log', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}


frappe.ui.form.on('SC Washing Log', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}


frappe.ui.form.on('SC Drying Log', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}


frappe.ui.form.on('SC Hulling Storage', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}

frappe.ui.form.on('SC Sample Roasting', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}

frappe.ui.form.on('SC Cupping Log', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}

frappe.ui.form.on('SC Batch Status', {
    start: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    },
    end: function(frm, cdt, cdn) {
        calculate_duration(cdt, cdn);
    }
});

function calculate_duration(cdt, cdn) {
    let row = locals[cdt][cdn];

    if (row.start && row.end) {
        let start = moment(row.start);
        let end = moment(row.end);

        if (end.isAfter(start)) {
            let diff = moment.duration(end.diff(start));

            let hours = Math.floor(diff.asHours());
            let minutes = diff.minutes();

            let parts = [];
            if (hours > 0) parts.push(hours + " hour" + (hours > 1 ? "s" : ""));
            if (minutes > 0) parts.push(minutes + " minute" + (minutes > 1 ? "s" : ""));

            frappe.model.set_value(cdt, cdn, "duration", parts.join(" "));
        } else {
            frappe.model.set_value(cdt, cdn, "duration", "");
        }
    }
}

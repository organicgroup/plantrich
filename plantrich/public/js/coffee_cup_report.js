// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt


// frappe/public/js/coffee_cup_report.js

frappe.ui.form.on('COFFEE CUP REPORT', {
    refresh: function(frm) {
        // Add a console log to verify if the refresh function is called
        console.log("Refresh function called");

        // Check if the custom_chart_wrapper field exists
        if (frm.fields_dict.custom_chart_wrapper) {
            // Add the custom button to show the chart
            frm.add_custom_button('Show Radar Chart', () => {
                console.log("Show Chart button clicked");
                frappe.call({
                    method: 'plantrich.plantrich.doctype.coffee_cup_report.coffee_cup_report.get_chart_data',
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(response) {
                        const data = response.message;
                        const labels = data.labels;
                        const values = data.values;

                        // Clear the wrapper
                        let wrapper = frm.fields_dict.custom_chart_wrapper.$wrapper.empty();
                        console.log('$wrapper:', wrapper);
                        let canvas = document.createElement('canvas');
                        canvas.id = 'myRadarChart';
                        canvas.width = 400;
                        canvas.height = 400;
                        wrapper.append(canvas);
                        console.log('$wrapper:', wrapper);

                        // Ensure Chart.js is available
                        const checkChart = () => {
                            if (typeof Chart !== 'undefined') {
                                const ctx = document.getElementById('myRadarChart').getContext('2d');
                                const chartData = {
                                    labels: labels,
                                    datasets: [{
                                        label: 'Cup Profile',
                                        data: values,
                                        fill: true,
                                        backgroundColor: 'rgba(34, 202, 236, 0.2)',
                                        borderColor: 'rgba(34, 202, 236, 1)',
                                        pointBackgroundColor: 'rgba(34, 202, 236, 1)',
                                        pointBorderColor: '#fff',
                                        pointHoverBackgroundColor: '#fff',
                                        pointHoverBorderColor: 'rgba(34, 202, 236, 1)'
                                    }]
                                };

                                const options = {
                                    scale: {
                                        ticks: {
                                            beginAtZero: true,
                                            max: 10
                                        }
                                    }
                                };

                                new Chart(ctx, {
                                    type: 'radar',
                                    data: chartData,
                                    options: options
                                });
                            } else {
                                setTimeout(checkChart, 50);
                            }
                        };

                        checkChart();
                    }
                });
            });
        }
    }
});


/*frappe.ui.form.on('COFFEE CUP REPORT', {
    refresh: function(frm) {
        // Add a console log to verify if the refresh function is called
        console.log("Refresh function called");

        // Call the custom method to calculate and update the total points
        frappe.call({
            method: 'plantrich.plantrich.doctype.coffee_cup_report.coffee_cup_report.calculate_total_points',
            args: {
                doc: frm.doc
            },
            callback: function(response) {
                frm.refresh_field('total_points_sca');
                console.log("Total Points SCA updated: ", frm.doc.total_points_sca);
            }
        });

        // Check if the custom_chart_wrapper field exists
        if (frm.fields_dict.custom_chart_wrapper) {
            // Add the custom button to show the chart
            frm.add_custom_button('Show Chart', () => {
                console.log("Show Chart button clicked");
                frappe.call({
                    method: 'plantrich.plantrich.doctype.coffee_cup_report.coffee_cup_report.get_chart_data',
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(response) {
                        const data = response.message;
                        const labels = data.labels;
                        const values = data.values;

                        // Clear the wrapper
                        let wrapper = frm.fields_dict.custom_chart_wrapper.$wrapper.empty();
                        console.log('$wrapper:', wrapper);
                        let canvas = document.createElement('canvas');
                        canvas.id = 'myRadarChart';
                        canvas.width = 400;
                        canvas.height = 400;
                        wrapper.append(canvas);
                        console.log('$wrapper:', wrapper);

                        // Ensure Chart.js is available
                        const checkChart = () => {
                            if (typeof Chart !== 'undefined') {
                                const ctx = document.getElementById('myRadarChart').getContext('2d');
                                const chartData = {
                                    labels: labels,
                                    datasets: [{
                                        label: 'Cup Profile',
                                        data: values,
                                        fill: true,
                                        backgroundColor: 'rgba(34, 202, 236, 0.2)',
                                        borderColor: 'rgba(34, 202, 236, 1)',
                                        pointBackgroundColor: 'rgba(34, 202, 236, 1)',
                                        pointBorderColor: '#fff',
                                        pointHoverBackgroundColor: '#fff',
                                        pointHoverBorderColor: 'rgba(34, 202, 236, 1)'
                                    }]
                                };

                                const options = {
                                    scale: {
                                        ticks: {
                                            beginAtZero: true,
                                            max: 10
                                        }
                                    }
                                };

                                new Chart(ctx, {
                                    type: 'radar',
                                    data: chartData,
                                    options: options
                                });
                            } else {
                                setTimeout(checkChart, 50);
                            }
                        };

                        checkChart();
                    }
                });
            });
        }
    }
});
*/
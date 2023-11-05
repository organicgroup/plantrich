frappe.ui.form.on("Sales Invoice", {
    before_load:function(frm){
        frm.trigger("get_business_type")
    },
    get_business_type:function(frm){
        if(frm.doc.company){
            frm.set_query('custom_business_type', function(doc) {
                return {
                    filters: {
                        "company": cur_frm.doc.company
                    }
                };
            });
        }
    },
    company:function(frm){
        frm.set_value("custom_business_type", "")
        frm.trigger("get_business_type")
    },
    custom_business_type: function(frm){
        if(frm.doc.custom_business_type && frm.is_new()){
            frm.set_value("naming_series", frm.doc.custom_business_type)
        }
    }
})
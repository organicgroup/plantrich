frappe.ui.form.on("Lead", {
    before_save:function(frm){
        let total_amount = 0
        frm.doc.custom_item.forEach(row=>{
            if(!row.amount){
                row.amount = row.qty * row.rate
            }
            total_amount += row.amount 
        })
        frm.set_value("custom_total_amount", total_amount)
    }
})

frappe.ui.form.on('Lead Item', {
    item_code:function(frm, cdt, cdn){
        let row = locals[cdt][cdn]
        row.qty = 1
        row.amount = row.qty * row.rate
        frm.refresh_field("custom_item")
        if(row.rate == 0){
            frappe.db.get_value("Item Price", {"item_code": row.item_code, "price_list": "Standard Selling", "selling":1}, ["price_list_rate"]).then(data=>{
                if(data.message.price_list_rate){
                    row.rate = data.message.price_list_rate
                    row.amount = data.message.price_list_rate * row.qty
                    frm.refresh_field("custom_item")
                }
            })
        }
        
    },
    qty:function(frm, cdt, cdn){
        let row = locals[cdt][cdn]
        if(row.qty){
            row.amount = row.qty * row.rate
        }
        frm.refresh_field("custom_item")
    },
    rate:function(frm, cdt, cdn){
        let row = locals[cdt][cdn]
        if(row.rate){
            row.amount = row.qty * row.rate
        }
        frm.refresh_field("custom_item")
    }
})
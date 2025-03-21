// Copyright (c) 2024, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Factory Audit Checklist', {
	// refresh: function(frm) {

	// }
	

	onload: function(frm) {

		cur_frm.get_field("q1").grid.cannot_add_rows = true;
		refresh_field("q1");
		cur_frm.get_field("q2").grid.cannot_add_rows = true;
		refresh_field("q2");
		cur_frm.get_field("q3").grid.cannot_add_rows = true;
		refresh_field("q3");
		cur_frm.get_field("q4").grid.cannot_add_rows = true;
		refresh_field("q4");
		cur_frm.get_field("q5").grid.cannot_add_rows = true;
		refresh_field("q5");
		cur_frm.get_field("q6").grid.cannot_add_rows = true;
		refresh_field("q6");
		cur_frm.get_field("q7").grid.cannot_add_rows = true;
		refresh_field("q7");
		cur_frm.get_field("q8").grid.cannot_add_rows = true;
		refresh_field("q8");
		cur_frm.get_field("q9").grid.cannot_add_rows = true;
		refresh_field("q9");
		cur_frm.get_field("q10").grid.cannot_add_rows = true;
		refresh_field("q10");
		cur_frm.get_field("q11").grid.cannot_add_rows = true;
		refresh_field("q11");
		cur_frm.get_field("q12").grid.cannot_add_rows = true;
		refresh_field("q12");
		cur_frm.get_field("q13").grid.cannot_add_rows = true;
		refresh_field("q13");
		cur_frm.get_field("q14").grid.cannot_add_rows = true;
		refresh_field("q14");
		cur_frm.get_field("q15").grid.cannot_add_rows = true;
		refresh_field("q15");
		cur_frm.get_field("q16").grid.cannot_add_rows = true;
		refresh_field("q16");
		cur_frm.get_field("q17").grid.cannot_add_rows = true;
		refresh_field("q17");
		cur_frm.get_field("q17").grid.cannot_add_rows = true;
		refresh_field("q17");
		cur_frm.get_field("q18").grid.cannot_add_rows = true;
		refresh_field("q18");
		cur_frm.get_field("q19").grid.cannot_add_rows = true;
		refresh_field("q19");
		cur_frm.get_field("q20").grid.cannot_add_rows = true;
		refresh_field("q20");
		cur_frm.get_field("q21").grid.cannot_add_rows = true;
		refresh_field("q21");
		cur_frm.get_field("q22").grid.cannot_add_rows = true;
		refresh_field("q22");
		cur_frm.get_field("q23").grid.cannot_add_rows = true;
		refresh_field("q23");
		cur_frm.get_field("q24").grid.cannot_add_rows = true;
		refresh_field("q24");
		cur_frm.get_field("q25").grid.cannot_add_rows = true;
		refresh_field("q26");
		cur_frm.get_field("q27").grid.cannot_add_rows = true;
		refresh_field("q27");
		cur_frm.get_field("q28").grid.cannot_add_rows = true;
		refresh_field("q28");
		cur_frm.get_field("q29").grid.cannot_add_rows = true;
		refresh_field("q29");
		cur_frm.get_field("q30").grid.cannot_add_rows = true;
		refresh_field("q30");
		cur_frm.get_field("q31").grid.cannot_add_rows = true;
		refresh_field("q31");
		cur_frm.get_field("q32").grid.cannot_add_rows = true;
		refresh_field("q32");
		cur_frm.get_field("q33").grid.cannot_add_rows = true;
		refresh_field("q33");
		cur_frm.get_field("q34").grid.cannot_add_rows = true;
		refresh_field("q34");
		cur_frm.get_field("q35").grid.cannot_add_rows = true;
		refresh_field("q35");
		cur_frm.get_field("q36").grid.cannot_add_rows = true;
		refresh_field("q36");
		cur_frm.get_field("q37").grid.cannot_add_rows = true;
		refresh_field("q37");
		cur_frm.get_field("q38").grid.cannot_add_rows = true;
		refresh_field("q38");
		cur_frm.get_field("q39").grid.cannot_add_rows = true;
		refresh_field("q39");
		cur_frm.get_field("q40").grid.cannot_add_rows = true;
		refresh_field("q40");
		cur_frm.get_field("q41").grid.cannot_add_rows = true;
		refresh_field("q41");
		cur_frm.get_field("q42").grid.cannot_add_rows = true;
		refresh_field("q42");
		cur_frm.get_field("q43").grid.cannot_add_rows = true;
		refresh_field("q43");
		cur_frm.get_field("q44").grid.cannot_add_rows = true;
		refresh_field("q44");
		cur_frm.get_field("q45").grid.cannot_add_rows = true;
		refresh_field("q45");
		cur_frm.get_field("q46").grid.cannot_add_rows = true;
		refresh_field("q46");
		cur_frm.get_field("q47").grid.cannot_add_rows = true;
		refresh_field("q47");
		cur_frm.get_field("q48").grid.cannot_add_rows = true;
		refresh_field("q48");

		cur_frm.get_field("q50").grid.cannot_add_rows = true;
		refresh_field("q50");
		cur_frm.get_field("q51").grid.cannot_add_rows = true;
		refresh_field("q51");
		cur_frm.get_field("q52").grid.cannot_add_rows = true;
		refresh_field("q52");
		cur_frm.get_field("q53").grid.cannot_add_rows = true;
		refresh_field("q53");
		cur_frm.get_field("q54").grid.cannot_add_rows = true;
		refresh_field("q54");
		cur_frm.get_field("q55").grid.cannot_add_rows = true;
		refresh_field("q55");
		cur_frm.get_field("q56").grid.cannot_add_rows = true;
		refresh_field("q56");
		cur_frm.get_field("q57").grid.cannot_add_rows = true;
		refresh_field("q57");
		cur_frm.get_field("q58").grid.cannot_add_rows = true;
		refresh_field("q58");
		cur_frm.get_field("q59").grid.cannot_add_rows = true;
		refresh_field("q59");
		cur_frm.get_field("q60").grid.cannot_add_rows = true;
		refresh_field("q60");


		

	},
	fetch_questions:function(cur_frm){
		cur_frm.call({
			doc:cur_frm.doc,
			method:'get_performa',
			args:{},
			callback:function(a){
				console.log("test java ")
				console.log(a);
			}
	});
	
	}
});

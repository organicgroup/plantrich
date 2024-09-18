# Copyright (c) 2024, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FactoryAuditChecklist(Document):
	@frappe.whitelist()
	def get_performa(self):

		
		c = frappe.db.sql("""select * from `tabStacking` order by idx """,as_dict=1)

		
		if c:
			for idx,i in enumerate(c, start=1):
				self.append("q1", {
					'questions': i.questions,
					'idx':idx
				
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		d = frappe.db.sql("""select * from `tabStock Management` order by idx """,as_dict=1)

		
		if d:
			for idx,i in enumerate(d, start=1):
				self.append("q2", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////			

		e = frappe.db.sql("""select * from `tabLabeling` order by idx """,as_dict=1)

		
		if e:
			for idx,i in enumerate(e, start=1):
				self.append("q3", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		f = frappe.db.sql("""select * from `tabAwareness of Workers` order by idx """,as_dict=1)

		
		if f:
			for idx,i in enumerate(f, start=1):
				self.append("q4", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		g = frappe.db.sql("""select * from `tabAwareness of Organic Standards` order by idx """,as_dict=1)

		
		if g:
			for idx,i in enumerate(g, start=1):
				self.append("q5", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////	

		k = frappe.db.sql("""select * from `tabAwareness of Fairtrade Standards` order by idx """,as_dict=1)

		
		if k:
			for idx,i in enumerate(k, start=1):
				self.append("q6", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		j = frappe.db.sql("""select * from `tabAwareness of RFA Standards` order by idx """,as_dict=1)

		
		if j:
			for idx,i in enumerate(j, start=1):
				self.append("q7", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		l = frappe.db.sql("""select * from `tabPersonal Hygiene` order by idx """,as_dict=1)

		
		if l:
			for idx, i in enumerate(l, start=1):
				self.append("q8", {
					'questions': i.questions,
					'idx': idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////
				

		


		m = frappe.db.sql("""select * from `tabMigrant Workers Contract` order by idx""", as_dict=1)

		if m:
			for idx, i in enumerate(m, start=1):
				self.append("q9", {
					'questions': i.questions,
					'idx': idx
				})





# /////////////////////////////////////////////////////////////////////////////////////////////

		n = frappe.db.sql("""select * from `tabEntry Exit System` order by idx """,as_dict=1)

		
		if n:
			for idx,i in enumerate(n, start=1):
				self.append("q10", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		o = frappe.db.sql("""select * from `tabDocumentation in ERP` order by idx """,as_dict=1)

		
		if o:
			for idx,i in enumerate(o, start=1):
				self.append("q11", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		p = frappe.db.sql("""select * from `tabMachinery` order by idx """,as_dict=1)

		
		if p:
			for idx,i in enumerate(p, start=1):
				self.append("q12", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		q = frappe.db.sql("""select * from `tabMaintenance System` order by idx """,as_dict=1)

		
		if q:
			for idx,i in enumerate(q, start=1):
				self.append("q13", {
					'questions': i.questions,
					'idx':idx
				}) 
			
# /////////////////////////////////////////////////////////////////////////////////////////////				

		r = frappe.db.sql("""select * from `tabNon Conformities` order by idx """,as_dict=1)

		
		if r:
			for idx,i in enumerate(r, start=1):
				self.append("q14", {
					'questions': i.questions,
					'idx':idx
				}) 		

# /////////////////////////////////////////////////////////////////////////////////////////////				

		s = frappe.db.sql("""select * from `tabStacking of Used Bags` order by idx """,as_dict=1)

		
		if s:
			for idx,i in enumerate(s, start=1):
				self.append("q15", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		t = frappe.db.sql("""select * from `tabLab Maintenance` order by idx """,as_dict=1)

		
		if t:
			for idx,i in enumerate(t, start=1):
				self.append("q16", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		u = frappe.db.sql("""select * from `tabAccident SOP` order by idx """,as_dict=1)

		
		if u:
			for idx,i in enumerate(u, start=1):
				self.append("q17", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		v = frappe.db.sql("""select * from `tabTheft SOP` order by idx """,as_dict=1)

		
		if v:
			for idx,i in enumerate(v, start=1):
				self.append("q18", {
					'questions': i.questions,
					'idx':idx
				}) 								
# /////////////////////////////////////////////////////////////////////////////////////////////				

		w = frappe.db.sql("""select * from `tabFire SOP` order by idx """,as_dict=1)

		
		if w:
			for idx,i in enumerate(w, start=1):
				self.append("q19", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		x = frappe.db.sql("""select * from `tabPest Control Plan` order by idx """,as_dict=1)

		
		if x:
			for idx,i in enumerate(x, start=1):
				self.append("q20", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		y = frappe.db.sql("""select * from `tabExternal Pest Control Services` order by idx """,as_dict=1)

		
		if y:
			for idx,i in enumerate(y, start=1):
				self.append("q21", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		z = frappe.db.sql("""select * from `tabRodent Proofing` order by idx """,as_dict=1)

		
		if z:
			for idx,i in enumerate(z, start=1):
				self.append("q22", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		aa = frappe.db.sql("""select * from `tabRegular Monitoring` order by idx """,as_dict=1)

		
		if aa:
			for idx,i in enumerate(aa, start=1):
				self.append("q23", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		bb = frappe.db.sql("""select * from `tabCleaning  Sanitation` order by idx """,as_dict=1)

		
		if bb:
			for idx,i in enumerate(bb, start=1):
				self.append("q24", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		cc = frappe.db.sql("""select * from `tabChemical Control Methods` order by idx """,as_dict=1)

		
		if cc:
			for idx,i in enumerate(cc, start=1):
				self.append("q25", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		dd = frappe.db.sql("""select * from `tabNon Chemical Control Methods` order by idx """,as_dict=1)

		
		if dd:
			for idx,i in enumerate(dd, start=1):
				self.append("q26", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		ee = frappe.db.sql("""select * from `tabEmployee Training` order by idx """,as_dict=1)

		
		if ee:
			for idx,i in enumerate(ee, start=1):
				self.append("q27", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		ff = frappe.db.sql("""select * from `tabCompliance with Standards` order by idx """,as_dict=1)

		
		if ff:
			for idx,i in enumerate(ff, start=1):
				self.append("q28", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		gg = frappe.db.sql("""select * from `tabPest Control Equipment Maintenance` order by idx """,as_dict=1)

		
		if gg:
			for idx,i in enumerate(gg, start=1):
				self.append("q29", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		hh = frappe.db.sql("""select * from `tabResponse to Infestations` order by idx """,as_dict=1)

		
		if hh:
			for idx,i in enumerate(hh, start=1):
				self.append("q30", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		ii = frappe.db.sql("""select * from `tabStorage of Food Products` order by idx """,as_dict=1)

		
		if ii:
			for idx,i in enumerate(ii, start=1):
				self.append("q31", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		jj = frappe.db.sql("""select * from `tabInspection of Water Systems` order by idx """,as_dict=1)

		
		if jj:
			for idx,i in enumerate(jj, start=1):
				self.append("q32", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		kk = frappe.db.sql("""select * from `tabLeak Detection System` order by idx """,as_dict=1)

		
		if kk:
			for idx,i in enumerate(kk, start=1):
				self.append("q33", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		ll = frappe.db.sql("""select * from `tabPlumbing and Drainage Maintenance` order by idx """,as_dict=1)

		
		if ll:
			for idx,i in enumerate(ll, start=1):
				self.append("q34", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		mm = frappe.db.sql("""select * from `tabWater Metering` order by idx """,as_dict=1)

		
		if mm:
			for idx,i in enumerate(mm, start=1):
				self.append("q35", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		nn = frappe.db.sql("""select * from `tabImmediate Action Protocol` order by idx """,as_dict=1)

		
		if nn:
			for idx,i in enumerate(nn, start=1):
				self.append("q36", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		oo = frappe.db.sql("""select * from `tabPreventive Maintenance` order by idx """,as_dict=1)

		
		if oo:
			for idx,i in enumerate(oo, start=1):
				self.append("q37", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		pp = frappe.db.sql("""select * from `tabTask Assignment and Monitoring` order by idx """,as_dict=1)

		
		if pp:
			for idx,i in enumerate(pp, start=1):
				self.append("q38", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		qq = frappe.db.sql("""select * from `tabDaily Output Measurement` order by idx """,as_dict=1)

		
		if qq:
			for idx,i in enumerate(qq, start=1):
				self.append("q39", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		rr = frappe.db.sql("""select * from `tabUse of Technology` order by idx """,as_dict=1)

		
		if rr:
			for idx,i in enumerate(rr, start=1):
				self.append("q40", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		ss = frappe.db.sql("""select * from `tabPerformance KPIs` order by idx """,as_dict=1)

		
		if ss:
			for idx,i in enumerate(ss, start=1):
				self.append("q41", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		tt = frappe.db.sql("""select * from `tabTraining and Skill Development` order by idx """,as_dict=1)

		
		if tt:
			for idx,i in enumerate(tt, start=1):
				self.append("q42", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		uu = frappe.db.sql("""select * from `tabIncentives and Motivation` order by idx """,as_dict=1)

		
		if uu:
			for idx,i in enumerate(uu, start=1):
				self.append("q43", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		vv = frappe.db.sql("""select * from `tabError and Downtime Tracking` order by idx """,as_dict=1)

		
		if vv:
			for idx,i in enumerate(vv, start=1):
				self.append("q44", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		ww = frappe.db.sql("""select * from `tabWorkload Distribution` order by idx """,as_dict=1)

		
		if ww:
			for idx,i in enumerate(ww, start=1):
				self.append("q45", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		xx = frappe.db.sql("""select * from `tabFeedback Collection System` order by idx """,as_dict=1)

		
		if xx:
			for idx,i in enumerate(xx, start=1):
				self.append("q46", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		yy = frappe.db.sql("""select * from `tabRegular Feedback Sessions` order by idx """,as_dict=1)

		
		if yy:
			for idx,i in enumerate(yy, start=1):
				self.append("q47", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)

		
		if zz:
			for idx,i in enumerate(zz, start=1):
				self.append("q48", {
					'questions': i.questions,
					'idx':idx
				})

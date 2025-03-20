# Copyright (c) 2024, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import cint

class FactoryAuditChecklist(Document):
	@frappe.whitelist()
	def get_performa(self):

		
		c = frappe.db.sql("""
		SELECT stacking.*, audit_questions.*
		FROM `tabStacking` stacking
		JOIN `tabAudit Questions` audit_questions
		ON stacking.parent = audit_questions.name
		ORDER BY stacking.idx
	""", as_dict=1)


		
		if c:
			for idx,i in enumerate(c, start=1):
				self.append("q1", {
					'questions': i.questions,
					'idx':idx
				
				})

# /////////////////////////////////////////////////////////////////////////////////////////////
		d = frappe.db.sql("""
		SELECT stock.*, audit_questions.*
		FROM `tabStock Management` stock
		JOIN `tabAudit Questions` audit_questions
		ON stock.parent = audit_questions.name
		ORDER BY stock.idx
	""", as_dict=1)
		
		# d = frappe.db.sql("""select * from `tabStock Management` order by idx """,as_dict=1)

		
		if d:
			for idx,i in enumerate(d, start=1):
				self.append("q2", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////		
		e = frappe.db.sql("""
		SELECT label.*, audit_questions.*
		FROM `tabLabeling` label
		JOIN `tabAudit Questions` audit_questions
		ON label.parent = audit_questions.name
		ORDER BY label.idx
		""", as_dict=1)	

		# e = frappe.db.sql("""select * from `tabLabeling` order by idx """,as_dict=1)

		
		if e:
			for idx,i in enumerate(e, start=1):
				self.append("q3", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		# f = frappe.db.sql("""select * from `tabAwareness of Workers` order by idx """,as_dict=1)
		f = frappe.db.sql("""
		SELECT awareness_of_workers.*, audit_questions.*
		FROM `tabAwareness of Workers` awareness_of_workers
		JOIN `tabAudit Questions` audit_questions
		ON awareness_of_workers.parent = audit_questions.name
		ORDER BY awareness_of_workers.idx
		""", as_dict=1)	
		
		if f:
			for idx,i in enumerate(f, start=1):
				self.append("q4", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		# g = frappe.db.sql("""select * from `tabAwareness of Organic Standards` order by idx """,as_dict=1)
		g = frappe.db.sql("""
		SELECT awareness_of_organic_standards.*, audit_questions.*
		FROM `tabAwareness of Organic Standards` awareness_of_organic_standards
		JOIN `tabAudit Questions` audit_questions
		ON awareness_of_organic_standards.parent = audit_questions.name
		ORDER BY awareness_of_organic_standards.idx
		""", as_dict=1)
		
		if g:
			for idx,i in enumerate(g, start=1):
				self.append("q5", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////	

		# k = frappe.db.sql("""select * from `tabAwareness of Fairtrade Standards` order by idx """,as_dict=1)
		k = frappe.db.sql("""
		SELECT awareness_of_fairtrade_standards.*, audit_questions.*
		FROM `tabAwareness of Fairtrade Standards` awareness_of_fairtrade_standards
		JOIN `tabAudit Questions` audit_questions
		ON awareness_of_fairtrade_standards.parent = audit_questions.name
		ORDER BY awareness_of_fairtrade_standards.idx
		""", as_dict=1)
		
		if k:
			for idx,i in enumerate(k, start=1):
				self.append("q6", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# j = frappe.db.sql("""select * from `tabAwareness of RFA Standards` order by idx """,as_dict=1)
		j = frappe.db.sql("""
		SELECT awareness_of_rfa_standards.*, audit_questions.*
		FROM `tabAwareness of RFA Standards` awareness_of_rfa_standards
		JOIN `tabAudit Questions` audit_questions
		ON awareness_of_rfa_standards.parent = audit_questions.name
		ORDER BY awareness_of_rfa_standards.idx
		""", as_dict=1)
		
		if j:
			for idx,i in enumerate(j, start=1):
				self.append("q7", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# l = frappe.db.sql("""select * from `tabPersonal Hygiene` order by idx """,as_dict=1)
		l = frappe.db.sql("""
		SELECT personal_hygiene.*, audit_questions.*
		FROM `tabPersonal Hygiene` personal_hygiene
		JOIN `tabAudit Questions` audit_questions
		ON personal_hygiene.parent = audit_questions.name
		ORDER BY personal_hygiene.idx
		""", as_dict=1)
		
		if l:
			for idx, i in enumerate(l, start=1):
				self.append("q8", {
					'questions': i.questions,
					'idx': idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////
				

		


		# m = frappe.db.sql("""select * from `tabMigrant Workers Contract` order by idx""", as_dict=1)
		m = frappe.db.sql("""
		SELECT migrant_workers_contract.*, audit_questions.*
		FROM `tabMigrant Workers Contract` migrant_workers_contract
		JOIN `tabAudit Questions` audit_questions
		ON migrant_workers_contract.parent = audit_questions.name
		ORDER BY migrant_workers_contract.idx
		""", as_dict=1)
		if m:
			for idx, i in enumerate(m, start=1):
				self.append("q9", {
					'questions': i.questions,
					'idx': idx
				})





# /////////////////////////////////////////////////////////////////////////////////////////////

		# n = frappe.db.sql("""select * from `tabEntry Exit System` order by idx """,as_dict=1)
		n = frappe.db.sql("""
		SELECT entry_exit_system.*, audit_questions.*
		FROM `tabEntry Exit System` entry_exit_system
		JOIN `tabAudit Questions` audit_questions
		ON entry_exit_system.parent = audit_questions.name
		ORDER BY entry_exit_system.idx
		""", as_dict=1)
		
		if n:
			for idx,i in enumerate(n, start=1):
				self.append("q10", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		# o = frappe.db.sql("""select * from `tabDocumentation in ERP` order by idx """,as_dict=1)
		o = frappe.db.sql("""
		SELECT documentation_in_erp.*, audit_questions.*
		FROM `tabDocumentation in ERP` documentation_in_erp
		JOIN `tabAudit Questions` audit_questions
		ON documentation_in_erp.parent = audit_questions.name
		ORDER BY documentation_in_erp.idx
		""", as_dict=1)
		
		if o:
			for idx,i in enumerate(o, start=1):
				self.append("q11", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# p = frappe.db.sql("""select * from `tabMachinery` order by idx """,as_dict=1)
		p = frappe.db.sql("""
		SELECT machinery.*, audit_questions.*
		FROM `tabMachinery` machinery
		JOIN `tabAudit Questions` audit_questions
		ON machinery.parent = audit_questions.name
		ORDER BY machinery.idx
		""", as_dict=1)
		
		if p:
			for idx,i in enumerate(p, start=1):
				self.append("q12", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# q = frappe.db.sql("""select * from `tabMaintenance System` order by idx """,as_dict=1)
		q = frappe.db.sql("""
		SELECT maintenance_system.*, audit_questions.*
		FROM `tabMaintenance System` maintenance_system
		JOIN `tabAudit Questions` audit_questions
		ON maintenance_system.parent = audit_questions.name
		ORDER BY maintenance_system.idx
		""", as_dict=1)
		
		if q:
			for idx,i in enumerate(q, start=1):
				self.append("q13", {
					'questions': i.questions,
					'idx':idx
				}) 
			
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# r = frappe.db.sql("""select * from `tabNon Conformities` order by idx """,as_dict=1)
		r = frappe.db.sql("""
		SELECT non_conformities.*, audit_questions.*
		FROM `tabNon Conformities` non_conformities
		JOIN `tabAudit Questions` audit_questions
		ON non_conformities.parent = audit_questions.name
		ORDER BY non_conformities.idx
		""", as_dict=1)
		
		if r:
			for idx,i in enumerate(r, start=1):
				self.append("q14", {
					'questions': i.questions,
					'idx':idx
				}) 		

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# s = frappe.db.sql("""select * from `tabStacking of Used Bags` order by idx """,as_dict=1)
		s = frappe.db.sql("""
		SELECT stacking_of_used_bags.*, audit_questions.*
		FROM `tabStacking of Used Bags` stacking_of_used_bags
		JOIN `tabAudit Questions` audit_questions
		ON stacking_of_used_bags.parent = audit_questions.name
		ORDER BY stacking_of_used_bags.idx
		""", as_dict=1)
		
		if s:
			for idx,i in enumerate(s, start=1):
				self.append("q15", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# t = frappe.db.sql("""select * from `tabLab Maintenance` order by idx """,as_dict=1)
		t = frappe.db.sql("""
		SELECT lab_maintenance.*, audit_questions.*
		FROM `tabLab Maintenance` lab_maintenance
		JOIN `tabAudit Questions` audit_questions
		ON lab_maintenance.parent = audit_questions.name
		ORDER BY lab_maintenance.idx
		""", as_dict=1)
		
		if t:
			for idx,i in enumerate(t, start=1):
				self.append("q16", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# u = frappe.db.sql("""select * from `tabAccident SOP` order by idx """,as_dict=1)
		u = frappe.db.sql("""
		SELECT accident_sop.*, audit_questions.*
		FROM `tabAccident SOP` accident_sop
		JOIN `tabAudit Questions` audit_questions
		ON accident_sop.parent = audit_questions.name
		ORDER BY accident_sop.idx
		""", as_dict=1)
		
		if u:
			for idx,i in enumerate(u, start=1):
				self.append("q17", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# v = frappe.db.sql("""select * from `tabTheft SOP` order by idx """,as_dict=1)
		v = frappe.db.sql("""
		SELECT theft_sop.*, audit_questions.*
		FROM `tabTheft SOP` theft_sop
		JOIN `tabAudit Questions` audit_questions
		ON theft_sop.parent = audit_questions.name
		ORDER BY theft_sop.idx
		""", as_dict=1)
		
		if v:
			for idx,i in enumerate(v, start=1):
				self.append("q18", {
					'questions': i.questions,
					'idx':idx
				}) 								
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# w = frappe.db.sql("""select * from `tabFire SOP` order by idx """,as_dict=1)
		w = frappe.db.sql("""
		SELECT fire_sop.*, audit_questions.*
		FROM `tabFire SOP` fire_sop
		JOIN `tabAudit Questions` audit_questions
		ON fire_sop.parent = audit_questions.name
		ORDER BY fire_sop.idx
		""", as_dict=1)
		
		if w:
			for idx,i in enumerate(w, start=1):
				self.append("q19", {
					'questions': i.questions,
					'idx':idx
				}) 
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# x = frappe.db.sql("""select * from `tabPest Control Plan` order by idx """,as_dict=1)
		x = frappe.db.sql("""
		SELECT pest_control_plan.*, audit_questions.*
		FROM `tabPest Control Plan` pest_control_plan
		JOIN `tabAudit Questions` audit_questions
		ON pest_control_plan.parent = audit_questions.name
		ORDER BY pest_control_plan.idx
		""", as_dict=1)
		
		if x:
			for idx,i in enumerate(x, start=1):
				self.append("q20", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# y = frappe.db.sql("""select * from `tabExternal Pest Control Services` order by idx """,as_dict=1)
		y = frappe.db.sql("""
		SELECT external_pest_control_services.*, audit_questions.*
		FROM `tabExternal Pest Control Services` external_pest_control_services
		JOIN `tabAudit Questions` audit_questions
		ON external_pest_control_services.parent = audit_questions.name
		ORDER BY external_pest_control_services.idx
		""", as_dict=1)
		
		if y:
			for idx,i in enumerate(y, start=1):
				self.append("q21", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# z = frappe.db.sql("""select * from `tabRodent Proofing` order by idx """,as_dict=1)
		z = frappe.db.sql("""
		SELECT rodent_proofing.*, audit_questions.*
		FROM `tabRodent Proofing` rodent_proofing
		JOIN `tabAudit Questions` audit_questions
		ON rodent_proofing.parent = audit_questions.name
		ORDER BY rodent_proofing.idx
		""", as_dict=1)
		
		if z:
			for idx,i in enumerate(z, start=1):
				self.append("q22", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# aa = frappe.db.sql("""select * from `tabRegular Monitoring` order by idx """,as_dict=1)
		aa = frappe.db.sql("""
		SELECT regular_monitoring.*, audit_questions.*
		FROM `tabRegular Monitoring` regular_monitoring
		JOIN `tabAudit Questions` audit_questions
		ON regular_monitoring.parent = audit_questions.name
		ORDER BY regular_monitoring.idx
		""", as_dict=1)
		
		if aa:
			for idx,i in enumerate(aa, start=1):
				self.append("q23", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# bb = frappe.db.sql("""select * from `tabCleaning  Sanitation` order by idx """,as_dict=1)
		bb = frappe.db.sql("""
		SELECT cleaning__sanitation.*, audit_questions.*
		FROM `tabCleaning  Sanitation` cleaning__sanitation
		JOIN `tabAudit Questions` audit_questions
		ON cleaning__sanitation.parent = audit_questions.name
		ORDER BY cleaning__sanitation.idx
		""", as_dict=1)
		
		if bb:
			for idx,i in enumerate(bb, start=1):
				self.append("q24", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# cc = frappe.db.sql("""select * from `tabChemical Control Methods` order by idx """,as_dict=1)
		cc = frappe.db.sql("""
		SELECT chemical_control_methods.*, audit_questions.*
		FROM `tabChemical Control Methods` chemical_control_methods
		JOIN `tabAudit Questions` audit_questions
		ON chemical_control_methods.parent = audit_questions.name
		ORDER BY chemical_control_methods.idx
		""", as_dict=1)
		
		if cc:
			for idx,i in enumerate(cc, start=1):
				self.append("q25", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# dd = frappe.db.sql("""select * from `tabNon Chemical Control Methods` order by idx """,as_dict=1)
		dd = frappe.db.sql("""
		SELECT non_chemical_control_methods.*, audit_questions.*
		FROM `tabNon Chemical Control Methods` non_chemical_control_methods
		JOIN `tabAudit Questions` audit_questions
		ON non_chemical_control_methods.parent = audit_questions.name
		ORDER BY non_chemical_control_methods.idx
		""", as_dict=1)
		
		if dd:
			for idx,i in enumerate(dd, start=1):
				self.append("q26", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# ee = frappe.db.sql("""select * from `tabEmployee Training` order by idx """,as_dict=1)
		ee = frappe.db.sql("""
		SELECT employee_training.*, audit_questions.*
		FROM `tabEmployee Training` employee_training
		JOIN `tabAudit Questions` audit_questions
		ON employee_training.parent = audit_questions.name
		ORDER BY employee_training.idx
		""", as_dict=1)
		
		if ee:
			for idx,i in enumerate(ee, start=1):
				self.append("q27", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# ff = frappe.db.sql("""select * from `tabCompliance with Standards` order by idx """,as_dict=1)
		ff = frappe.db.sql("""
		SELECT compliance_with_standards.*, audit_questions.*
		FROM `tabCompliance with Standards` compliance_with_standards
		JOIN `tabAudit Questions` audit_questions
		ON compliance_with_standards.parent = audit_questions.name
		ORDER BY compliance_with_standards.idx
		""", as_dict=1)
		
		if ff:
			for idx,i in enumerate(ff, start=1):
				self.append("q28", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# gg = frappe.db.sql("""select * from `tabPest Control Equipment Maintenance` order by idx """,as_dict=1)
		gg = frappe.db.sql("""
		SELECT pest_control_equipment_maintenance.*, audit_questions.*
		FROM `tabPest Control Equipment Maintenance` pest_control_equipment_maintenance
		JOIN `tabAudit Questions` audit_questions
		ON pest_control_equipment_maintenance.parent = audit_questions.name
		ORDER BY pest_control_equipment_maintenance.idx
		""", as_dict=1)
		
		if gg:
			for idx,i in enumerate(gg, start=1):
				self.append("q29", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# hh = frappe.db.sql("""select * from `tabResponse to Infestations` order by idx """,as_dict=1)
		hh = frappe.db.sql("""
		SELECT response_to_infestations.*, audit_questions.*
		FROM `tabResponse to Infestations` response_to_infestations
		JOIN `tabAudit Questions` audit_questions
		ON response_to_infestations.parent = audit_questions.name
		ORDER BY response_to_infestations.idx
		""", as_dict=1)
		
		if hh:
			for idx,i in enumerate(hh, start=1):
				self.append("q30", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# ii = frappe.db.sql("""select * from `tabStorage of Food Products` order by idx """,as_dict=1)
		ii = frappe.db.sql("""
		SELECT storage_of_food_products.*, audit_questions.*
		FROM `tabStorage of Food Products` storage_of_food_products
		JOIN `tabAudit Questions` audit_questions
		ON storage_of_food_products.parent = audit_questions.name
		ORDER BY storage_of_food_products.idx
		""", as_dict=1)
		
		if ii:
			for idx,i in enumerate(ii, start=1):
				self.append("q31", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# jj = frappe.db.sql("""select * from `tabInspection of Water Systems` order by idx """,as_dict=1)
		jj = frappe.db.sql("""
		SELECT inspection_of_water_systems.*, audit_questions.*
		FROM `tabInspection of Water Systems` inspection_of_water_systems
		JOIN `tabAudit Questions` audit_questions
		ON inspection_of_water_systems.parent = audit_questions.name
		ORDER BY inspection_of_water_systems.idx
		""", as_dict=1)
		
		if jj:
			for idx,i in enumerate(jj, start=1):
				self.append("q32", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# kk = frappe.db.sql("""select * from `tabLeak Detection System` order by idx """,as_dict=1)
		kk = frappe.db.sql("""
		SELECT leak_detection_system.*, audit_questions.*
		FROM `tabLeak Detection System` leak_detection_system
		JOIN `tabAudit Questions` audit_questions
		ON leak_detection_system.parent = audit_questions.name
		ORDER BY leak_detection_system.idx
		""", as_dict=1)
		
		if kk:
			for idx,i in enumerate(kk, start=1):
				self.append("q33", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# ll = frappe.db.sql("""select * from `tabPlumbing and Drainage Maintenance` order by idx """,as_dict=1)
		ll = frappe.db.sql("""
		SELECT plumbing_and_drainage_maintenance.*, audit_questions.*
		FROM `tabPlumbing and Drainage Maintenance` plumbing_and_drainage_maintenance
		JOIN `tabAudit Questions` audit_questions
		ON plumbing_and_drainage_maintenance.parent = audit_questions.name
		ORDER BY plumbing_and_drainage_maintenance.idx
		""", as_dict=1)
		
		if ll:
			for idx,i in enumerate(ll, start=1):
				self.append("q34", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# mm = frappe.db.sql("""select * from `tabWater Metering` order by idx """,as_dict=1)
		mm = frappe.db.sql("""
		SELECT water_metering.*, audit_questions.*
		FROM `tabWater Metering` water_metering
		JOIN `tabAudit Questions` audit_questions
		ON water_metering.parent = audit_questions.name
		ORDER BY water_metering.idx
		""", as_dict=1)
		
		if mm:
			for idx,i in enumerate(mm, start=1):
				self.append("q35", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# nn = frappe.db.sql("""select * from `tabImmediate Action Protocol` order by idx """,as_dict=1)
		nn = frappe.db.sql("""
		SELECT immediate_action_protocol.*, audit_questions.*
		FROM `tabImmediate Action Protocol` immediate_action_protocol
		JOIN `tabAudit Questions` audit_questions
		ON immediate_action_protocol.parent = audit_questions.name
		ORDER BY immediate_action_protocol.idx
		""", as_dict=1)
		
		if nn:
			for idx,i in enumerate(nn, start=1):
				self.append("q36", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# oo = frappe.db.sql("""select * from `tabPreventive Maintenance` order by idx """,as_dict=1)
		oo = frappe.db.sql("""
		SELECT preventive_maintenance.*, audit_questions.*
		FROM `tabPreventive Maintenance` preventive_maintenance
		JOIN `tabAudit Questions` audit_questions
		ON preventive_maintenance.parent = audit_questions.name
		ORDER BY preventive_maintenance.idx
		""", as_dict=1)
		
		if oo:
			for idx,i in enumerate(oo, start=1):
				self.append("q37", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# pp = frappe.db.sql("""select * from `tabTask Assignment and Monitoring` order by idx """,as_dict=1)
		pp = frappe.db.sql("""
		SELECT task_assignment_and_monitoring.*, audit_questions.*
		FROM `tabTask Assignment and Monitoring` task_assignment_and_monitoring
		JOIN `tabAudit Questions` audit_questions
		ON task_assignment_and_monitoring.parent = audit_questions.name
		ORDER BY task_assignment_and_monitoring.idx
		""", as_dict=1)
		
		if pp:
			for idx,i in enumerate(pp, start=1):
				self.append("q38", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# qq = frappe.db.sql("""select * from `tabDaily Output Measurement` order by idx """,as_dict=1)
		qq = frappe.db.sql("""
		SELECT daily_output_measurement.*, audit_questions.*
		FROM `tabDaily Output Measurement` daily_output_measurement
		JOIN `tabAudit Questions` audit_questions
		ON daily_output_measurement.parent = audit_questions.name
		ORDER BY daily_output_measurement.idx
		""", as_dict=1)
		
		if qq:
			for idx,i in enumerate(qq, start=1):
				self.append("q39", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# rr = frappe.db.sql("""select * from `tabUse of Technology` order by idx """,as_dict=1)
		rr = frappe.db.sql("""
		SELECT use_of_technology.*, audit_questions.*
		FROM `tabUse of Technology` use_of_technology
		JOIN `tabAudit Questions` audit_questions
		ON use_of_technology.parent = audit_questions.name
		ORDER BY use_of_technology.idx
		""", as_dict=1)
		
		if rr:
			for idx,i in enumerate(rr, start=1):
				self.append("q40", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# ss = frappe.db.sql("""select * from `tabPerformance KPIs` order by idx """,as_dict=1)
		ss = frappe.db.sql("""
		SELECT performance_kpis.*, audit_questions.*
		FROM `tabPerformance KPIs` performance_kpis
		JOIN `tabAudit Questions` audit_questions
		ON performance_kpis.parent = audit_questions.name
		ORDER BY performance_kpis.idx
		""", as_dict=1)
		
		if ss:
			for idx,i in enumerate(ss, start=1):
				self.append("q41", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# tt = frappe.db.sql("""select * from `tabTraining and Skill Development` order by idx """,as_dict=1)
		tt = frappe.db.sql("""
		SELECT training_and_skill_development.*, audit_questions.*
		FROM `tabTraining and Skill Development` training_and_skill_development
		JOIN `tabAudit Questions` audit_questions
		ON training_and_skill_development.parent = audit_questions.name
		ORDER BY training_and_skill_development.idx
		""", as_dict=1)
		
		if tt:
			for idx,i in enumerate(tt, start=1):
				self.append("q42", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# uu = frappe.db.sql("""select * from `tabIncentives and Motivation` order by idx """,as_dict=1)
		uu = frappe.db.sql("""
		SELECT incentives_and_motivation.*, audit_questions.*
		FROM `tabIncentives and Motivation` incentives_and_motivation
		JOIN `tabAudit Questions` audit_questions
		ON incentives_and_motivation.parent = audit_questions.name
		ORDER BY incentives_and_motivation.idx
		""", as_dict=1)
		
		if uu:
			for idx,i in enumerate(uu, start=1):
				self.append("q43", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# vv = frappe.db.sql("""select * from `tabError and Downtime Tracking` order by idx """,as_dict=1)
		vv = frappe.db.sql("""
		SELECT error_and_downtime_tracking.*, audit_questions.*
		FROM `tabError and Downtime Tracking` error_and_downtime_tracking
		JOIN `tabAudit Questions` audit_questions
		ON error_and_downtime_tracking.parent = audit_questions.name
		ORDER BY error_and_downtime_tracking.idx
		""", as_dict=1)
		
		if vv:
			for idx,i in enumerate(vv, start=1):
				self.append("q44", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# ww = frappe.db.sql("""select * from `tabWorkload Distribution` order by idx """,as_dict=1)
		ww = frappe.db.sql("""
		SELECT workload_distribution.*, audit_questions.*
		FROM `tabWorkload Distribution` workload_distribution
		JOIN `tabAudit Questions` audit_questions
		ON workload_distribution.parent = audit_questions.name
		ORDER BY workload_distribution.idx
		""", as_dict=1)
		
		if ww:
			for idx,i in enumerate(ww, start=1):
				self.append("q45", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# xx = frappe.db.sql("""select * from `tabFeedback Collection System` order by idx """,as_dict=1)
		xx = frappe.db.sql("""
		SELECT feedback_collection_system.*, audit_questions.*
		FROM `tabFeedback Collection System` feedback_collection_system
		JOIN `tabAudit Questions` audit_questions
		ON feedback_collection_system.parent = audit_questions.name
		ORDER BY feedback_collection_system.idx
		""", as_dict=1)
		
		if xx:
			for idx,i in enumerate(xx, start=1):
				self.append("q46", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# yy = frappe.db.sql("""select * from `tabRegular Feedback Sessions` order by idx """,as_dict=1)
		yy = frappe.db.sql("""
		SELECT regular_feedback_sessions.*, audit_questions.*
		FROM `tabRegular Feedback Sessions` regular_feedback_sessions
		JOIN `tabAudit Questions` audit_questions
		ON regular_feedback_sessions.parent = audit_questions.name
		ORDER BY regular_feedback_sessions.idx
		""", as_dict=1)
		
		if yy:
			for idx,i in enumerate(yy, start=1):
				self.append("q47", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		zz = frappe.db.sql("""
		SELECT worker_satisfaction.*, audit_questions.*
		FROM `tabWorker Satisfaction` worker_satisfaction
		JOIN `tabAudit Questions` audit_questions
		ON worker_satisfaction.parent = audit_questions.name
		ORDER BY worker_satisfaction.idx
		""", as_dict=1)
		
		if zz:
			for idx,i in enumerate(zz, start=1):
				self.append("q48", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		aaa = frappe.db.sql("""
		SELECT certifications.*, audit_questions.*
		FROM `tabCertifications` certifications
		JOIN `tabAudit Questions` audit_questions
		ON certifications.parent = audit_questions.name
		ORDER BY certifications.idx
		""", as_dict=1)
		
		if aaa:
			for idx,i in enumerate(aaa, start=1):
				self.append("q50", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		bbb = frappe.db.sql("""
		SELECT founders_details.*, audit_questions.*
		FROM `tabFounders Details` founders_details
		JOIN `tabAudit Questions` audit_questions
		ON founders_details.parent = audit_questions.name
		ORDER BY founders_details.idx
		""", as_dict=1)
		
		if bbb:
			for idx,i in enumerate(bbb, start=1):
				self.append("q51", {
					'questions': i.questions,
					'idx':idx
				})


# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		ccc = frappe.db.sql("""
		SELECT employee_details.*, audit_questions.*
		FROM `tabEmployee Details` employee_details
		JOIN `tabAudit Questions` audit_questions
		ON employee_details.parent = audit_questions.name
		ORDER BY employee_details.idx
		""", as_dict=1)
		
		if ccc:
			for idx,i in enumerate(ccc, start=1):
				self.append("q52", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		ddd = frappe.db.sql("""
		SELECT quality_policies.*, audit_questions.*
		FROM `tabQuality Policies` quality_policies
		JOIN `tabAudit Questions` audit_questions
		ON quality_policies.parent = audit_questions.name
		ORDER BY quality_policies.idx
		""", as_dict=1)
		
		if ddd:
			for idx,i in enumerate(ddd, start=1):
				self.append("q53", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		eee = frappe.db.sql("""
		SELECT worker_social.*, audit_questions.*
		FROM `tabWorker Social` worker_social
		JOIN `tabAudit Questions` audit_questions
		ON worker_social.parent = audit_questions.name
		ORDER BY worker_social.idx
		""", as_dict=1)
		
		if eee:
			for idx,i in enumerate(eee, start=1):
				self.append("q54", {
					'questions': i.questions,
					'idx':idx
				})
# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		fff = frappe.db.sql("""
		SELECT documentation_system.*, audit_questions.*
		FROM `tabDocumentation System` documentation_system
		JOIN `tabAudit Questions` audit_questions
		ON documentation_system.parent = audit_questions.name
		ORDER BY documentation_system.idx
		""", as_dict=1)
		
		if fff:
			for idx,i in enumerate(fff, start=1):
				self.append("q55", {
					'questions': i.questions,
					'idx':idx
				})	

# /////////////////////////////////////////////////////////////////////////////////////////////				

		# zz = frappe.db.sql("""select * from `tabWorker Satisfaction` order by idx """,as_dict=1)
		ggg = frappe.db.sql("""
		SELECT insurance_details.*, audit_questions.*
		FROM `tabInsurance Details` insurance_details
		JOIN `tabAudit Questions` audit_questions
		ON insurance_details.parent = audit_questions.name
		ORDER BY insurance_details.idx
		""", as_dict=1)
		
		if ggg:
			for idx,i in enumerate(ggg, start=1):
				self.append("q56", {
					'questions': i.questions,
					'idx':idx
				})	



	@frappe.whitelist()
	def add_points_to_internal_auditors(factory_audit_checklist):
		try:
			# Fetch the Factory Audit Checklist document
			audit_doc = frappe.get_doc("Factory Audit Checklist", factory_audit_checklist)

			# Check if 'internal_auditor_list' exists as a child table
			if not hasattr(audit_doc, 'internal_auditor_list'):
				frappe.throw(_("The Factory Audit Checklist does not have an Internal Auditor List"))

			# Fetch the child table 'Internal Auditor List'
			auditors = audit_doc.internal_auditor_list

			# Define the number of points to be awarded (default points for audit)
			points = cint(frappe.db.get_single_value("Energy Points Settings", "default_points_for_audit") or 1)

			# Set to track users who have already been awarded points
			awarded_users = set()
			
			# List to collect logs before inserting them
			auditor_logs = []

			# Award points to each auditor in the Internal Auditor List
			for auditor in auditors:
				if not auditor.employee_id or auditor.employee_id in awarded_users:
					continue

				# Fetch the employee's user linked to the employee_id
				employee_user = frappe.db.get_value("Employee", auditor.employee_id, "user_id")
				
				# If no user is linked to the employee, skip this auditor
				if not employee_user:
					frappe.log_error(_("No user linked to Employee ID {0}").format(auditor.employee_id))
					continue

				# Create an energy point log for the employee
				auditor_log = frappe.get_doc({
					"doctype": "Energy Point Log",
					"points": points,
					"user": employee_user,
					"reason": "Participation as Internal Auditor",
					"reference_doctype": "Factory Audit Checklist",
					"reference_name": audit_doc.name
				})
				auditor_logs.append(auditor_log)
				awarded_users.add(auditor.employee_id)

			# Insert all logs at once
			if auditor_logs:
				frappe.get_doclist(auditor_logs).insert()

				# Commit the transaction to save logs to the database
				frappe.db.commit()

		except Exception as e:
			# Log the error for debugging purposes
			frappe.log_error(frappe.get_traceback(), _("Failed to add points to internal auditors"))

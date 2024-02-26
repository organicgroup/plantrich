# Copyright (c) 2024, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CoffeeCostEstimation(Document):
	def validate(self):
		self.total_qty = 0
		self.total_logistic_cost = 0
		self.total_process_cost = 0
		self.total_consumables = 0
		self.total_packing_cost = 0
		self.total_profit_margin = 0
		for row in self.coffee_cost_details:
			self.total_qty += float(row.qty)
			self.total_logistic_cost += float(row.logistic_cost)
			self.total_process_cost += float(row.process_cost)
			self.total_consumables = float(row.consumables)
			self.total_packing_cost = float(row.packing_cost)
			self.total_profit_margin = float(row.profit_margin)

			net_qty_in_kg = row.rm_qty*(100-row.process_loss)/100
			cost_after_process = row.rm_cost/net_qty_in_kg*row.rm_qty
			qty_proportion = float(row.qty)/self.total_qty
			cost_per_kg = cost_after_process*qty_proportion
			logistic_cost = float(row.qty)*float(row.logistic_cost)
			consumables = float(row.qty)*float(row.consumables)
			process_cost = float(row.qty)*float(row.process_cost)
			packing_cost = float(row.qty)*float(row.packing_cost)
			total_cost = cost_per_kg + logistic_cost + process_cost + consumables + packing_cost
			profit_margin = total_cost*row.profit_margin
			# frappe.throw(profit_margin)
			self.coffee_cost_calculation = []
			self.append("coffee_cost_calculation", {
				"net_qty_in_kg": net_qty_in_kg,
				"cost_after_process": cost_after_process,
				"grade": row.grade,
				"qty_proportion": qty_proportion,
				"cost_per_kg": cost_per_kg,
				"logistic_cost": logistic_cost,
				"consumables": consumables,
				"process_cost": process_cost,
				"packing_cost": packing_cost,
				"total_cost": total_cost,
				"profit_margin": profit_margin,
				"ex_factory_price": total_cost*row.profit_margin,
				"selling_price": float(row.market_price_per_kg_today)*float(row.qty)
			})
		self.total_qty_proportion = 0
		self.total_cost_per_kg = 0
		self.calculated_tlc = 0
		self.calculated_total_process_cost = 0
		self.calculated_total_consumables = 0
		self.calculated_tpc = 0
		self.calculated_tc = 0
		self.calculated_tpm = 0
		self.total_ex_factory_cost = 0
		self.calculated_sp = 0
		for row in self.coffee_cost_calculation:
			self.total_qty_proportion += row.qty_proportion
			self.total_cost_per_kg += row.cost_per_kg
			self.calculated_tlc += row.logistic_cost
			self.calculated_total_process_cost += row.process_cost
			self.calculated_total_consumables += row.consumables
			self.calculated_tpc += row.packing_cost
			self.calculated_tc += row.total_cost
			self.calculated_tpm += row.profit_margin
			self.total_ex_factory_cost += row.ex_factory_price
			self.calculated_sp += row.selling_price


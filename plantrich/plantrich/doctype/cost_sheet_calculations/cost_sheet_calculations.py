# Copyright (c) 2024, sammish and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class COSTSHEETCALCULATIONS(Document):
# 	pass

from frappe.model.document import Document

class COSTSHEETCALCULATIONS(Document):
    def validate(self):
        # Perform calculations for multiple child tables
        self.calculate_child_table("ft_premium_coffee")
        self.calculate_child_table("ftmp_coffee_details")
        self.calculate_coffee_market_price_per_kg()
        self.calculate_coffee_market_price_report()
        self.calculate_product_description_table_coffee()
        self.calculate_fob_expenses()
        
        # Calculate specific child table: Coffee Market Price Report A
        self.calculate_coffee_market_price_report_a()

        # Calculate totals
        self.calculate_totals()

        # Calculate main totals
        self.calculate_main_totals()

        self.calculate_product_description_table_coffee()

    def calculate_child_table(self, child_table_name):
        exchange_rate_inrs = (
            self.exchange_rate_notification[0].inrs if self.exchange_rate_notification else 0
        )

        child_table = getattr(self, child_table_name, [])
        for row in child_table:
            row.usdkg = row.in_pound * 2.2046
            row.inrs = row.usdkg * exchange_rate_inrs

    def calculate_coffee_market_price_per_kg(self):
        exchange_rate_inrs = (
            self.exchange_rate_notification[0].inrs if self.exchange_rate_notification else 0
        )

        if exchange_rate_inrs > 0:  # Avoid division by zero
            for row in self.coffee_market_price_per_kg:
                row.usdkg = row.inrs / exchange_rate_inrs

    def calculate_coffee_market_price_report(self):
        exchange_rate_inrs = (
            self.exchange_rate_notification[0].inrs if self.exchange_rate_notification else 0
        )

        for row in self.coffee_market_price_report:
            row.usdkg = row.usdton / 1000 if row.usdton else 0
            row.inrs = row.usdkg * exchange_rate_inrs if exchange_rate_inrs else 0

    def calculate_coffee_market_price_report_a(self):
        exchange_rate_inrs = (
            self.exchange_rate_notification[0].inrs if self.exchange_rate_notification else 0
        )

        for row in self.coffee_market_price_report_a:  # Child table: Coffee Market Price Report A
            row.usdkg = row.uscent * 0.02204 if row.uscent else 0
            row.inrs = row.usdkg * exchange_rate_inrs if exchange_rate_inrs else 0

    def calculate_totals(self):
        total_usdkg = 0
        total_inr = 0
        total_usdkg1 = 0
        total_inr1 = 0

        for row in self.coffee_market_price_report:
            total_usdkg += row.usdkg if row.usdkg else 0
            total_inr += row.inrs if row.inrs else 0

        self.total_usdkg = total_usdkg
        self.total_inr = total_inr

        for row in self.coffee_market_price_report_a:
            total_usdkg1 += row.usdkg if row.usdkg else 0
            total_inr1 += row.inrs if row.inrs else 0

        self.total_usdkg1 = total_usdkg1
        self.total_inr1 = total_inr1

    def calculate_product_description_table_coffee(self):
        for row in self.product_description_table_coffee:
            row.amount = row.qty * row.rate if row.qty and row.rate else 0

    def calculate_fob_expenses(self):
        for row in self.fob_expenses:
            row.amount = row.qty * row.rate if row.qty and row.rate else 0

    def calculate_main_totals(self):
        
        self.total_product_amount = sum(
            row.amount for row in self.product_description_table_coffee if row.amount
        )
        self.total_fob_expenses = sum(
            row.amount for row in self.fob_expenses if row.amount
        )

        
        self.total = self.total_product_amount - self.total_fob_expenses

        
        self.price_per_kg = self.total / self.quantity if self.quantity else 0

        self.ft_premium = sum(row.inrs for row in self.ft_premium_coffee if row.inrs)

        
        self.selling_rate = self.price_per_kg + self.ft_premium if self.ft_premium else 0



    def calculate_product_description_table_coffee(self):
    
        if self.product_description_table_coffee:
        
            ftmp_first_inrs = self.ftmp_coffee_details[0].inrs if self.ftmp_coffee_details else 0
            coffee_market_inrs = max(
                row.inrs for row in self.coffee_market_price_per_kg if row.inrs
            ) if self.coffee_market_price_per_kg else 0
            total_inr = self.total_inr if hasattr(self, "total_inr") else 0
            total_inr1 = self.total_inr1 if hasattr(self, "total_inr1") else 0

        
            max_rate = max(ftmp_first_inrs, coffee_market_inrs, total_inr, total_inr1)

        
            self.product_description_table_coffee[0].rate = max_rate

    
        for row in self.product_description_table_coffee:
            row.amount = row.qty * row.rate if row.qty and row.rate else 0



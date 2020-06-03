# -*- coding: utf-8 -*-
# Copyright (c) 2020, suganya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Case(Document):
    def validate(self):
        check_package = frappe.get_all("Check Package",{"name":self.check_package})
        for ch in check_package:
            check = frappe.get_doc("Check Package",ch)
            check_list = check.checks_list
            for checks in check_list:
                un = int(checks.units)
                for unit in range(un):
                    if(self.checks_created!=1):
                        create_check = frappe.new_doc(checks.checks)
                        create_check.ce_tat = checks.ce_tat
                        create_check.customer = self.customer
                        create_check.check_package = self.check_package
                        create_check.batch = self.batch
                        create_check.case_id = self.name
                        create_check.case_name = self.case_name
                        create_check.date_of_birth = self.date_of_birth
                        create_check.case_gender = self.case_gender
                        create_check.father_name = self.father_name
                        create_check.email_id = self.email_id
                        create_check.client_employee_code = self.client_employee_code
                        create_check.insert()
                        create_check.save(ignore_permissions=True)
                        create_check = frappe.new_doc("Verify"+" "+checks.checks)
                        create_check.ce_tat = checks.ce_tat
                        create_check.customer = self.customer
                        create_check.check_package = self.check_package
                        create_check.batch = self.batch
                        create_check.case_id = self.name
                        create_check.case_name = self.case_name
                        create_check.date_of_birth = self.date_of_birth
                        create_check.case_gender = self.case_gender
                        create_check.father_name = self.father_name
                        create_check.email_id = self.email_id
                        create_check.client_employee_code = self.client_employee_code
                        create_check.insert()
                        create_check.save(ignore_permissions=True)
                       
                    
            if(self.entry_status == "Draft"):
                batch = frappe.get_doc("Batch",{"name":self.batch})
                count = int(batch.entry_count) - 1
                if(batch.entry_count!=0):
                    frappe.db.set_value("Batch",batch.name,"entry_count",count)
            


                    



            



           
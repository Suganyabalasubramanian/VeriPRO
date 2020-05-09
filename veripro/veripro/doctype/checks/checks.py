# -*- coding: utf-8 -*-
# Copyright (c) 2020, suganya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Checks(Document):
	def validate(self):
		add_check = frappe.new_doc(self.checks)
		add_check.insert()
		frappe.errprint(add_check)
# -*- coding: utf-8 -*-
# Copyright (c) 2020, suganya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Batch(Document):
	# pass
	def validate(self):
		self.entry_count = self.no_of_cases
	
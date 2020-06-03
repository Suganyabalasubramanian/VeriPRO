from __future__ import unicode_literals
import json
import calendar
import random
import frappe
import socket
import os
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils.data import today
from frappe.utils import cstr,formatdate, add_months, cint, fmt_money, add_days,flt
import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from frappe import throw, _, scrub
import time
import itertools
from frappe.utils import today, flt, add_days, date_diff
from frappe.utils.csvutils import read_csv_content
from erpnext.hr.doctype.employee.employee import get_holiday_list_for_employee, is_holiday

@frappe.whitelist()
def case_count(batch):
    count = frappe.db.count("Case",{"batch":batch})
    frappe.errprint(count)
    b1 = frappe.get_all("Batch",{"name":batch})
    for b in b1:
        batch_count = frappe.get_doc("Batch",b)
        if(batch_count.no_of_cases == count):
            frappe.throw("Entry not allowed")
    
    
   
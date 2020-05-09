from frappe import _

def get_data():
    return [
        {
			"label": _("General"),
			"items": [
                {
					"type": "doctype",
					"name": "Checks",
					"description": _("checks"),
					"onboard": 1,
				},
				# {
					
				# 	"name": "Check Variables",
				# 	"description": _("veripro"),
				# 	"onboard": 1,
				# },
				# {
				# 	"type": "doctype",
				# 	"name": "Check Package",
				# 	"description": _("Applicants"),
				# 	"onboard": 1,
				# },
				# {
				# 	"type": "doctype",
				# 	"name": "veriPRO Batch",
				# 	"description": _("Invoice"),
				# 	"onboard": 1,
				# },
				# {
				# 	"type": "doctype",
				# 	"name": "Case",
				# 	"description": _("Invoice"),
				# 	"onboard": 1,
				# },
               
            ]
        },
        # {
		# 	"label": _("Entry"),
		# 	"items": [
        #         {
		# 			"type": "doctype",
		# 			"name": "Address Check",
		# 			"description": _("checks"),
		# 			"onboard": 1,
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Education Check",
		# 			"description": _("veripro"),
		# 			"onboard": 1,
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Employment Check",
		# 			"description": _("Applicants"),
		# 			"onboard": 1,
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Identity Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Exit Interview",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Reference Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Vendor Screening",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Medical Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Family History",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Financial History",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Gap Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Database Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Criminal Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Matrimonial Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
               
        #     ]
        # },
        # {
		# 	"label": _("Execution"),
		# 	"items": [
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Address Check",
		# 			"description": _("checks"),
		# 			"onboard": 1,
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Verify Education Check",
		# 			"description": _("veripro"),
		# 			"onboard": 1,
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Verify Employment Check",
		# 			"description": _("Applicants"),
		# 			"onboard": 1,
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Verify Identity Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Exit Interview",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Reference Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Vendor Screening",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Medical Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Family History",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Financial History",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Gap Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Database Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Criminal Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
        #         {
		# 			"type": "doctype",
		# 			"name": "Verify Matrimonial Check",
		# 			"description": _("Invoice"),
		# 			"onboard": 1,
		# 		},
               
        #     ]
        # }
        # {
        #     "module_name": "veriPRO",
        #     "color": "grey",
        #     "icon": "fa fa-star",
        #             "type": "module",
        #             "label": _("General"),
        #             "items": [
        #                 {
        #                     "type": "doctype",
        #                     "name": "Check Package",
        #                     "icon": "fa fa-star",
        #                     "label": _("Check Package"),
        #                     "description": _("Check Package"),
        #                 },
        #                 {
        #                     "type": "doctype",
        #                     "name": "Applicant",
        #                     "icon": "fa fa-star",
        #                     "label": _("Applicant"),
        #                     "description": _("Applicant"),
        #                 },
        #                 {
        #                     "type": "doctype",
        #                     "name": "veriPRO Batch",
        #                     "icon": "fa fa-star",
        #                     "label": _("veriPRO Batch"),
        #                     "description": _("veriPRO Batch"),
        #                 },
        #                 {
        #                     "type": "doctype",
        #                     "name": "Sales Invoice",
        #                     "icon": "fa fa-star",
        #                     "label": _("veriPRO Batch"),
        #                     "description": _("veriPRO Batch"),
        #                 },
        #             ],
                    

        # },
        # {
        #     "module_name": "veriPRO",
        #     "color": "grey",
        #     "icon": "fa fa-star",
        #             "type": "module",
        #             "label": _("Entry"),
        #             "items": [
        #                 {
        #                     "type": "doctype",
        #                     "name": "Check Package",
        #                     "icon": "fa fa-star",
        #                     "label": _("Check Package"),
        #                     "description": _("Check Package"),
        #                 },
        #                 {
        #                     "type": "doctype",
        #                     "name": "Applicant",
        #                     "icon": "fa fa-star",
        #                     "label": _("Applicant"),
        #                     "description": _("Applicant"),
        #                 },
        #                 {
        #                     "type": "doctype",
        #                     "name": "veriPRO Batch",
        #                     "icon": "fa fa-star",
        #                     "label": _("veriPRO Batch"),
        #                     "description": _("veriPRO Batch"),
        #                 },
        #                 {
        #                     "type": "doctype",
        #                     "name": "Sales Invoice",
        #                     "icon": "fa fa-star",
        #                     "label": _("veriPRO Batch"),
        #                     "description": _("veriPRO Batch"),
        #                 },
        #             ],
                    

        # }
    ]

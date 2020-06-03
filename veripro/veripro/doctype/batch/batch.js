// Copyright (c) 2020, suganya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Batch", {
	customer: function (frm) {
		frappe.call({
			"method": "frappe.client.get_list",
			args: {
				"doctype": "Check Package",
				"customer": frm.doc.customer,
				// "fields": ["name"]
			},
			callback: function (r) {
				$.each(r.message, function (i, d) {
					frm.set_query("check_package", function () {
						return {
							"filters": {
								"customer": frm.doc.customer
							}
						};
					});

				})


			}
		})


	},
	// check_package: function (frm) {
	// 	frappe.call({
	// 		"method": "frappe.client.get",
	// 		args: {
	// 			"doctype": "Check Package",
	// 			"name": frm.doc.check_package

	// 		},
	// 		callback: function (r) {
				
	// 			$.each(r.message.checks_list, function (i, d) {
	// 				var row = frappe.model.add_child(frm.doc,"Checks","check_batch")
	// 				row.checks = d.checks
	// 				row.units = d.units
	// 				row.ca_tat = d.ca_tat
	// 				row.ce_tat = d.ce_tat
	// 				row.pricing_model = d.pricing_model
	// 				row.check_price = d.check_price
	// 				row.check_selling_price = d.check_selling_price
	// 				row.tcsp = d.tcsp
				

	// 			})
	// 			refresh_field("check_batch")

	// 		}
	// 	})

	// }


});
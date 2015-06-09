import frappe

def get_context(context):

	doctypes = frappe.get_list("Doctype")
	context.update({
		"doctypes": doctypes
	})
	return context

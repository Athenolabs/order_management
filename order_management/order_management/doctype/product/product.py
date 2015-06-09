# -*- coding: utf-8 -*-
# Copyright (c) 2015, Nishta Solutions and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.exceptions import ValidationError

class Product(Document):

	def autoname(self):
		self.name = '-'.join([self.category, self.subcategory, self.shape])
	
	def validate(self):
		pass
		# if frappe.db.count('Product', filters={
		# 	'category': self.category,
		# 	'shape': self.shape
		# }):
		# 	frappe.msgprint("A product already exists for this shape and category", raise_exception=ValidationError)

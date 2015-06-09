# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "order_management"
app_title = "Order Management"
app_publisher = "Nishta Solutions"
app_description = "Order Management for Bakery"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@nishtasolutions.in"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_js = [
	"assets/order_management/js/lib/jquery.colorpicker.js",
	"assets/order_management/js/lib/jquery-ui.min.js"
]
app_include_css = "assets/order_management/css/jquery.colorpicker.css"

# include js, css files in header of web template
# web_include_css = "/assets/order_management/css/order_management.css"
# web_include_js = "/assets/order_management/js/order_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "order_management.install.before_install"
# after_install = "order_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "order_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"order_management.tasks.all"
# 	],
# 	"daily": [
# 		"order_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"order_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"order_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"order_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "order_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "order_management.event.get_events"
# }

fixtures = ["State", "City","Category","Subcategory","Shape"]

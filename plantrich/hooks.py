from . import __version__ as app_version

app_name = "plantrich"
app_title = "Plantrich"
app_publisher = "sammish"
app_description = "Empowering Farmers"
app_email = "sammish.thundiyil@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/plantrich/css/plantrich.css"
# app_include_js = "/assets/plantrich/js/plantrich.js"

# include js, css files in header of web template
# web_include_css = "/assets/plantrich/css/plantrich.css"
# web_include_js = "/assets/plantrich/js/plantrich.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "plantrich/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Lead" : "public/js/lead.js",
	"Sales Invoice": "public/js/sales_invoice.js"

}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "plantrich.utils.jinja_methods",
#	"filters": "plantrich.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "plantrich.install.before_install"
# after_install = "plantrich.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "plantrich.uninstall.before_uninstall"
# after_uninstall = "plantrich.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "plantrich.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Lead": {
		"validate": "plantrich.doc_events.lead.get_item_total",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"plantrich.tasks.all"
#	],
#	"daily": [
#		"plantrich.tasks.daily"
#	],
#	"hourly": [
#		"plantrich.tasks.hourly"
#	],
#	"weekly": [
#		"plantrich.tasks.weekly"
#	],
#	"monthly": [
#		"plantrich.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "plantrich.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "plantrich.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "plantrich.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["plantrich.utils.before_request"]
# after_request = ["plantrich.utils.after_request"]

# Job Events
# ----------
# before_job = ["plantrich.utils.before_job"]
# after_job = ["plantrich.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"plantrich.auth.validate"
# ]

fixtures =[{
	"dt":"Custom Field",
	"filters":[
		["name","in",[
			"Lead-custom_job_title",
            "Lead-custom_interest",
            "Lead-custom_other_interest",
            "Lead-custom_section_break_hjz5x",
            "Lead-custom_is_sale",
            "Lead-custom_item",
            "Lead-custom_total_amount",

			"Sales Invoice-custom_business_type",

			'Job Applicant-father_name',
			'Job Applicant-sex',
			'Job Applicant-date_of_birth',
			'Job Applicant-religion_caste',
			'Job Applicant-blood_group',
			'Job Applicant-column_break_usn9v',
			'Job Applicant-marital_status',
			'Job Applicant-present_address',
			'Job Applicant-address',
			'Job Applicant-column_break_a1v2e',
			'Job Applicant-permanent_postal_address',
			'Job Applicant-same_as_present_address',
			'Job Applicant-driving_licences',
			'Job Applicant-passport',
			'Job Applicant-criminal_offence',
			'Job Applicant-disability',
			'Job Applicant-column_break_usr2x',
			'Job Applicant-section_break_npkrz',
			'Job Applicant-already_interviewed',
			'Job Applicant-employee_referral_1',
			'Job Applicant-section_break_pvc5u',
			'Job Applicant-educational_and_qualifications',
			'Job Applicant-section_break_kzuxl',
			'Job Applicant-courses_sales',
			'Job Applicant-section_break_9gt5p',
			'Job Applicant-language',
			'Job Applicant-section_break_ey4hj',
			'Job Applicant-employment_history',
			'Job Applicant-reason',
			'Job Applicant-section_break_mhzg4',
			'Job Applicant-references',
			'Job Applicant-column_break_faztx',
			'Job Applicant-section_break_yw5ti',
			'Job Applicant-about',
			'Job Applicant-section_break_4vyai',
			'Job Applicant-sign',
			'Job Applicant-column_break_rd1lj',
			'Job Applicant-place',
			'Job Applicant-notice_period_form_current_position_'

		]]
	]
},
{
	"dt":"Property Setter",
	"filters":
		[["name","in",[
			"Sales Invoice-naming_series-read_only"
		]]
	]
}]

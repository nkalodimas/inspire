"""
	Returns template subject and content for:
	a HEP reference ticket
"""
def get_template_data(record):
	from invenio.config import CFG_SITE_URL
	from invenio.bibrecord import record_get_field_value, record_get_field_values

	recid = record_get_field_value(record,'001','','','')
	report_numbers = record_get_field_values('037','_','_','a')
	queue = "HEP_ref"
	subject = "Refs for #%s %s" % ( recid, ' '.join(report_numbers))
	content = "%s/record/edit/#state=edit&recid=%s" % ( CFG_SITE_URL, recid)
	return (queue, subject, content)
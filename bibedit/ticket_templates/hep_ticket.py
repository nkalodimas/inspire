"""
	Returns template subject and content for:
	a HEP record ticket
"""
def get_template_data(record):
	from invenio.config import CFG_SITE_URL
	from invenio.bibrecord import record_get_field_value, record_get_field_values

	recid = record_get_field_value(record,'001','','','')
	report_numbers = record_get_field_values('037','_','_','a')
	postfix =''
	if report_numbers:
		postfix = ' '
	queue = "HEP_cor"
	subject = "%s%s(#%s)" % ( ' '.join(report_numbers), postfix, recid)
	content = "Curate record here: %s/record/edit/#state=edit&recid=%s" % ( CFG_SITE_URL, recid)
	return (queue, subject, content)
"""
	Returns template subject and content for:
	an authors_long_ticket ticket
"""
def get_template_data(record):
	from invenio.config import CFG_SITE_URL
	from invenio.bibrecord import record_get_field_value, record_get_field_values

	recid = record_get_field_value(record,'001','','','')
	report_numbers = record_get_field_values('037','_','_','a')
	queue = "AUTHORS_long_list"
	subject = "long author list in #%s %s" % ( recid, ' '.join(report_numbers))
	content = "Please update the authors in %s/record/edit/%s" % ( CFG_SITE_URL, recid)
	return (queue, subject, content)
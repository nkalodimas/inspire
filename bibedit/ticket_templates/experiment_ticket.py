"""
	Returns template subject and content for:
	an experiment ticket
"""
def get_template_data(record):
	from invenio.config import CFG_SITE_URL
	from invenio.bibrecord import record_get_field_value, record_get_field_values

	recid = record_get_field_value(record,'001','','','')
	report_numbers = record_get_field_values('037','_','_','a')
	queue = "Exp"
	subject = "unknown experiment in #%s %s" % ( recid, ' '.join(report_numbers))
	content = "This unknown experiment: \n\n\
	has appeared in this paper. Please create a record in Experiments and update the paper at\
	 %s/record/edit/%s" % ( CFG_SITE_URL, recid )
	return (queue, subject, content)
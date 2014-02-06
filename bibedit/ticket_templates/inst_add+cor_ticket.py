"""
	Returns template subject and content for:
	an institution ticket
"""
def get_template_data(record):
	from invenio.config import CFG_SITE_URL
	from invenio.bibrecord import record_get_field_value

	recid = record_get_field_value(record,'001','','','')
	queue = "INST_add+cor"
	subject = "new inst"
	content = "The record %(site)s/record/edit/%(recid)s has an unknown affiliation. The information given is:\n\n\
	Please create an Institutions record, if not done in the meantime, and update the paper at\
	 %(site)s/record/edit/%(recid)s with the correct inst short name." % { 'site' : CFG_SITE_URL, 'recid' : recid }
	return (queue, subject, content)
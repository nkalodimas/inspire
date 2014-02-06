"""
	Returns template subject and content for:
	a conference ticket
"""
def get_template_data(record):
	from invenio.config import CFG_SITE_URL
	from invenio.bibrecord import record_get_field_value

	recid = record_get_field_value(record,'001','','','')
	queue = "CONF_add+cor"
	subject = "new conf"
	content = "The record %(site)s/record/edit/%(recid)s has information on a new conference.\
	Please create a conference record if not done in the meantime, and update the\
	 paper at %(site)s/record/edit/%(recid)s" % { 'site' : CFG_SITE_URL, 'recid' : recid }
	return (queue, subject, content)
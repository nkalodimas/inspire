"""
Inspire tasklet.

Creates an RT ticket containing link to record with holding pen change applied.
"""

import os
import sys
from invenio.bibtask import write_message, task_get_option
from invenio.bibcatalog import BIBCATALOG_SYSTEM


def bst_hep_name_update(recordId, tmp_file_path, subject, content, queue, comment=''):
    """
    Creates an Rt ticket with the given properties and deletes the tmp xml file
    used in order to upload the holding pen change.

    @param recordId: the updated record's id
    @type recordId: string
    @param tmp_file_path: the path of tmp xml file used to store updated
    record's details
    @type tmp_file_path: string
    @param subject: the ticket's subject
    @type subject: string
    @param content: the ticket's content
    @type content: string
    @param queue: the ticket's queue
    @type queue: string
    @param comment: the user comment
    @type comment: string
    """
    hp_id = task_get_option('hp_id')
    content = content + str(hp_id)
    #submit ticket
    ticket_id = BIBCATALOG_SYSTEM.ticket_submit(subject=subject, queue=queue,text=content,
        recordid=recordId)
    if ticket_id:
        if comment:
            BIBCATALOG_SYSTEM.ticket_comment( None, ticket_id, comment)
        write_message("ticket for record %s submitted succesfully in queue" %
         (recordId, queue), verbose=3)
        # delete tmp xml file
        os.remove(tmp_file_path)
    else:
        write_message("ticket submission failed", sys.stderr, verbose=3)
    return 1

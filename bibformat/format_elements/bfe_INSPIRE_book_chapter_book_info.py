# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints book chapter's host book's info 
"""

from invenio.bibrecord import record_get_field_value, record_get_field_values
from invenio.search_engine import get_record
from invenio.bibformat_elements import bfe_INSPIRE_publi_info

def format_element(bfo, book_prefix='Book: ', separator='; ', view='detailed'):
    """
    Displays book info (various book fields)

    @param book_prefix: a prefix before each book
    @param separator: a separator between notes of a group
    """
    if view == "brief" and bfe_INSPIRE_publi_info.format_element(bfo):
        return

    book_details = get_book_details(bfo)
    if book_details:
        return book_prefix + book_details


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0

def get_book_details(bfo):
    """
    Checks whether the record is a book chapter record and if it contains
    the record id of the host book.
    In that case it retrieves the book record and returns various metadata
    of the book formatted.
    """
    details = ''
    recid = bfo.field('773__0')
    if "BookChapter" in bfo.fields('980__a') and recid:
        record = get_record(recid)
        if record:
            #chapter = record_get_field_value(record, '024', '', '', 'a').split('_')[-1]
            title = record_get_field_value(record, '245', '', '', 'a')
            main_author = record_get_field_value(record, '100', '', '', 'a')
            main_author_is_editor = record_get_field_value(record, '100', '', '', 'e')
            second_author = record_get_field_value(record, '700', '', '', 'a')
            second_author_is_editor = record_get_field_value(record, '700', '', '', 'e')
            number_of_authors = len(record_get_field_values(record, '700', '', '', 'a'))
            authors_suffix = ''
            if number_of_authors > 1:
                authors_suffix = 'et al.'
            publisher = record_get_field_value(record, '260', '', '', 'b')
            year = record_get_field_value(record, '260', '', '', 'c')
            details += 'chapter of '
            details += '\"' + title + '\",'
            details += '<br/>' + main_author
            if main_author_is_editor:
                details += ' (' + main_author_is_editor + ')'
            if second_author:
                details += ', ' + second_author
                if second_author_is_editor:
                    details += ' (' + second_author_is_editor + ')'
            details += authors_suffix
            if publisher:
                details += '<br/>' + ', published by ' + publisher
                if year:
                    details += ' (' + year + ')'
    return details
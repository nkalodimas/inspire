# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011 CERN.
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
"""BibFormat element - Prints twitter link for HepNames
"""
__revision__ = "$Id$"

def format_element(bfo):
    """
    Prints twitter link for HepNames from 035__9/a.
    """
    twitter_link = ''
    external_links = bfo.fields("035__")
    for field in external_links:
        if "twitter" in field.get('9','').lower():
            twitter_username = field.get('a','')
            if twitter_username:
                twitter_link = '<a href="http://twitter.com/' +\
                    twitter_username + '" >@' + twitter_username + '</a>'
            break

    return twitter_link

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0

# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008 CERN.
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
"""BibFormat element - Prints address for Institution.
"""
__revision__ = "$Id$"
from invenio.config import CFG_SITE_LANG
from invenio.search_engine import search_pattern

def format_element(bfo, separator=", "):
    #Print Address marc fields for an Inst record
    #
    out = []
    fulladdress = bfo.fields("371__", repeatable_subfields_p=True)

    for printaddress in fulladdress:
        if printaddress.has_key('x'):
            continue
        if printaddress.has_key('f'):
        ## if f exists print only f fields
        ## loop over f fields
            out.append(separator.join(printaddress['f']))
        else:
            ## only print all a's and d
            ## loop over a fields
            if printaddress.has_key('a'):
                out.append(separator.join(printaddress['a']))
            if printaddress.has_key('d'):
                out.append(separator.join(printaddress['d']))
            break

    return separator.join(out)

def escape_values(bfo):
    return 0

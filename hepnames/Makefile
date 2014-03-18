# $Id$

include ../config.mk
-include ../config-local.mk

LIBFILES = hepnames.py
LIBDIR = $(WEBDIR)
PYLIBFILES = hepnames_templates.py hepnames_config.py
PYLIBDIR = $(PREFIX)/lib/python/invenio
JSFILES = hepnames_update.js

all:
	@echo "Done."

test:
	@echo "Nothing to test."

install:
	$(INSTALL) -m 664 $(LIBFILES) $(LIBDIR)
	$(INSTALL) -m 664 $(PYLIBFILES) $(PYLIBDIR)
	$(INSTALL) -m 664 $(JSFILES) $(WEBDIR)/js

clean:
	@rm -f *.orig *~

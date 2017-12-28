AM_CFLAGS = -Wall -Werror


cputool_SOURCES = cputool.c cputool.h
cputool_LDADD = -lrt

man8_MANS = cputool.8

bin_PROGRAMS = cputool

# docbook2man writes the output itself, not to stdout
%.8: doc/%.sgml
	if [ "$(DOCBOOKTOMAN)" = "docbook2man" ]; then \
		$(DOCBOOKTOMAN) $< > /dev/null 2>&1; \
	else \
		$(DOCBOOKTOMAN) $< 2>&1 > $@ | sed 's/^[^:]*://'; \
	fi

# docbook2man creates extra files which need cleaning
distclean-local: killbuildmanpages

killbuildmanpages:
	rm -f doc/*.tmp manpage.refs manpage.links cputool.8

PacmanQuery2XML
---------------------------------------------------------------------------------
NoGuiLinux - Ni64Systems - Mon Feb  5 22:49:31 UTC 2018
---------------------------------------------------------------------------------
./getSystemOptionalDeps.sh
create xml dump of all system packages with just their 
optional dependencies.
Hopefully this may give someone some ideas

./pkg2xml.py
a python 3 script to xmlformatted data on an installed package on a linux system

you will need pyalpm and of course python3

usage: pkg2xml.py [-h] -p PACKAGE [-o] [-D] [-r] [-c] [-m] [-b] [-d] [-f] [-g]
                  [-k] [-R] [-e] [-P] [-A] [-w WRITE]

optional arguments:
  -h, --help            show this help message and exit
  -p PACKAGE, --package PACKAGE
  -o, --opt-deps
  -D, --depends
  -r, --required_by
  -c, --conflicts
  -m, --details
  -b, --backup
  -d, --dates
  -f, --files
  -g, --groups
  -k, --checksumsAndSigs
  -R, --replaces
  -e, --reason
  -P, --provides
  -A, --dump-all
  -w WRITE, --write WRITE
                        file to write xml dump to
please note that this tool dumps output in raw xml; for now, to prettify the output for human readability use `xmllint --format -`.

some simple examples are listed below:
	dump all package data:
		python pkg2xml.py -p vim | xmllint --format -
		python pkg2xml.py -p vim -A | xmllint --format -
	dump optional dependencies of a package:
		python pkg2xml.py -p vim -o | xmllint --format -

example output from `xmllint --format -`:
<?xml version="1.0"?>
<pkg name="vim">
  <optional_deps>
    <dep num="0">python2</dep>
    <dep num="1">python</dep>
    <dep num="2">ruby</dep>
    <dep num="3">lua</dep>
    <dep num="4">perl</dep>
    <dep num="5">tcl</dep>
  </optional_deps>
</pkg>

example out from pkg2xml.py:
<pkg name="vim"><optional_deps><dep num="0">python2</dep><dep num="1">python</dep><dep num="2">ruby</dep><dep num="3">lua</dep><dep num="4">perl</dep><dep num="5">tcl</dep></optional_deps></pkg>

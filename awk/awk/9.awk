#! /usr/bin/awk -f

BEGIN {
	f="";
}
{
	if ( f != FILENAME) {
		print "reading",FILENAME;
		f=FILENAME;
	}
	print;
}

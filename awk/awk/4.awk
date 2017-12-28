#! /usr/bin/awk -f

BEGIN {
	lines=0;
	total=0;
	}
{
	if ($1 != "total" ) lines++;
	total+=$1;
}
END {
	print lines ": lines read";
	print total ": total";
	if (lines > 0 ) {
		print "average is words per file: ",total/lines;
	}
	else {
		print "average words per file: 0"
	}
}


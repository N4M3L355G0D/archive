#! /usr/bin/awk -f
#11 fields
#3 target total
BEGIN {
	val=0;
	FS="|"
}
{
	print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11;
	val=val+$3;
	print "======\nTotal ($)\n"val"\n======\n";
}
END {
	if ( !NR ) {
	print "there are no return values from the SERVER";
	}
	else {
		print "END Total ($) :",val;
	}
}

#! /usr/bin/awk -f

BEGIN {
	# change the record separator, RS, to nothing
	RS="";
	# change the field separator to newline, \n
	FS="\n";
	# change output field separator to newline, \n
	OFS="\n";
	# change the output record separator to newline, \n
	ORS="\n";
}
{
	#print second and third line of file
	print $2, $3;
}

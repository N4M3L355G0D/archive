#! /usr/bin/awk -f

BEGIN {
	who="";
}
{
	FS=":"
if (length($0) > 1) {
	if ( NF > 6 ){
		for ( i=6 ; i <= NF ; i++ )
			if ( who == "" ) {
			print $1 " " $i;
			}
			else {
				if ( who == $1 ) {
					print $1 " " $i
				}
			}
		}
	}
}

#! /usr/bin/awk -f

BEGIN{
	FS=",";
	line="";
	fieldCheck="no";
	opt_fields="";
	term="";
	}
{
if ( fieldCheck == "no" ){
	if ( opt_fields != "" ) {
		if ( term != "" ) {
			if ( $opt_fields ~ term ) {
				print "opt_fields for term " term ": " $opt_fields
			}
		}
		else {
			print "opt_fields : " $opt_fields
		}
	}
	else {
		if ( $29 ~ "@" ) {
			print $29;
			}
		if ( $30 ~ "@" ) {
			print $30;
			}
		}
	}
	
else {
	for ( i=0 ; i < NF ; i++ ) {
	if ( $i ~ "@" ) {
		if ( i > 0 ) {
		print "NF" ":" NF " Email Field" ":" i;
		}
	} 
	}
	}
}


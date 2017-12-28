#! /usr/bin/awk -f

BEGIN {
       	print "NF\tColumn\tOpt_Col" ;
	f="";
}
{

	# set the output field seperator, OFS
	OFS="\t";
	# set column number here
	column=$3;
	opt_col=$2;
	# begin filter
	if ( $1 == "#COLON" ) {
		# set the field seperator, FS
		FS=":";
		# print number of fields, NF, column, and optional column (opt_col)
		if ( NF > 1 ) {
			print NF,column,opt_col;
		}
	}
	else if ( $1 == "#SEMICOLON" ) {
		FS=";";
		if ( NF > 1 ) {
			print NF,column,opt_col;
		}
	}
	else if ( $1 == "#SPACE" ) {
		FS=" ";
		print NF,column,opt_col;
	}
	else {
	# use the first delimiter is comes across per line
		if ( $0 ~ /:/ ) {
			FS=":";
			# re-evaluate the line
			$0=$0;
			}
		else if ( $0 ~ /;/ ) {
			FS=";";
			$0=$0;
			}
		else {
			FS=" ";
			$0=$0;
			}
		print NF,column,opt_col;
		}
}
END {
	# check for stdin
	if ( FILENAME == "-" ) {
		print "Reading from STDIN";
		}
	# if not stdin, print FILENAME
	else if ( f != FILENAME){
		print "Reading: ",FILENAME;
		f=FILENAME;
		}
}

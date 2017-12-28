#! /usr/bin/awk -f
BEGIN {
	# create a predefined array
	username[""]=0;
	size[""]=0;
	inode[""]=0;
	OFS="=";
	print "Label           User","Data";
	print "--------------- -----------";
}
{
	#only increment input that has 10 fields
	if ( NF > 10 ) {
		username[$4]++;
		inode[$1]++;
		if ( inode[$1] == 1 ) {
			size[$4]+=$6;
		}
	}
	else if (( NF > 7 ) && (NF < 10 )) {
		print "are you using `ls -li`?";
		exit;
	}
}
END {
	for ( i in username) {
		# only print array fields that contain data
		if ( i != "" ) {
			print "FT for User:    " i,username[i];
			print "DU User[bytes]: " i,size[i];
		}
	}
	print "\n\nLegend";
	print "FT "," File number total";
	print "DU "," Disk Useage, or total space used, in bytes";
}

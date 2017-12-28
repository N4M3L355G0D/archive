#! /usr/bin/awk -f

BEGIN { print "File\tOwner\tPermissions"} 
{ print $9, "\t", $3,"\t",$1} 
END { print " - DONE -" } 

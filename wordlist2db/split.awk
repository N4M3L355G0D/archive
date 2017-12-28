#! /usr/bin/awk -f

{
	print "split -a 8 --numeric-suffixes=0 -l " 4000000 " " $0 " " $0 ".part_";
}	

#! /bin/bash

for (( i=0 ; "$i" <= "`wc -l yaourt-packages.txt | cut -f1 -d' '`" ; i=`expr $i + 1` )) ; do
	cmd=`cat yaourt-packages.txt | nl | grep -w " $i" | sed s\|"\t"\|"#"\|g | cut -f2 -d"#" | sed s\|"^"\|"yaourt -S "\|g`
	$cmd
done

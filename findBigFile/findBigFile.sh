#! /usr/bin/env bash
#noguilinux
#will be adding config options later to use sqlite3 db, text, hardcode settings, with the finally of user input if settings fail
#find files of $SIZE
searchTerm=('') 

#load locations from cnf
cnf="fBF.cnf"
searchTermFromCnf="`grep -w "searchTerm" $cnf | cut -f 2 -d=`"
export IFS=","
for i in $searchTermFromCnf ; do
	searchTerm+=($i)
done

#let the user know the 'where' and 'from where the "where"' came from
cat << EOF
Locations to Searched as specified from $cnf
`for i in ${searchTerm[@]}; do echo -e "\t"$i ; done`

EOF

bar(){
python3 << EOF
def barcalc():
 string="$1"
 stringLen=len(string)
 oput='='*stringLen
 print(oput)
barcalc()
EOF
}


SIZE="+512M"
#cmds
# demo="dryrun"
# demo="find"

read -rp "cmd: " demo
#purely internal
counter=0
#messages
dr="a dry run was requested"
ar="Results of the File Search"
errInvalidCmd="error that is not a valid cmd"

for i in ${searchTerm[@]} ; do 
	if test $demo == "dryrun" ; then
		if test "$counter" -lt 1 ; then
			bar "$dr"
			echo "$dr"
			bar "$dr"
		fi
		echo -e "\t$i"
	elif test "$demo" == "find" ; then
	       	if test $counter -lt 1 ; then
			bar "$ar"
			echo "$ar"
			bar "$ar"
		fi
		if test "$i" != "" ; then
			bar "$i"
			echo "$i"
			bar "$i"
			time find "$i" -xdev -size "$SIZE" -print0 | xargs -0 ls -shQ
			echo
		fi
	else
		bar "$errInvalidCmd"
		echo "$errInvalidCmd"
		bar "$errInvalidCmd"
		exit 1
	fi
	counter=`expr $counter + 1`
done
#just for asthetic appearance
echo

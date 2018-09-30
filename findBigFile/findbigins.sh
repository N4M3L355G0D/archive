#! /usr/bin/env bash
#NoGuiLinux

##Generate a list of files that exist on system that are over a certain size

#adjustable vars
LOC=('/home/carl' '/srv/samba')
SZ='+1G'
cDelim=','

function calculate(){
	echo "$1/(1024^$2)" | bc
}

function size2Eng(){
	if test "$1" -le 1024 ; then
		echo "$1"
	elif test "$1" -ge $((1024 ** 1)) && test "$1" -le $((1024 ** 2)) ; then
		echo "`calculate $1 1`K"
	elif test "$1" -ge $((1024 ** 2)) && test "$1" -le $((1024 ** 3)) ; then
		echo "`calculate $1 2`M"
	elif test "$1" -ge $((1024 ** 3)) && test "$1" -le $((1024 ** 4)) ; then
		echo "`calculate $1 3`G"
	elif test "$1" -ge $((1024 ** 4)) && test "$1" -le $((1024 ** 5)) ; then
		echo "`calculate $1 4 `T"
	elif test "$1" -ge $((1024 ** 5)) && test "$1" -le $((1024 ** 6)) ; then
		echo "`calculate $1 5 `P"
	else
		echo "$1"
	fi
}

function findFile(){
	echo "fname_path""$cDelim""relaSize"
	for loc in ${LOC[@]} ; do
		file="`find "$loc" -size "$SZ" | tr '\n' '#'`"
        	export IFS='#'
		for FNAME in ${file[@]}; do
			export IFS=' '	
			if test ! -e "$FNAME" ; then
				echo "$FNAME [does not exist]"
			else
				file=$(stat "`echo $FNAME`" --format='%n#%s')
				size=`echo $file | cut -f2 -d'#'`
				file="`echo $file | cut -f1 -d'#'`"
				echo "$file$cDelim`size2Eng $size`"
			fi
		done
		export IFS=' '
	done
}
findFile

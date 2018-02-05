#! /usr/bin/env bash
#NoGuiLinux
#example code on how to xml formatted document of optional package dependencies for all packages installed on system

function optionaldepends(){
	if test "$1" == "" ; then
		read -rp "outfile: " $OUTFILE
	else
		OUTFILE="$1"
	fi

	echo "<list>" > $OUTFILE
	for PACKAGE in `pacman -Qqe` ; do 
		python3 pkg2xml.py -p "$PACKAGE" -o >> $OUTFILE
	done 
	echo "</list>" >> $OUTFILE
}
optionaldepends "$@"

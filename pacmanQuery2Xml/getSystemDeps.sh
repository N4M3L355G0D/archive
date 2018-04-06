#! /usr/bin/env bash
#NoGuiLinux
#example code on how to xml formatted document of optional package dependencies for all packages installed on system

function repName(){
	read  IN
	echo "$IN" | cut -f1 -d'<' | sed s/'&gt;'/'>'/g | sed s/'&lt;'/'<'/g 
}
function systemDepends(){
	xmlDir="pkg-xml"
	finalized="finalized"
	if test "$1" == "" ; then
		read -rp "outfile: " OUTFILE
	else
		OUTFILE="$1"
	fi
	if test ! -e "$xmlDir" ; then
		mkdir "$xmlDir"
	fi
	for PACKAGE in `pacman -Qq` ; do 
		python3 pkg2xml.py -p "$PACKAGE" -oD | xmllint --format - | grep -v 'xml version="1.0"' >> "$xmlDir""/""$OUTFILE""_""$PACKAGE"".xml"
	done 
	cat pkg-xml/*.xml | grep 'dep num' | cut -f 2 -d'>' | cut -f1 -d'<' > "$OUTFILE"".txt" 
	cat pkg-xml/*.xml | grep 'pkg name' | cut -f 2 -d'"' >> "$OUTFILE"".txt"
	rm -r "$xmlDir"
	python3 extraprocessing.py -p "$OUTFILE"".txt" -o "$finalized"".txt"
	mv "$finalized"".txt" "$OUTFILE"".txt"
	for line in `cat "$OUTFILE"".txt"` ; do
		echo "$line" | repName >> "$finalized"".txt"
	done
	mv "$finalized"".txt" "$OUTFILE"".txt"
}
systemDepends "$@"


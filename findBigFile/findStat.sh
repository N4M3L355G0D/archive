#! /usr/bin/env python3
#NoGuiLinux

TYPE="*.py"
SIZE=""
LOC="$HOME"

function findStr(){
#actions here are performed on each line printed by find

cat << EOF
if test -f "$1" ; then
	printf '<unit name="$1">\n' ; 

	printf '\t<ls>\n' ; 
	ls -hlQ '$1' | sed s/'^'/'\t\t\t'/g ; 
	printf '\t</ls>\n' ;

	if test "$SIZE" == "" ; then
		printf '\t<grep>\n' ;
		grep '#\!' '$1' | sed s/'^'/'\t\t\t'/g ; 
		printf '\t</grep>\n' ;
	fi

	printf '\t<stat>\n' ;
	stat '$1' | sed s/'^'/'\t\t\t'/g ; 
	printf '\t</stat>\n' ;

	printf '\t<file>\n' ;
	file ~/.bashrc --mime-encoding --mime-type '$1' | sed s/'^'/'\t\t\t'/g ;
	printf '\t</file>\n' ;
	
	printf '\t<sha512>\n' ;
	sha512sum '$1' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
	printf '\t</sha512>\n' ;
	
	printf '\t<sha256>\n' ;
	sha256sum '$1' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
	printf '\t</sha256>\n' ;
	
	printf '\t<md5sum>\n' ;
	md5sum '$1' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
	printf '\t</md5sum>\n' ;
	
	printf '</unit>\n' ;
fi
EOF
}

function findPy2(){
echo "<results type=""'$TYPE'"">"

find "$LOC" -iname "$TYPE" -exec bash -c "`findStr {}`" \; | sed s/'^'/'\t'/g

echo '</results>'
}

function findBigFile(){

echo "<results size=""'$SIZE'"">"

find "$LOC" -size "$SIZE" -exec bash -c "`findStr {}`" \; 2> /dev/null | sed s/'^'/'\t'/g

echo "</results>"

}

function helper(){
cat << EOF
syntax: bash $0
	-size [file extension]
	-type [file size]

EOF
}

function main(){
	read -rp "Path: " LOC
	if test "$1" == '-size' ; then
		if test "$2" == "" ; then
			read -rp "minimum file size: " SIZE
		else
			SIZE="$2"
		fi
		findBigFile
	elif test "$1" == "-type" ; then
		if test "$2" == "" ; then
			read -rp "filetype/extension: " TYPE
		else
			TYPE="$2"
		fi
		findPy2
	else
		helper
	fi
}

main "$@"

#! /usr/bin/env bash
#NoGuiLinux
# another revised version of mix-cap
function lowerCase(){
	read iString
	echo "$iString" | sed 's/\([a-z]\)/\U\1/g' 
}

function upperCase(){
	read iString
	echo "$iString" | sed 's/\([A-Z]\)/\l\1/g'
}

function wordCap(){
	read iString
	echo "$iString" | sed 's/\(^[a-z]\)/\U\1/g'
}

function mixCase(){
	wordCap="no"
	acc=''
	if test "$1" == "" ; then
		read iString
	else
		if test "$1" == "wordCap" ; then
			wordCap="yes"
		fi
		iString="$2"
	fi
	if test "$mode" == "mixCaseM" ; then
		broken="`echo $iString | grep -o .`"
		counter=0
		direction_forward="upperCase"
		direction_backward="lowerCase"
		for char in $broken ; do
			if test "`expr $counter \% 2`" == 0 ; then
				acc="$acc""`echo $char | $direction_forward`"
			else
				acc="$acc""`echo $char | $direction_backward`"
			fi
			counter="`expr $counter + 1`"
		done
	elif test "$mode" == "wordCap" ; then
		#you idiot, seriously, the only place where $char is even valid is the wordCap == 'no' block
		acc="`echo "$iString" | wordCap`"
	fi
	echo "$acc"
}
function main(){
	iString=''
	mode="wordCap"
	modes=("wordCap" "mixCaseM")
	exist="no"
	if test "$1" == "" ; then
		while test "$iString" == "" ; do
			read -rp "enter a string to transform: " iString
		done
	else
		if test "$1" == "wordCap" ; then
			mode="wordCap"
		elif test "$1" == "mixCaseM" ; then
			mode="mixCaseM"
		fi
		for m in ${modes[@]} ; do
			if test "$mode" == "$m" ; then
				exist="yes"
			fi
		done
		if test $exist != "yes" ; then
			echo "that mode is not supported!"
			exit 1
		fi
		iString="$2"
	fi
	acc=()
	counter=0
	for word in $iString ; do
		acc[$counter]="`mixCase "$mode" "$word"`"
		counter="`expr $counter + 1`"
	done
	echo "${acc[@]}"
}
#take input from all cmd-line args
main "$@"

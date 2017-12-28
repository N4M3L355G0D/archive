#! /bin/bash
path="./tmp"
if [ ! -z "$1" ] ; then
	if [ "$1" == "two-gen" ] ; then
		shift
		previous="$1"
		cat "$@" | grep ":" | grep -v "WEP" | uniq |  cut -f1 -d" " > "$path"/bigger.tmp 	
	elif [ "$1" == "one-gen" ] ; then
		shift
		current="$1"
		if [ -e "$current" ] ; then
			cat "$current" | grep ":" | grep -v "WEP" | uniq | cut -f1 -d" " > "$path"/smaller.tmp
		else
			echo "no such file file or directory: $current"
			exit
		fi
	fi
else
	echo "use one-gen to generate source mac file 'one'"
	echo "use two-gen to generate current source mac file 'two'"
fi

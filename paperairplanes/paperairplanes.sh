#! /usr/bin/env bash

function badvals(){
python3 << EOF
import string
acc=""
ac=([" "+char+" " for char in ''.join([string.ascii_letters,string.punctuation])])
for i in ac:
 acc+=i
print(acc)
EOF
}
function checkNum(){
	bad="no"
	val="`echo "$1" | grep -o .`"
	for char in $val ; do
		for testChar in `badvals` ; do
			if test "$char" == "$testChar" ; then
				bad="yes"
				break
			fi
			if test "$bad" == "yes" ; then
				break
			fi
		done
	done
	if test "$bad" == "yes" ; then
		return 1
	else
		return 0
	fi
}
function main(){
	MESSAGE="I will not throw paper airplanes in class."
	counter=1
	dumbCounter=1
	countOut=20
	checked="no"
	MAX=''
	if test "$1" != "" ; then
		MAX="$1"
	else
		while test "$checked" == "no"; do 
			read -rp "How many lines am I supposed to write for you?:" MAX
			if test "$MAX" != "" ; then
				if checkNum "$MAX" == 1; then
					checked="yes"
				fi
			fi
			dumbCounter="`expr $dumbCounter + 1`"
			if test "$dumbCounter" -ge "$countOut" ; then
				echo "apparently you do not know what a number is... why should I help you?"
				exit 1
			fi
		done
	fi
	while test $counter -le $MAX ; do
		echo "$counter : $MESSAGE"
		counter="`expr $counter + 1`"
	done
}
main

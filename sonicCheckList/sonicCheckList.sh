#! /usr/bin/env bash
#noguilinux

function bar(){
python3 << EOF
string="$1"
barChar="="
barString=barChar*len(string)
print(barString)
EOF
}

function datecode(){
	date +H%HM%MS%Smm%mdd%dyy%Y
}

function sonicCheckList(){
	src_dir="."
	ctrl="$(datecode) - $(whoami)" 
	ctrlBar=`bar "$ctrl"`

	echo "$ctrlBar"
	echo "$ctrl"
	echo "$ctrlBar"
	echo -e "`cat \"$src_dir\"/sonic-cookschecklist-vH21M55S39mm12dd23yy2017.txt `" | sed -e s/^' '*/'  '/ | nl
}
if test "$1" == "-print" ; then
	sonicCheckList | lpr
elif test "$1" == "-to-file" ; then
	sonicCheckList > sonicChecklist-current.txt
else
	sonicCheckList
fi

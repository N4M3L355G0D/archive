#! /usr/bin/env bash
#6/22/2017
#hackit/noguilinux
if [ -z "$1" ] ; then
	echo "no file provided"
	exit
fi

if [ ! -e "$1" ] ; then
	echo "$1 : no such file or directory"
fi

bssid='00:02:6F:92:10:5C'
ap="IRTSortAP_1"

cat << EOF
[AP=$ap]
[iFile=$1]

EOF

cat "$1" | grep "$bssid" | awk 'BEGIN{OFS="," ; print "MAC_Address"  "\t\t  AP[BSSID]\n================= =================";}{print $1 " " $8}' | grep -v '-' | sed s/"$ap"/""/g | sed s/','/""/g

#! /bin/bash

header(){
python3 << EOF
import time
a=len("$1")
dash=""
Dash=""
final=""
finalS=""
for i in range(0,a):
	dash=dash+"="
	middle=dash+" "+"$1"+" DATE ["+time.ctime()+"] "+dash+"\n"
for i in range(0,len(middle)):
	final=final+"-"
finalS=final+"\n"+middle+final+"\n"
print(finalS)
EOF
}


localCheck() {
 if [ -e "$1" ] ; then
	 header "$1"
	 cat "$1"
	 echo -e "\n"
 else
	 echo "$1 Does not Exist"
 fi
}
localCheck ./stringparser.h
localCheck ./userparse.c
localCheck ./print-preview.sh

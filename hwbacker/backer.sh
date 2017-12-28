#! /bin/bash

user_check(){
if [ `whoami` != "root" ] ; then
 echo "You are not SUDO/ROOT!"
 exit
fi
}

answer_continue(){
/usr/bin/python3 << EOF
no=["no","No","n","N","NO","nO"]
if "$1" in no:
 print("True")
else:
 print("False")
EOF
}

main() {
hwSize=`hdparm -I "$1" | fgrep 'device size with M = 1000*1000:' | cut -f2 -d\( | cut -f1 -d\) | sed s\|" "\|"_"\|g`

if [ ! -z "$1" ] && [ ! -z "$2" ] && [ ! -z "$3" ] && [ ! -z "$4" ] ; then
read -rp "The File will take the form of \"$2\"-\"`date \"+%R %D\" | sed s\|'/'\|'.'\|g`\"-\"$3\"-\"$4\".\"$hwSize\".\"img\". Do you wish to continue? [N/y] : " continue
 if [ `answer_continue $continue` == "False" ] ; then
  dd if="$1" of="$2"-"`date \"+%R %D\" | sed s\|'/'\|'.'\|g`"-"$3"-"$4"."$hwSize"."img"
 else
  echo "operation aborted!"
 fi
else
 if [ -z "$1" ] ; then
  echo "<disk DEV || FILE> : NOT LISTED"
 fi
 
 if [ -z "$2" ] ; then
  echo "<HOSTNAME> : NOT LISTED"
 fi

 if [ -z "$3" ] ; then
  echo "<OS> : NOT LISTED"
 fi

 if [ -z "$4" ] ; then
  echo "<ARCH> : NOT LISTED"
 fi
 echo -e "$0 <disk DEV || FILE> <HOSTNAME> <OS> <ARCH>" 
fi
}
user_check
main "$1" "$2" "$3" "$4"

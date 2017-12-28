#! /bin/bash

gencheck(){
if [ -e "$1" ] ; then
 if [ -e /usr/bin/pv ] ; then
  cat "$1" | pv | sha512sum -b | cut -f 1 -d" "
 else
  cat "$1" | sha512sum -b | cut -f 1 -d" "
 fi
else
 echo "That file does not exist"
fi
}

verify(){
 echo "======== Separator Line ========"
 echo "$1" | fgrep -w "$2"
 echo "======== Separator Line ========"
 echo "If you see any output between the separator lines, then the hash sums match"
}

helper() {
cat << EOF

-h, --help help,this screen
-v,--verify compare two hashes
-g generate a verification hash

EOF

}

if [ ! -z "$1" ] ; then
 if [ "$1" == "--verify" ] || [ "$1" == "-v" ] ; then
  verify "$2" "$3"
 elif [ "$1" == "-g" ] ; then
  gencheck "$2"
 elif [ "$1" == "--help" ] || [ "$1" == "-h" ] ; then
  helper
 fi
else
helper
fi

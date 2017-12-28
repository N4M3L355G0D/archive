#! /bin/bash

RFILE=./remove.txt
if [ -e "$RFILE" ] ; then
	cat $RFILE | awk '{ print "yaourt -S " $1 } '
else
	echo "$RFILE : Does not exist!"
fi

#! /bin/bash

if [ ! -e "$1" ] ; then
 mkdir "$1"
 cd "$1"
else
 cd "$1"
fi
datecode=`sha512sum <<< "$1 $(date)" | cut -f1 -d" "`

#uncomment for visual indicator check
/usr/bin/python3 ../trucate.py $datecode


sudo barcode -S -b "`/usr/bin/python3 ../trucate.py $datecode`" -o "`echo "$1" | sed s\|" "\|"_"\|g`".svg

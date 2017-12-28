#! /usr/bin/env bash

#remove spaces from netgearxx.txt.part_* wordlists

for i in `ls -1 netgearxx.txt.part_*` ; do
       	echo "$i" 
	cat "$i" | sed s\|" "\|""\|g > "$i".tmp
	mv "$i".tmp "$i"
done

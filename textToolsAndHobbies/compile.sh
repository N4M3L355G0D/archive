#! /bin/bash
build() {

 gcc -o num2ascii.bin num2ascii.c
}


build

buD=./backup
if [ ! -e "$buD" ] ; then
	mkdir "$buD"
fi

if [ $? == 0 ] ; then
	cp num2ascii.c "$buD"/num2ascii-`date +%F"H"%H"M"%M"S"%S"NS"%N`.c
else
	echo "there was a failure in build() run, so no backup was made!"
fi

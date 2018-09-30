#! /usr/bin/env bash
#NoGuiLinux
file='file.txt'
#as far as i know, without the ability to seek a file, using a while loop in shell/bash to count file by lines is not possible when using a while loop; here are some alternatives, each with some flaws to consider

function linecounter1(){
	#this is the most fool proof method
	#if file is huge >1GB, you will be waiting a bit, still the fast method though
	#wc is written in c, and is available on most linux distros
	#using wc -l will count lines by the \n character
	wc -l $file | cut -f1 -d" "
}
function linecounter2(){
	#be warned this method is flawed and is susceptible to memory overflow if the file is too big
	IFS="\n"
	counter=0
	for line in `cat $file` ; do
		counter=$(( $counter + 1 ))
	done
	IFS=' '
	echo $counter
}
function linecounter3(){
	#this is susceptible to not displaying anything/counting if a newline is alone on one line
	cat -b $file | tail -n1 | cut -f1 -d" "
}
function linecounter4(){
	#same problem as linecounter3
	nl $file | tail -n1 | cut -f1 -d" "
}
function linecounter5(){
	#this example can be found in the man pages for read
	counter=0
	while read x ; do
		counter=$(( $counter + 1 ))
	done < $file
	echo $counter
	#this will yield the same result in linecounter1() without the pipe
}
linecounter5

#! /usr/bin/env bash
#noguilinux
#a simple nc based server script


datecode(){
	date +H%HM%MS%Smm%mdd%dyy%y
}
#topdir log will be stored
topdir="."
#port number to listen on
port=2389

#since x evaluates to true when compared to itself, infinite loop
x="x"
while test "$x" == "$x" ; do
	echo "starting connection"
	#run netcat,nc, and log the results
	nc -l "$port" > "$topdir"/log.`datecode`
	echo "connection ended"
done

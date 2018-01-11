#! /usr/bin/env bash
#noguilinux
#check packet loss to see if host is up
#if packet loss is less than 100, then host is up, if packet loss is less than 100 but greater than zero
#a degraded connnection error is produced as well
#if packet loss is equal to 100, then consider the host down, due to lack of packet return

function protocolStrip(){
	host="$1"
	protocols=("https" "http" "ftp" "rdp")
	h=''
	counter=0
	for protocol in ${protocols[@]} ; do
		h="`echo "$1" | sed "s/^$protocol:\/\//->HOST<- /"`"
		hSub="`echo "$h" | cut -f2 -d" "`"
		hSub1="`echo "$h" | cut -f1 -d" "`"
		if test "$hSub1" == "->HOST<-"  ; then
			echo "$hSub"
			counter=0
		else
			counter="`expr $counter + 1`"
		fi
	done
	if test $counter -eq ${#protocols[@]} ; then
		#if string has reach here and unsupported protocol has been used
		h0st="`echo "$h" | cut -f3 -d"/"`"
		if test "$h0st" == "" ; then
			echo INVALID_URI: $h
			exit 1
		else
			echo "$h0st"
		fi
	fi
}
function packetLoss(){
	host="$1"
	ping -b -c 1 "$host" | grep -w "packets transmitted" | cut -f3 -d, | sed 's/ //g' | cut -f1 -d%
}

#protocolStrip https://google.com0
#protocolStrip google.com1
#protocolStrip rtp://google.com2
#protocolStrip rtp:/google.com3 [fail]
function conStatus(){
	url="$1"
	if test "$url" != "" ; then
		host="`protocolStrip $url`"
		hostStat="`echo $host | cut -f1 -d":"`" 
		if test "$hostStat" == "$host"; then
			stat=`packetLoss $host`
			if test "$stat" -lt 100 ; then
				echo host: UP
				if test "$stat" -gt 0 && test "$stat" -lt 100 ; then
					echo "connection_status: DEGRADED"
				fi
			else
				echo host: DOWN
			fi
		else
			echo $host
		fi
	else
		echo "ERROR: url cannot be blank"
	fi
}
conStatus "$1"

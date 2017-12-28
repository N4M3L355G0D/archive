#! /usr/bin/env bash

#set system up for airodump-ng
#noguilinux

card=wlan0

helper(){
	cat << EOF
       	use start/stop
	start - prep system for airodump-ng
	stop - bring system back to pre-start state
EOF
}


if [ "$1" == "start" ] ; then
	sudo systemctl stop NetworkManager
	sudo iwconfig wlan0 mode monitor
	sudo ifconfig wlan0 up
elif [ "$1" == "stop" ] ; then
	sudo ifconfig wlan0 down
	sudo iwconfig wlan0 mode managed
	sudo systemctl start NetworkManager
else
	case "$1" in
		#add other options here
		*)
			helper
			;;
	esac
fi

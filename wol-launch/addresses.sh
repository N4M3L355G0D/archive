#! /bin/bash

echo "you will need to install wol-systemd from the AUR"
echo "you will need to install etherwake from the AUR"

case "$1" in

all-on)
	upwards_MAC=64:31:50:92:ce:6a
	#vohlboar['MAC-Address']=00:24:54:3e:78:c0
	trialis_MAC=44:1e:a1:e2:a1:e8
	echo waking upwards
	sudo etherwake -i enp3s0 $upwards_MAC
	sleep 5s
	echo waking Trialis
	sudo etherwake -i enp3s0 $trialis_MAC
	;;
all-off)
	ssh carl@10.42.0.60 poweroff
	ssh carl@10.42.0.85 poweroff
	;;
*)
	cat << EOF
	all-on : turn on all wol units
	all-off : turn off all wol units through ssh
EOF
	;;
esac

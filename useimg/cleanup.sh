#! /usr/bin/env bash
#NoGuiLinux
#cleanup the mess created by a failed createimg.sh
VG="critical"
loopFile="0"
imgFile="disk.img"

function error(){
	printf "ERROR %s\n" "$@"
}
function checkUser(){
	if `whoami` != "root" ; then
		error "[`whoami`] is not root!"
		exit 1
	fi
}
function VGDisable(){
	vgchange -an "$VG"
}
function PVRemvove(){
	pvremove --force --force /dev/loop"$loopFile"
}
function loopRemove(){
	#detatch the loopdevice
	losetup -d /dev/loop"$loopFile"
}
function imgDel(){
	rm "$imgFile"
}

#! /bin/bash

error() {
	err="empty variable... cannot continue [$1]"
	zenity --error --text="$err"
	echo "$err"
}

cancelled() {

	err="$1 entry cancelled"
	zenity --error --text="$err"
	echo "$err"
}

main() {
#this is here because I am currently on a DHCP'd network, and the address
#could change at any time
address=`zenity --entry --text="remote share address"`
if [ -z "$address" ] ; then
	cancelled "address"
	exit
fi

if [ ! -e "$HOME/.remote-share" ] || [ "$1" == "--override-cfg" ] ; then
	user=`zenity --entry --text="remote share USERNAME"`
	if [ -z "$user" ] ; then
		cancelled "user"
		exit
	fi
	pass=`zenity --entry --text="remote share PASSWORD"`
	if [ -z "$pass" ] ; then
		cancelled "pass"
		exit
	fi
	share=`zenity --entry --text="sharename"`
	if [ -z "$share" ] ; then
		cancelled "share"
		exit
	fi
	mntpnt=`zenity --entry --text="mount point"`
	if [ -z "$mntpnt" ] ; then
		cancelled "mntpnt"
		exit
	fi
else
	user=`cat "$HOME"/.remote-share | grep -w "user" | cut -f2 -d"="`
	pass=`cat "$HOME"/.remote-share | grep -w "pass" | cut -f2 -d"="`
	share=`cat "$HOME"/.remote-share | grep -w "share" | cut -f2 -d"="`
	mntpnt=`cat "$HOME"/.remote-share | grep -w "mount_point" | cut -f2 -d"="`
fi
if [ -z "$pass" ] ; then
	error "pass"
	exit
fi
if [ -z "$user" ] ; then
	error "user"
	exit
fi
if [ -z "$share" ] ; then
	error "share"
	exit
fi
if [ -z "$mntpnt" ] ; then
	error "mntpnt"
	exit
fi
sudo mount -t cifs //"$address"/$share "$mntpnt" -o username="$user",password="$pass"
}

main "$@"

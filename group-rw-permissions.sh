#! /usr/bin/env bash
#NoGuiLinux

function checkRoot(){
	if test `whoami` == 'root' ; then
		return 0
	else
		return 1
	fi
}	


function mkGroupShare(){
	group="group_share"
	directory="/srv/samba/group-share"
	users=('carl' 'root')
	if checkRoot ; then

		if test ! -e "$directory" ; then
			mkdir "$directory"
		fi

		groupadd "$group"
		chgrp "$group" /srv/samba/group-share
		chmod -R g+rwx /srv/samba/group-share
	
		#add desired users to group share

		for user in ${users[@]} ; do
			usermod -a -G "$group" $user
		done
	else
		printf "user is not root!\n"
	fi
}
mkGroupShare

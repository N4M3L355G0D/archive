#! /usr/bin/env bash
#NoGuiLinux

if test "`whoami`" == "root" ; then
	smbCfg=/etc/samba/smb.conf
	
	cp $smbCfg $smbCfg.bak	
	
	bash `pwd`/lib/checkDeps.sh
	if test ! "$?" -eq 0 ; then
		exit 1
	fi
	
	if test -e $smbCfg ; then
		#this script checks for the share first, if it exists, then don't add it, otherwise add it
		python3 `pwd`/lib/smbparse.py
	else
		printf "missing $smbCfg\n"
		exit 1
	fi
	
	if test ! -e /srv/samba/storage ; then
		mkdir /srv/samba/storage
	fi
	chown -R root:root /srv/samba/storage
	chmod -R 775 /srv/samba/storage

	systemctl restart smb nmb

	sudo bash `pwd`/lib/mkdisk.sh
	
	#do a demomount
else
	echo "user `whoami` is not root!"
fi

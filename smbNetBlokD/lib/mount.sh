#! /usr/bin/env bash
#NoGuiLinux

if test `whoami` == "root" ; then
	dirs=('mount' 'disk')
	
	for folder in ${dirs[@]} ; do
	    if test ! -e "$folder" ; then
        	mkdir "$folder"
	    fi
	done

	read -rp "user: " user
	read -rp "password: " password
	read -rp "host: " host
	
	mount -t cifs //"$host"/storage mount -o username=$user,password=$password
	mount mount/storage.img disk
else
	echo "user `whoami` is not root"
fi

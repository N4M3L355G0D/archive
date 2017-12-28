#! /bin/bash

PTH=cfe2a9e5-a177-449a-87c6-691b1be03483
target=/run/media/carl/$PTH/"`hostname`-`whoami`"/
if [ ! -e "$target" ] ; then
	mkdir "$target"
fi
/usr/bin/cp -rv --remove-destination /home/carl /srv/samba /etc /var/cache/pacman $target 
echo "last backup on `date` by `whoami` for `hostname`" >> /var/run/media/carl/$PTH/backup.log

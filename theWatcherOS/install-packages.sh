#! /usr/bin/env bash
#NoGuiLinux

if test `whoami` == "root" ; then
	#python3 whichIsIt.py > installed.txt
	grep "OFFICIAL" installed.txt | cut -f1 -d: > official.txt

	#make container
	mkdir container
	pacstrap --config ./pacman.conf -i /mnt base base-devel $(cat official.txt)
	
	grep "AUR" installed.txt | cut -f1 -d: > aur.txt

	cp aur.txt yaourt-install.sh install-aur.sh /mnt/root/


	genfstab /mnt > /mnt/etc/fstab
	#boot container
	#systemd-nspawn -b -D container
	arch-chroot /mnt
	#log in to root
	#run rootlogin.sh
	##run containerlogin.sh
else
	printf "user '%s' is not 'root'" `whoami`
fi

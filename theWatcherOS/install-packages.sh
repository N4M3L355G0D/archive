#! /usr/bin/env bash
#NoGuiLinux

if test `whoami` == "root" ; then
	#python3 whichIsIt.py > installed.txt
	grep "OFFICIAL" installed.txt | cut -f1 -d: > official.txt

	#make container
	#mkdir
	pacstrap -C ./pacman.conf -i /mnt base base-devel $(cat official.txt)
	
	grep "AUR" installed.txt | cut -f1 -d: > aur.txt

	cp arch-linux-config.sh aur.txt yaourt-install.sh install-aur.sh containerlogin.sh rootlogin.sh /mnt/root/
	cp smb.conf /mnt/etc/samba/

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

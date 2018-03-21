#! /usr/bin/env bash
#NoGuiLinux
#post system install

#ensure NetworkManager is started
sudo systemctl start NetworkManager
if test $? != 0 ; then
	printf "%s" "starting NetworkManager failed..."
	exit 1
fi
#needed for yaourt
pacman -S yajl

bash yaourt-install.sh

yaourt -S <<< cat base-pkgs.txt

pkgs=('NetworkManager' 'sshd' 'smbd' 'nmbd' 'lightdm')

cp -v smb.conf /etc/samba/

for i in {'enable','start'} ; do
	for j in ${pkgs[@]} ; do
		systemctl "$i" "$j"
	done
done

#for systemwide users
cp -v .bashrc /etc/skel/
cp -v .bashrc $HOME
cp -rv wallpapers /srv/
cp -rv etc/* /etc
grub-mkconfig -o /boot/grub/grub.cfg

cd LAMP_install
bash lampinstall.sh


#! /bin/bash
echo "-4  [update pacman]"
sudo pacman -Syyu
echo "-3 [pack-common gen]"
python common.py > pack-common
echo "-2 [pacman.sh gen]"
cat pack-common | ./filet-arch.awk > pacman.sh
echo "-1 [pacman.sh exec]"
bash pacman.sh
echo "0 [pack gen]"
python compare.py > pack
echo "1 [aur-isntall.sh gen]"
sudo pacman -S $(cat pack) |& grep error: | ./filet.awk > aur-install.sh
exit
echo "2 [aur-install.sh exec]"
bash aur-install.sh
echo "3 [cleanup]"
rm pack pack-common aur-install.sh pacman.sh
echo "4 [grub backup]" 
DATE=`date`
sudo cp /boot/grub/grub.cfg /boot/grub/grub.cfg."$DATE".bak
echo "5 [grub update]" 
sudo grub-mkconfig -o /boot/grub/grub.cfg
if [ $? == 0 ] ; then
	echo -e "\t[grub update successful, removing grub backup]"
	sudo rm /boot/grub/grub.cfg."$DATE".bak
else
	echo -e "\t[grub update failed, backup kept]"
fi
echo 6

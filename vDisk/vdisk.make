#! /bin/bash

gui=`zenity --forms --title="vDisk" --add-entry="Disk Name" --add-entry="Size" --add-entry="Format Command"` 
name=`echo $gui | cut -f1 -d'|'`
size=`echo $gui | cut -f2 -d'|'`
format=`echo $gui | cut -f3 -d'|'`
checkMount=`mount | grep -w $name.img.d | cut -f2 -d'/' | head -n 1 `
if [ -a $name.img ] ; then
	if [ -f $name.img ] ; then
		warning=`zenity --question --text="This image already exists, would you like to overwrite it"`
		if [ $? == 0 ] ; then
				if [ ! -z $checkMount ] ; then
				warning=`zenity --question --text="This image is mounted, would you like to unmount it?"`
					if [ $? == 0 ] ; then
					sudo -S umount $name.img.d < /opt/vdisk/.password
					sudo -S mount -a < /opt/vdisk/.password
					fi 
				fi
		sudo -S rm -rf $name.img $name.img.d < /opt/vdisk/.password
		elif [ $? == 0 ] ; then
			zenity --warning --text="Then there is nothing else to do. Good Bye!"
			sudo -S killall -9 vdisk < /opt/vdisk/.password
		fi
	fi
fi
stage1=`sudo -S dd if=/dev/zero of=$name.img bs=1M count=$size < /opt/vdisk/.password`
sudo -S $format $name.img < /opt/vdisk/.password
sudo -S mkdir $name.img.d < /opt/vdisk/.password
sudo -S mount $name.img $name.img.d < /opt/vdisk/.password
sudo -S chmod -R 777 $name.img.d < /opt/vdisk/.password

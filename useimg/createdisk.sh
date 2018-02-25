#! /usr/bin/env bash
#NoGuiLinux
DISK="disk.img"
max=4
diskSize="18G"
VG="critical"
LV="disk"
LVSize="4G"
raidLVL="5"
raidDev="md0"
loopDev="0"
cryptDev="e"
period=1s
localMount="mount"
user="carl"
group="carl"
function error(){
	printf "Error: %s\n" "$@"
	exit 1
}
function checkUser(){
	if test `whoami` != "root" ; then
		error "user is not root/sudo"
	fi
}
function diskCreate(){
	if test ! -e "$DISK" ; then
		fallocate -l "$diskSize" "$DISK"
	else
		error "there is already a file by that name '$DISK'"
	fi
}
function diskLoop(){
	losetup	/dev/loop$loopDev "$DISK"
	if test "$?" != 0 ; then
		error "something went wrong in diskLoop()"
	fi
}
function diskPVCreate(){
	pvcreate /dev/loop$loopDev
	if test "$?" != 0 ; then
		error "something went wrong in diskPVCreate()"
	fi
}
function diskVGCreate(){
	vgcreate "$VG" /dev/loop$loopDev
	if test "$?" != 0 ; then
		error "something went wrong in diskVGCreate()"
	fi
}
function diskDisksCreate(){
	x=1
	while (( $x < $max )) ; do
		lvcreate -n "$LV"$x -L "$LVSize" "$VG"
		if test "$?" != 0 ; then
			error "something went wrong in diskDisksCreate() for disk$i"
		fi
		x=$(( $x + 1 ))
	done
}
function diskDisksRaid(){
	#a loop will be used later to optimize adding new disks 
	mdadm --create /dev/$raidDev --level $raidLVL --raid-devices=$(($max - 1)) /dev/mapper/critical-disk1 /dev/mapper/critical-disk2 /dev/mapper/critical-disk3
	if test "$?" != 0 ; then
		error "something went wrong in diskDisksRaid()"
	fi
}
function diskCryptFormat(){
	cryptsetup luksFormat /dev/$raidDev
	if test "$?" != 0 ; then
		error "something went wrong in diskCryptFormat()"
	fi
}
function diskCryptOpen(){
	cryptsetup luksOpen /dev/$raidDev "$cryptDev"
	if test "$?" != 0 ; then
		error "something went wrong in diskCryptOpen()"
	fi
}
function diskFSFormat(){
	mkfs.ext4 /dev/mapper/"$cryptDev"
	if test "$?" != 0 ; then
		error "something went wrong in diskFSFormat()"
	fi
}
function diskMount(){
	if test ! -e "$localMount" ; then
		mkdir "$localMount"
	fi
	mount /dev/mapper/$cryptDev mount
	chown -R $user:$group mount/
	su -c "chmod -R 775 mount" $user
}
function main(){
	checkUser
	sleep $period
	diskCreate
	sleep $period
	diskLoop
	sleep $period
	diskPVCreate
	sleep $period
	diskVGCreate
	sleep $period
	diskDisksCreate	
	sleep $period
	diskDisksRaid
	sleep $period
	diskCryptFormat
	sleep $period
	diskCryptOpen
	sleep $period
	diskFSFormat
	sleep $period
	diskMount
}
main

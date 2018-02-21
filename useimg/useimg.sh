#! /usr/bin/env bash
#NoGuiLinux

period=1
imgFile=""
eFile=""
mdDevice=""
localMount=""
loopFile=""
VG=""
function xml(){
	xmllint "$1" --xpath "$2"/"text()"
}
function getcfg(){
	cfg="useimg.xml"
	if test -e "$cfg" ; then
		period=`xml "$cfg" "/config/period"`
		imgFile=`xml "$cfg" "/config/imgFile"`
		eFile=`xml "$cfg" "/config/eFile"`
		mdDevice=`xml "$cfg" "/config/mdDevice"`
		localMount=`xml "$cfg" "/config/localMount"`
		loopFile=`xml "$cfg" "/config/loopFile"`
		VG=`xml "$cfg" "/config/VG"`
		return 0
	else
		printf "%s\n" "config file '$cfg' does not exist"
		return 1
	fi
}
function periodCheck(){
	if test "$period" == '' ; then
		echo "period is not specified in config"
		return 1
	else
		return 0
	fi
}
function imgFileCheck(){
	if test ! -e "$imgFile" ; then
		echo "period does not exist"
		return 1
	else
		return 0
	fi
}
function mdDeviceCheck(){
	if test ! -e "$mdDevice" ; then
		echo "mdDevice seems to not have been created"
		return 1
	else
		return 0
	fi
}
function localMountCheck(){
	if test ! -e "$localMount" ; then
		echo "localMount does not exist! creating!"
		mkdir "$localMount"
		if test "$?" != 0 ; then
			echo "something went wrong and localMount was not created"
			return 1
		else
			return 0
		fi
	else
		return 0
	fi
}
function loopFileCheck(){
	if test ! -e "$loopFile" ; then
		echo "loopFile was not created!"
		return 1
	else
		return 0
	fi
}
function eFileCheck(){
	if test ! -e "/dev/mapper/$eFile" ; then
		echo "eFile was not created!"
		return 1
	else
		return 0
	fi
}
function run(){
	#execution appears to occur too fast, so application of a wait period seems to fix it	
	if getcfg ; then
		if ! periodCheck ; then
			exit 1
		else
			printf "%s" "#"
		fi

		if ! imgFileCheck ; then
			exit 2
		else
			printf "%s" "#"
		fi

		if test "$1" == "-m" ; then

			sudo losetup "$loopFile" "$imgFile"
			if ! loopFileCheck; then
				exit 3
			else
				printf "%s" "#"
			fi
	        	
			sleep $period	
			
			sudo mdadm --auto-detect
			if ! mdDeviceCheck; then
				exit 4
			else
				printf "%s\n" "#"
			fi

			sleep $period
			
			sudo cryptsetup luksOpen "$mdDevice" "$eFile"
			if ! eFileCheck; then
				exit 5
			else
				printf "%s" "#"
			fi

			sleep $period
			
			if ! localMountCheck; then
				exit 6
			else
				printf "%s\n" "#"
			fi

			sudo mount /dev/mapper/"$eFile" "$localMount"

		elif test "$1" == "-u" ; then
			sudo umount "$localMount"
			sudo cryptsetup close "$eFile"
			sudo mdadm --stop "$mdDevice"
			sudo vgchange -an "$VG"
			sudo losetup -d "$loopFile"
		fi
	else
		printf "%s\n" "an error occurred during the process of getting the configuration"
	fi
}
run "$@"

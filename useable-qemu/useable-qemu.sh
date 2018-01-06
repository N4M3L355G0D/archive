#! /usr/bin/env bash
#noguilinux

function randomMac(){
python3 << EOF

import random

addr=['52',':','54',':']
top=4
for num,i in enumerate(range(top)):
    raIntHexStr=str(hex(random.randint(0,255))).strip("0x")
    addr.append(raIntHexStr)
    if num < top-1:
        addr.append(":")
print(''.join(addr))

EOF
}


###NOTES TODOS###
#get external configurations from
#sqlite3
#xmllint
#textfile
#cmdline arg supplied
##use python with argparse
#read -rp
##if errors fail with errors_msg

export QEMU_AUDIO_DRV=pa
export QEMU_PA_SOURCE=input

# sink should be something like alsa_output.pci-0000_00_1f.3.analog-stereo.monitor
export QEMU_PA_SINK=`pactl list sinks | grep "Monitor Source" | cut -f2 -d: | sed s/^' '*//`

CD='/srv/samba/middle/Torrents/ubuntu-17.10-desktop-amd64.iso'
IMG="ubu.img"
IMG_SIZE="10G"
CMD="qemu-system-x86_64"

#common values
cpu="host"
accel="kvm"
ram="4G"
cores="4"
vga="std"
display="gtk"
#macAddr="`randomMac`"
DB="qemuVM.db"
name="`echo "$IMG" | sed s\|"\.img"$\|\|`"
exist=''
nicModel="pcnet"
#soundHW="hda"
soundHW=""
function optionSift(){
	input="$1"
	shift
	option="$1"
	echo -e "$input" | grep -w "$option" | cut -f2 -d'#' 
}

function getConfig(){
	if test "$1" != "" ; then
		arg="style"
		style="$1"
	else
		arg=""
	fi
	data="`bash ./config.sh $arg "$style"`"
	if test "$data" == "invalid configuration format" ; then
		echo "$data"
		exit 1
	elif test "`echo $data | cut -f2 -d":"`" == "configuration file does not exist" ; then
		echo "$data"
		exit 1
	elif test "$data" == "no configuration files exist!" ; then
		echo "$data"
		exit 1
	else
		CD="`optionSift "$data" "CD"`"
		IMG="`optionSift "$data" "IMG"`"
		IMG_SIZE="`optionSift "$data" "IMG_SIZE"`"
		CMD="`optionSift "$data" "CMD"`"
		cpu="`optionSift "$data" "cpu"`"
		accel="`optionSift "$data" "accel"`"
		ram="`optionSift "$data" "ram"`"
		cores="`optionSift "$data" "cores"`"
		vga="`optionSift "$data" "vga"`"
		display="`optionSift "$data" "display"`"
		DB="`optionSift "$data" "DB"`"
		name="`optionSift "$data" "name"`"
		nicModel="`optionSift "$data" "nicModel"`"
		soundHW="`optionSift "$data" "soundHW"`"
	fi
}

function records(){
	if test "$1" != "skip" ; then
		macAddr="`randomMac`"
		exist="`sqlite3 "$DB" "select mac from macs where mac = '$macAddr'"`"
	fi
	vm="`sqlite3 "$DB" "select name from macs where name = '$name' ;"`"
	if test "$vm" == "" ; then
		sqlite3 "$DB" "insert into macs(mac,name) values ('$macAddr','$name');"
		echo $name@$macAddr
	else
		macAddr="`sqlite3 "$DB" "select mac from macs where name='$name'"`"
		echo $name@$macAddr
	fi
}

function macRecord(){
	macAddr="`randomMac`"
	#need detection if a vm is running
	if test ! -e "$DB" ; then
		sqlite3 "$DB" "create table if not exists macs ( mac text, name text );"

	fi
	exist="`sqlite3 "$DB" "select mac from macs where mac = '$macAddr'"`"
	if test "$exist" == "" ; then
		records skip
	else
		while test "$exist" != "" ; do
			records
		done
	fi
}

function resetGlobalDefaults(){
	macRecord
	COMMON="-vga $vga -display $display -cpu $cpu -accel $accel -m $ram -smp cores=$cores -enable-kvm -net nic,macaddr="`macRecord | cut -f2 -d"@"`",model="$nicModel" -net user -soundhw $soundHW -usb -device usb-tablet"
	ISO_COMMON="-drive file=$CD,format=raw,media=cdrom,readonly"
	# append new element to DEV_PASS_USB array to add new device

	#use lsusb to get addresses for devices
	#please not that the most reliable way to specify a device is to use vendorid:productid
	#to use vendorid:productid from lsusb, take the values from the desired device and add 0x to the beginning
	#this indicates that the value is hexadecimal
	#in the code below, 0x04f9:0x0075 is my Brother HL-2305W printer
	DEV_PASS_USB=("-device usb-host,vendorid=0x04f9,productid=0x0075")
	INSTALL="-cdrom $CD -boot order=d -drive format=raw,file=$IMG"
	RUN="-drive format=raw,file=$IMG"
}
#need a function to remove mac after vm has shut down

macRecord
#global defaults
COMMON="-vga $vga -display $display -cpu $cpu -accel $accel -m $ram -smp cores=$cores -enable-kvm -net nic,macaddr="`macRecord | cut -f2 -d"@"`",model="$nicModel" -net user -soundhw $soundHW -usb -device usb-tablet"
ISO_COMMON="-drive file=$CD,format=raw,media=cdrom,readonly"
# append new element to DEV_PASS_USB array to add new device

#use lsusb to get addresses for devices
#please not that the most reliable way to specify a device is to use vendorid:productid
#to use vendorid:productid from lsusb, take the values from the desired device and add 0x to the beginning
#this indicates that the value is hexadecimal
#in the code below, 0x04f9:0x0075 is my Brother HL-2305W printer
DEV_PASS_USB=("-device usb-host,vendorid=0x04f9,productid=0x0075")
INSTALL="-cdrom $CD -boot order=d -drive format=raw,file=$IMG"
RUN="-drive format=raw,file=$IMG"

function checkDeps(){
	export IFS=":"
	deps=("bc":"xmllint":"$CMD":"sqlite3":"python3")
	exist="no"
	missing=()
	counter=0
	for dep in ${deps[@]} ; do
		exist="no"
		for i in $PATH ; do
			pth="$i"/"$dep"
			if test -e "$pth" && test -f "$pth" ; then
				exist="yes"
			fi
		done
		if test "$exist" == "no" ; then
			counter="`expr $counter + 1`"
			missing[$counter]="$dep"
		fi
	done
	export IFS=" "
	if test "${#missing[@]}" -gt 0 ; then
		echo -e "missing dependencies:\n`echo ${missing[@]} | tr " " "\n" | sed s/^/'\t'/`"
		exit 1
	fi	
}

function main(){
	if test "$1" == "style" ; then
		if test "$2" != "" ; then
			cnfT="$2"
			shift 2
		else
			echo "\$2 cannot be blank"
			exit 1
		fi
	else
		if test "$2" == "style" ; then
			if test "$3" != "" ; then
				cnfT="$3"
			else
				echo "\$3 cannot be blank"
			fi
		fi
	fi
	checkDeps
	getConfig "$cnfT"
	resetGlobalDefaults
	checkDeps
	if test "$1" == "iso-only" ; then
		sudo $CMD $COMMON $ISO_COMMON ${DEV_PASS_USB[@]}
	elif test "$1" == "install" ; then
		fallocate -l "$IMG_SIZE" "$IMG"
		mkfs.ext4 "$IMG"
		sudo $CMD $COMMON $INSTALL ${DEV_PASS_USB[@]}
	elif test "$1" == "check" ; then
		sudo $CMD $COMMON $INSTALL ${DEV_PASS_USB[@]}
	else
		sudo $CMD $COMMON $RUN ${DEV_PASS_USB[@]}
	fi
}
main "$@"

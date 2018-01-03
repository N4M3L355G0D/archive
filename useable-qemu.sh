#! /usr/bin/env bash
#noguilinux

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

COMMON="-vga $vga -display $display -cpu $cpu -accel $accel -m $ram -smp cores=$cores -enable-kvm -net nic,model=pcnet -net user -soundhw hda -usb"
ISO_COMMON="-drive file=$CD,format=raw,media=cdrom,readonly"
# do a for-loop to add new devices
#use lsusb to get addresses for devices
#please not that the most reliable way to specify a device is to use vendorid:productid
#to use vendorid:productid from lsusb, take the values from the desired device and add 0x to the beginning
#this indicates that the value is hexadecimal
#in the code below, 0x04f9:0x0075 is my Brother HL-2305W printer
DEV_PASS_USB=("-device usb-host,vendorid=0x04f9,productid=0x0075")
INSTALL="-cdrom $CD -boot order=d -drive format=raw,file=$IMG"
RUN="-drive format=raw,file=$IMG"

function main(){
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

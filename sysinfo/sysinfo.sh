#! /bin/bash
if [ -z $1 ] ; then
	echo "a general tool to ease a Windows User into the linux world. It's also nice to have a wrapper that allows for general gathering of hardware info."
	echo "                      "
	echo "sysinfo.sh <info type> <search term, other than for other ( has its own options )>"
	echo "                      "
	echo "======================"
	echo "Info types: "
	echo "cpu - processor info"
	echo "pci - pci bus based info ( graphics card/network card/etc...)"
	echo "usb - usb devices ( usb hubs, connected devces ( phones/flash devices/etc...))"
	echo "other - kernel info, machine info, Processor Arch ( which is : $(uname -m))"
	echo "other options: "
	echo "kernel | node | os | kernel-version | kernel-release | processor | arch | hardware-platfrom"
elif [ $1 == "cpu" ] ; then
	if [ -z $2 ] ; then
		lscpu
	else
		lscpu | grep "$2"
	fi
elif [ $1 == "pci" ] ; then
	if [ -z $2 ] ; then
		lspci
	else
		lspci | grep "$2"
	fi
elif [ $1 == "usb" ] ; then
	if [ -z $2 ] ; then
		lsusb
	else
		lsusb | grep "$2"
	fi
elif [ $1 == "other" ] ; then
	if [ -z "$2" ] ; then
		uname -a
	elif [ "$2" == "kernel" ] ; then
		uname -s
	elif [ "$2" == "node" ] ; then
		uname -n
	elif [ "$2" == "kernel-version" ] ; then
		uname -v
	elif [ "$2" == "kernel-release" ] ; then
		uname -r
	elif [ "$2" == "arch" ] ; then
		uname -m
	elif [ "$2" == "processor" ] ; then
		uname -p
	elif [ "$2" == "hardware-platform" ] ; then
		uname -i
	elif [ "$2" == "os" ] ; then
		uname -o
	fi
fi














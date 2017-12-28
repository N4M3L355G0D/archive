#! /bin/bash

config=wps-office.cfg
base_path=/opt/software
ss="$base_path"/wps-office/et
wd="$base_path"/wps-office/wps
pd="$base_path"/wps-office/wpp
arch=`uname -m`
package64=`cat $config | grep -w source64 | cut -f2 -d=`
package32=`cat $config | grep -w source32 | cut -f2 -d=`
pack64=`basename "$package64"`
pack32=`basename "$package32"`
dir64=`echo $pack64 | sed s\|".tar.xz"\|""\|g`
dir32=`echo $pack32 | sed s\|".tar.xz"\|""\|g`

echo "Download Path: $package64"

if [ ! -e "$base_path" ] ; then
 sudo mkdir "$base_path"
 if [ $? == "1" ] ; then
  echo "you do not have sudo permissions... will exit NOW!"
  exit
 fi
fi

if [ -e $ss ] ; then
	if [ -e $wd ] ; then
		if [ -e $pd ] ; then
			getopts "wps" mode
			if [ $mode == "w" ] ; then
				echo "writer mode"
				/opt/software/wps-office/wps $@
			elif [ $mode == "p" ] ; then
				echo "presentation mode"
				/opt/software/wps-office/wpp $@
			elif [ $mode == "s" ] ; then
				echo "spread sheet mode"
				/opt/software/wps-office/et $@
			else
				echo "there is no such mode!"
				echo "syntax: "
				echo "$0 -w --- writer mode"
				echo "$0 -p --- presenation mode"
				echo "$0 -s --- spread sheet mode"
			fi

		fi
	fi
else
	echo "WPS Office is not installed to the /opt/software/wps-office Directory!"
	read -rp "Do you wish to go on ahead and install it to that directory? [Y/n]" install
	if [ $install == "n" ] ; then
		echo "okay, then, maybe I will see you later! "
		exit
	else
		if [ $arch == "x86_64" ] ; then
			wget -c "$package64"
			tar -xvf "$pack64"
			sudo mv "$dir64" wps-office && sudo mv wps-office /opt/software/
		elif [ $arch == "i686"] ; then
			wget -c "$package32"
			tar -xvf "$pack32"
			sudo mv "$dir32" wps-office && sudo mv wps-office /opt/software/
		else
			echo "That is not a valid architecture, or I am seeing an error of some kind. I do hope not, but it might happen."
		fi
	fi
fi


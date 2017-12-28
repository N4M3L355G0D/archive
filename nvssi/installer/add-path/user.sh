#! /bin/bash

user=`whoami`
file=".bashrc"
if [ $user == "root" ] ; then
	path="/root/"
elif [ $user != "root" ] ; then
	path="/home/$user/"
fi

read -rp "What path are you adding to you shell variable? " dir_path

if [ $dir_path == "q" ] ; then
	exit
else
	echo 'PATH=$PATH:'$dir_path >> $path$file
fi

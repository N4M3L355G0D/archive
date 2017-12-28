#! /bin/bash

if [ `whoami` != "root" ] ; then
 echo "Not SUDO/ROOT! BYE!"
 exit
fi

if [ "$1" == "--help" ] || [ "$1" == "-h" ] ; then
 echo "$0 <USER>"
fi
USER="$1"

if [ -z "$1" ] ; then
 read -rp "The user field was left blank. Please enter the USER : " USER
fi

sudo passwd "$USER"
sudo pdbedit -a -u "$USER"

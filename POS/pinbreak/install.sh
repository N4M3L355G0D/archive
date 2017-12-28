#! /bin/bash

#noguilinux
if [ `whoami` != "root" ] ; then
 echo "you are not root/sudo"
 exit
fi

cd ./install
if [ -e ./install.sh ] ; then
 if [ -f ./install.sh ] ; then
  bash ./install.sh
 else
  echo "install/install.sh is not a file"
  exit
 fi
else
 echo "install/install.sh does not exist"
fi

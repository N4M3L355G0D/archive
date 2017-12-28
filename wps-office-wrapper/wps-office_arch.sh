#! /bin/bash

if [ "$1" == "--auto" ] ; then
 yaourt -S wps-office
elif [ "$2" == "--stepper" ] ; then
 sudo rm -rf /temp/*
 yaourt -G wps-office
 cd wps-office
 makepkg
 sudo pacman -U ./wps-office-*.tar
 cd ..
 rm -rf wps-office
fi

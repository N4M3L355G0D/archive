#! /bin/bash

install_dir="/opt/software"
install_bin="/opt/bin"

if [ ! -e $install_bin ] ; then
        mkdir $install_bin
fi

if [ ! -e $install_dir ] ; then
	mkdir $install_dir
fi
cp -rf "$1" $install_dir
chmod +x "$2"/*
chmod -x "$2"/README.md

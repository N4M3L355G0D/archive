#! /bin/bash

echo "The 'Not Very Secure Simple Installer' "

help=""

if [ -z "$1" ] ; then
	echo $help
elif [ "$1" == "update" ] ; then
	cd ./retriever
	./cleaner.sh
	./retrieve.py
	cd ../installer
	./installer.py
	cd ../linker
	./sh-or-py.py
	echo "Done, if you do not have a the executable path set, use nvssi.sh addpath. Links have been cleaned. Please run ./nvssi.sh link to relink. This is a little security for you, should you wish to examine the software before using it."
	exit
elif [ "$1" == "addpath" ] ; then
	cd ./add-path
	./user.sh
	echo "The path has been added."
	exit
elif [ "$1" == "link" ] ; then
	cd ./linker
	./sh-or-py.py
	echo "Done Linking"
	exit
elif [ "$1" == "install" ] ; then
	cd ./installer
	./installer.py
	echo "Done installing from cache."
elif [ "$1" == "retrieve" ] ; then
	cd ./retriever
	./cleaner.sh
	./retrieve.py
	echo "Done retrieving."
fi

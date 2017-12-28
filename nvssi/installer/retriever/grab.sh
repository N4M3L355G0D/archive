#! /bin/bash
if [ -e ./grabbed ] ; then 
	cd ./grabbed && git clone "$1"
else
	mkdir ./grabbed && cd ./grabbed && git clone "$1"
fi

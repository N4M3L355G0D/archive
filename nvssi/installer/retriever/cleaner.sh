#! /bin/bash

file=./grabbed

if [ -e $file ] ; then
	read -rp "What do you want to remove? 
$(ls $file) : " check
	if [ $check == "q" ] ; then 
		exit
	elif [ $check == "all" ] ; then
		rm -rf $file/*
	else
		rm -rf $file/$check
	fi
fi

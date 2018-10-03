#! /usr/bin/env bash
function install(){
	if test `whoami` == "root" ; then
		cp -r etc/* /etc
		cp -r usr/* /usr
	else
		echo user is not root
	fi
}
install

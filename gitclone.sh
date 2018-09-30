#! /usr/bin/env bash
#NoGuiLinux
GITHUB_USER="deskos-xp"
repos=("forecast" "NvidiaCardSpecs" "serverTree" "autistic-resume" 'productW')
baseURL="https://github.com/$GITHUB_USER/"
function clone(){
	if test ! -d ".git" ; then
		for i in ${repos[@]} ; do
			cloneURL="$baseURL$i"
			printf "\e[1;5;32;40m%s\n\e[0;m" "$cloneURL"
			git clone "$cloneURL"
		done
	else
		printf "\e[1;31;40m%s\n\e[0;m" "please leave the repo directory that you are in currently before running this script"
	fi
}
clone

#! /usr/bin/env bash
#NoGuiLinux

function main(){
	ifile="resume.xml"
	template="$ifile"".template"
	pyfile="resume.py"
	
	if bash ./depCheck.sh "vim base64 xclip gzip" ; then
		if test -e "$template" ; then
			cp "$template" "$ifile"
			vim "$ifile"
			cat "$ifile" | gzip - | base64 - | xclip
			if test -e "$pyfile" ; then
				vim "$pyfile"
			else
				echo "$pyfile : does not exist"
			fi
		else
			echo "missing $template"
		fi
	else
		exit 1
	fi
}
main

#! /usr/bin/env bash
#NoGuiLinux
#gpg user
User="Karl Josef Wisdom III"
endCode="#stop"
function data(){
	acc=''
	message=''
	while test "$message" != "$endCode" ; do
		read -rp "TXT: " message
		acc="$acc\n""$message"
	done
	echo -e "$acc" | sed "s/$endCode$//"
}
function gzipData(){
	data | gzip - -f
}
function gpgData(){
	gzipData | gpg -e -r "$User"
}
function b64Data(){
	gpgData | base64 -
}
function dataToXclip(){
	b64Data | xclip
}

function dataD(){
	acc=''
	message=''
	while test "$message" != "$endCode"; do
		read -rp "B64: " message
		acc="$acc""$message"
	done
	echo -e "$acc" | sed "s/$endCode$//"
}
function b64DataD(){
	dataD | base64 -d -
}
function gpgDataD(){
	b64DataD | gpg -d -r "$User"
}
function gunzipData(){
	gpgDataD | gunzip -d - -f
}
if test "$1" == "-e" ; then
	dataToXclip
elif test "$1" == "-d" ; then
	gunzipData
fi

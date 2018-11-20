#! /usr/bin/env bash
ext=".avi"
function grab(){
	FILE="$1"
	if test "$FILE" == "" ; then
		while test "$FILE" == "" ; do
			read -rp "ofile: " FILE
		done
	fi
	ffmpeg -f x11grab -s \
		1366x768 -r 30 -i :0.0 \
		-f pulse -i default -ac 2 -acodec mp3 -q:v 0 \
		-vcodec libx264 -preset ultrafast \
		-pix_fmt yuv444p "$FILE""$ext"
}
grab "$@"

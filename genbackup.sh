#! /usr/bin/env bash
blb=`echo $1 | sed s\|'.tar.xz$'\|''\|g`
label="`basename $blb`"
oname="$blb$label.iso"
indir="$2"
echo $blb
echo $label
echo $oname
echo $indir

cat << EOF
genisoimage -v -J -r -V $label -o $oname $indir

where:
	-v -> be verbose
	-J -> generate a second super block so that windows
		based systems can read the iso
	-r -> enable rockridge format
	-V -> disk/iso label name
	-o -> filename for output
	$indir -> file/directory to be inserted into iso image

EOF
sleep 1s

genisoimage -v -J -r -V "$label" -o "$oname" "$indir"
sha512sum "$oname" > "$oname.hsh"

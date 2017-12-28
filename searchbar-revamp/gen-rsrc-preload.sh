#! /usr/bin/env bash

topd=""
datecode(){
	date +H%HM%MS%Smm%mdd%dyy%Y
}

mod() {
In="$1"
python << EOF
from math import pow

infile=int("$In")
dvd=4294967296
resolution_div=int(infile/dvd)
resolution_mod=infile % dvd
if resolution_mod != 0:
 resolution_div+=1
if resolution_div == 0:
 resolution_div+=1
print(resolution_div)
EOF
}

if test -d "$topd""resources" ; then
 if test ! -d "resources-iso" ; then
  mkdir "resources-iso"
 fi
 if test ! -d "resources-iso/part" ; then
  mkdir "resources-iso/part"
 fi
 if test ! -d "resources-iso/iso" ; then
  mkdir "resources-iso/iso"
 fi

 _date=`datecode`

 fname_tgz="resources-preloaded-$_date.tar.gz" 
 fname_sfs="resources-preloaded-$_date.tgz_squashfs"

 tar -zcvf $fname_tgz "$topd"resources/

 mksquashfs $fname_tgz $fname_sfs
 sz=`ls -l $fname_sfs | awk '{print $5}'`

 rm $fname_tgz

 split -n `mod $sz` --numeric-suffix=0 $fname_sfs resources-iso/part/r-$_date.sfs.
 for i in `ls resources-iso/part` ; do 
  genisoimage -v -J -r -UDF -V $i -o resources-iso/iso/$i.iso resources-iso/part/$i
 done
 rm -rf resources-iso/part
fi

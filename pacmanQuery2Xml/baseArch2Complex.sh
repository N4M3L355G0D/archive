#! /usr/bin/env bash
#NoGuiLinux
#get the pkg information and dump to pkgDetails/$PKGNAME.txt

pkgDetailsDir="./pkgDetails"
basePkgFile="../archlinux-prep/archbuild/base-pkgs.txt"
#get config options
config="b2c.xml"
# <scale-commnet> in the event that i want to scale this script for multiple instances, this is here for the for loop around
#that starts here
ver=1

function getConfigXML(){
	if test ! -e "$config" ; then
		echo "config does not exist"
		exit 1
	fi
	if test ! -f "$config" ; then
		echo "config is not a file!"
		exit 1
	fi
	pkgDetailsDir=`xmllint --xpath '/config/version[@version='"'$ver'"']/pkgDetailsDir/text()' "$config"`
	basePkgFile=`xmllint --xpath '/config/version[@version='"'$ver'"']/basePkgFile/text()' "$config"`
}
function main(){
	if test ! -e "$pkgDetailsDir" ; then
		mkdir "$pkgDetailsDir"
	fi

	for i in `cat "$basePkgFile"`; do 
		echo "$i"
	       	python rodTree.py -p "$i" | tee "$pkgDetailsDir/$i.xml" | xmllint --format - 
		if test $? != 0 ; then 
			break
		fi 
	done
}
#main
getConfigXML
main
#and ends here </scale-comment>

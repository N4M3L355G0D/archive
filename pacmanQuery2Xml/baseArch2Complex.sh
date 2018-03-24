#! /usr/bin/env bash
#NoGuiLinux
#get the pkg information and dump to pkgDetails/$PKGNAME.txt

pkgDetailsDir=""
basePkgFile=""
final=''
#get config options
config="b2c.xml"
# <scale-commnet> in the event that i want to scale this script for multiple instances, this is here for the for loop around
#that starts here
ver=1
function xmlGen(){
	printf "<master host='%s'>\n" "$HOST"
	cat "$pkgDetailsDir"/*.xml
	printf "</master>\n"

}
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
	final=`xmllint --xpath '/config/version[@version='"$ver"']/finalXML/text()' "$config"`
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
function extraProcessingAll(){
	cat master-packages.xml | xmllint --format - | fgrep -w 'pack' | grep -v '\&' | cut -f 2 -d'>' | cut -f1 -d'<' > "$final".txt
	cat master-packages.xml | xmllint --format - | fgrep -w 'conflict' | cut -f2 -d'>' | grep -v '&' | cut -f1 -d'<' > "$final"-conflicts.txt
	python3 extraprocessing.py -c "$final"-conflicts.txt -p "$final".txt -o "$final"-finalized.txt
}
getConfigXML
main
xmlGen > "$final"
rm -r "$pkgDetailsDir"
extraProcessingAll
#and ends here </scale-comment>

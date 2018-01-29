#! /usr/bin/env bash
#NoGuiLinux

#one liner
#echo $(lsblk /dev/sda /dev/sdb /dev/sdc -o NAME,SIZE -i | grep -w "sd[abc]" | sed 's/ /#/' | cut -f2 -d'#' | sed s/' '//g | sed s/'G'$/+/ | tr -d "\n" | sed s/'+'$//g) | bc
minor="abc"
disks=()
function setupPaths(){
	counter=0
	minors="`echo $minor | grep -o .`"
	for min in $minors ; do
		if test "$min" != "" ; then
			disks[$counter]="/dev/sd""`echo $min | tr -d "\n"`"
			counter=$(($counter + 1))
		fi
	done
}

function lsblkData(){
	lsblk ${disks[@]} -o NAME,SIZE -i
}

function grepper(){
	lsblkData | grep -w "sd[$minor]"
}

function filterSedHash(){
	grepper | sed s/' '/'#'/
}
function sliceF1KillSpace(){
	filterSedHash | cut -f2 -d'#' | sed s/' '//g
}

function convertG2Plus(){
	sliceF1KillSpace | sed s/'G'$/'+'/ | tr -d "\n" | sed s/'+'$//
}

function calculate(){
	setupPaths
	sizes=$(convertG2Plus)
	export IFS="+"
	firstNum=0
	calcs=('python3' 'python2' 'awk' 'bc' 'expr')
	calcPath=''
	for calc in ${calcs[@]} ; do
		binary=`which $calc 2> /dev/null`
		if test "$binary" != "" ; then
			calcPath=$binary
			#break
		fi
	done
	if test "$calcPath" != "" ; then
		if test "`basename $calcPath`" == "expr" ; then
			for num in $sizes ; do
				num=`echo $num | cut -f1 -d"." `
				firstNum=`expr $firstNum + $num`
			done
		elif test "`basename $calcPath`" == "python2" ; then
			firstNum=$(python2 <<< "sizes="$sizes" ; print sizes")
		elif test "`basename $calcPath`" == "python3" ; then
			firstNum=$(python3 <<< "sizes="$sizes"; print(sizes)")
		elif test "`basename $calcPath`" == "awk" ; then
			firstNum=$(awk "BEGIN {print $sizes;}")
		elif test "`basename $calcPath`" == "bc" ; then
			firstNum=$(echo "$sizes" | bc)
		fi
	else
		sizeFix=()
		counter=0
		for num in $sizes ; do
			sizeFix[$counter]=`echo $num | cut -f1 -d"."`
			counter=$(($counter + 1 ))
		done
		sz=`echo ${sizeFix[@]} | sed s/' '/' + '/g`
		firstNum=$(($sz))
	fi
	export IFS=" "
	printf "Size (GB) : %s\nCalculator: %s\n" $firstNum $calcPath
}
calculate

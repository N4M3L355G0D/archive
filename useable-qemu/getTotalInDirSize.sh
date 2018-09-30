#! /usr/bin/env bash
#noguilinux

function checkDeps(){
	export IFS=":"
	deps=("bc":"awk")
	exist="no"
	missing=()
	counter=0
	for dep in ${deps[@]} ; do
		exist="no"
		for i in $PATH ; do
			pth="$i"/"$dep"
			if test -e "$pth" && test -f "$pth" ; then
				exist="yes"
			fi
		done
		if test "$exist" == "no" ; then
			counter="`expr $counter + 1`"
			missing[$counter]="$dep"
		fi
	done
	export IFS=" "
	if test "${#missing[@]}" -gt 0 ; then
		echo -e "missing dependencies:\n`echo ${missing[@]} | tr " " "\n" | sed s/^/'\t'/`"
		exit 1
	fi	
}
checkDeps
ls -l |  grep -v total | awk '{print $5}' | tr "\n" "+" | sed 's/+$/\n/' | bc

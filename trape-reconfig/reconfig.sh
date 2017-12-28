#! /usr/bin/env bash
# change trape internal server address
# NoGuiLinux
# 11.7.2017
valid_ip() {
if [[ $1 =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] ; then
	OIFS=$IFS
	IFS='.'
	ip=($1)

	num=`echo ${#ip[@]}`
	x=0
	good=0
	while (( $x < $num )) ; do
		if test ${ip[$x]} -le 255 ; then
			good=`expr $good + 1`
		else
			echo "BAD"
			exit
		fi
		x=`expr $x + 1`
	done
	if test $good -eq 4 ; then
		echo "$1"
	else
		echo "BAD"
	fi
else
	echo "BAD"
fi
}

main() {
read -rp "What address was the original address used: " ORIG
check=`valid_ip $ORIG`
if test $check != "BAD" ; then
	read -rp "What address do you want to change the original address to: " NEW
	check=`valid_ip $NEW`
	if test $check != "BAD" ; then

		if test -d core ; then
			cd core
			for i in `ls -1 *.py` ; do 
				sed -i s\|"$ORIG"\|"$NEW"\|g $i 
	       		done
		fi
	else
		echo "New Address is not a correct address!"
	fi
else
	echo "Old Address is not a correct address"
fi

}
main

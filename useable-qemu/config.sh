#! /usr/bin/bash
#noguilinux
#this is the building ground to be used to build the configuration access options

cnfDb="useable-qemu_cnf.db"
table="qemuCnf"
cnf="useable-qemu.cnf"

function optArg(){
	read opt
	echo "$opt" | cut -f2 -d=
}

function textConfig(){
	if test -e "$cnf" ; then
		CD="`grep -w "iso" "$cnf" | optArg`"
		IMG="`grep -w "imgName" "$cnf" | optArg`"
		IMG_SIZE="`grep -w "imgSize" "$cnf" | optArg`"
		CMD="`grep -w "cmd" "$cnf" | optArg`"
		cpu="`grep -w "cpu" "$cnf" | optArg`"
		accel="`grep -w "accel" "$cnf" | optArg`"
		ram="`grep -w "ram" "$cnf" | optArg`"
		cores="`grep -w "cores" "$cnf" | optArg`"
		vga="`grep -w "vga" "$cnf" | optArg`"
		display="`grep -w "display" "$cnf" | optArg`"
		DB="`grep -w "DB" "$cnf" | optArg`"
		name="`grep -w "name" "$cnf" | optArg`"
		nicModel="`grep -w "nicModel" "$cnf" | optArg`"
		soundHW="`grep -w "soundHW" "$cnf" | optArg`"
		echo -e "$CD\n$IMG\n$IMG_SIZE\n$CMD\n$cpu\n$accel\n$ram\n$cores\n$vga\n$display\n$DB\n$name\n$nicModel\n$soundHW"
	else
		echo "textfile configuration does not exist"
		exit 1
	fi
}

function xmlConfig(){
 #this is just a placeholder
 #i still need to create the xml file/format to be used
 a=0

}

function getConfigOptions(){
	rows="$1"
	export IFS=","
	rowsAcc=''
	rowsValues=''
	rowsInput=''
	for i in ${rows[@]} ; do
		read -rp "`echo $i | cut -f1 -d" "`: " rowVal
		while test "$rowVal" == "" ; do
			read -rp "`echo $i | cut -f1 -d" "`: " rowVal
		done

		if test "$rowsValues" == "" ; then
			rowsValues='"'"$rowVal"'"'
		else
			rowsValues="$rowsValues"',"'"$rowVal"'"'
		fi
	done

	for i in ${rows[@]} ; do
		if test "$rowsInput" == "" ; then
			rowsInput="`echo "$i" | cut -f1 -d" "`"
		else
			rowsInput="$rowsInput"",""`echo "$i" | cut -f1 -d" "`"
		fi
	done
	export IFS=" "
	rowsInput="$table($rowsInput)"
	rowsValues="values(""$rowsValues"");"
	SQL="insert into $rowsInput $rowsValues"
	echo "$SQL"
}

function sqlite3ConfigGen(){
	export IFS=","
	rt="text"
	#this snippet will allow for semi-dynamic expansion
	rows=("CD $rt","IMG $rt","IMG_SIZE $rt","CMD $rt","cpu $rt","accel $rt","ram $rt","cores $rt","vga $rt","display $rt","DB $rt","name $rt","nicModel $rt","soundHW $rt")
	rowsAcc=''
	for i in ${rows[@]} ; do
		if test "$rowsAcc" == "" ; then
			rowsAcc="$i"
		else
			rowsAcc=$rowsAcc",""$i"
		fi
	done
	export IFS=" "
	SQL="create table if not exists $table ($rowsAcc, version INTEGER PRIMARY KEY AUTOINCREMENT);"
	if test ! -e "$cnfDb" ; then
		echo "$cnfDb : file does not exist creating it now!"
	else
		echo "$cnfDb : file exists! new conf version being created"
	fi
	sqlite3 "$cnfDb" "$SQL"
	sqlite3 "$cnfDb" "`getConfigOptions "$rows"`"

}

function sqlite3Config(){
	if test ! -e "$cnfDb" ; then
		counter=0
		read -rp "$cnfDb does not exist! Do you want to start the configuration wizard!? : " ANSWER
		while test "$ANSWER" != "no" && test "$ANSWER" != "yes" ; do
			if test "$counter" -le 10 ; then
				read -rp "$cnfDb does not exist! Do you want to start the configuration wizard![yes/no] : " ANSWER
			else
				echo "you must be having some trouble... maybe you should read the prompt [dUm6@55 617Ch]!"
				exit 1
			fi
			counter=`expr $counter + 1`
		done
		if test "$ANSWER" == "yes" ; then
			sqlite3ConfigGen
		else
			exit 1
		fi
	elif test "$1" == "newConf" ; then
		sqlite3ConfigGen
	else
		#by default, the latest version will be used
		#if failed configuration occurs from update, use versionOverride $versionNumber
		if test "$1" == "versionOverride" ; then
			latest="$2"
		else
			latest="`sqlite3 "$cnfDb" "select count(version) from qemuCnf"`"
		fi
		CD="`sqlite3 "$cnfDb" "select CD from $table where version=$latest"`"
		IMG="`sqlite3 "$cnfDb" "select IMG from $table where version=$latest"`"
		IMG_SIZE="`sqlite3 "$cnfDb" "select IMG_SIZE from $table where version=$latest"`"
		CMD="`sqlite3 "$cnfDb" "select CMD from $table where version=$latest"`"
		cpu="`sqlite3 "$cnfDb" "select cpu from $table where version=$latest"`"
		accel="`sqlite3 "$cnfDb" "select accel from $table where version=$latest"`"
		ram="`sqlite3 "$cnfDb" "select ram from $table where version=$latest"`"
		cores="`sqlite3 "$cnfDb" "select cores from $table where version=$latest"`"
		vga="`sqlite3 "$cnfDb" "select vga from $table where version=$latest"`"
		display="`sqlite3 "$cnfDb" "select display from $table where version=$latest"`"
		DB="`sqlite3 "$cnfDb" "select DB from $table where version=$latest"`"
		name="`sqlite3 "$cnfDb" "select name from $table where version=$latest"`"
		nicModel="`sqlite3 "$cnfDb" "select nicModel from $table where version=$latest"`"
		soundHW="`sqlite3 "$cnfDb" "select soundHW from $table where version=$latest"`"
		echo -e "$CD\n$IMG\n$IMG_SIZE\n$CMD\n$cpu\n$accel\n$ram\n$cores\n$vga\n$display\n$DB\n$name\n$nicModel\n$soundHW"
	fi
}

##access proof of concept
echo -e "sqlite3\n======"
sqlite3Config versionOverride 1
echo -e "textconfig\n==========="
textConfig

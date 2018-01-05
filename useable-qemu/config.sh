#! /usr/bin/bash
#noguilinux
#this is the building ground to be used to build the configuration access options

cnfDb="useable-qemu_cnf.db"
table="qemuCnf"
cnf="useable-qemu.cnf"
xmlCnf="useable-qemu_cnf.xml"

#globals
version=""
CD=""
IMG=""
IMG_SIZE=""
CMD=""
cpu=""
accel=""
ram=""
cores=""
vga=""
display=""
DB=""
name=""
nicModel=""
soundHW=""

#create a function that detects a blank global and attempt to get the missing global from another existing configuration

function header(){
	inString="$1"
python3 << EOF
print("-->","$inString","<--")
EOF
}

function optArg(){
	read opt
	echo "$opt" | cut -f2 -d=
}

function varDump(){
		if test "$1" != "" ; then 
			header "$1"
		fi
		echo -e "$CD\n$IMG\n$IMG_SIZE\n$CMD\n$cpu\n$accel\n$ram\n$cores\n$vga\n$display\n$DB\n$name\n$nicModel\n$soundHW"
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
		varDump "textConfig"
	else
		echo "textfile configuration does not exist"
		exit 1
	fi
}

function xmlConfig(){
	if test -e "$xmlCnf" ; then
		#get the latest version available
		if test "$1" == "versionOverride" ; then
			if test "$2" != "" ; then
				version="$2"
			else
				echo "\$2 cannot be blank"
			fi
		else
			version="`cat useable-qemu_cnf.xml | grep -w "<version" | tail -n1 | sed s/['><"\ \t']//g | cut -f 2 -d=`"
		fi
		CD="`xmllint --xpath "string(//version[@num='$version']/iso)" "$xmlCnf"`"
		IMG="`xmllint --xpath "string(//version[@num='$version']/imgName)" "$xmlCnf"`"
		IMG_SIZE="`xmllint --xpath "string(//version[@num='$version']/imgSize)" "$xmlCnf"`"
		CMD="`xmllint --xpath "string(//version[@num='$version']/cmd)" "$xmlCnf"`"
		cpu="`xmllint --xpath "string(//version[@num='$version']/cpu)" "$xmlCnf"`"
		accel="`xmllint --xpath "string(//version[@num='$version']/accel)" "$xmlCnf"`"
		ram="`xmllint --xpath "string(//version[@num='$version']/ram)" "$xmlCnf"`"
		cores="`xmllint --xpath "string(//version[@num='$version']/cores)" "$xmlCnf"`"
		vga="`xmllint --xpath "string(//version[@num='$version']/vga)" "$xmlCnf"`"
		display="`xmllint --xpath "string(//version[@num='$version']/display)" "$xmlCnf"`"
		DB="`xmllint --xpath "string(//version[@num='$version']/DB)" "$xmlCnf"`"
		name="`xmllint --xpath "string(//version[@num='$version']/name)" "$xmlCnf"`"
		nicModel="`xmllint --xpath "string(//version[@num='$version']/nicModel)" "$xmlCnf"`"
		soundHW="`xmllint --xpath "string(//version[@num='$version']/soundHW)" "$xmlCnf"`"
		#echo -e "$CD\n$IMG\n$IMG_SIZE\n$CMD\n$cpu\n$accel\n$ram\n$cores\n$vga\n$display\n$DB\n$name\n$nicModel\n$soundHW"
		varDump "xmlConfig"
	else
		echo "xml configuration file does not exist"
	fi
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
		varDump "sqlite3Config"
	fi
}

function selector(){
	#test if command exists
	commands=("sqlite3Config" "xmlConfig" "textConfig")
	command="$1"
	exist=""
	for i in ${commands[@]} ; do
		if test "$i" == "$command" ; then
			exist="yes"
		fi
	done
	if test "$1" == "xmlConfig" || test "$1" == "sqlite3Config" ; then
		if test "$exist" != "" ; then
			shift
			if test "$1" != "" || test "$1" != "textConfig" ; then
				versionOverrideYes="$1"
				if test "$2" != "" ; then
					if test "$versionOverrideYes" == "versionOverride" ; then
						versionOverride="$2"
					fi
				else
					echo "\$2 cannot be blank"
					exit 1
				fi
			"$command" "$versionOverrideYes" "$versionOverride"
			elif test "$command" == "textConfig" ; then
				"$command"
			fi
		else
			echo "no such command: $command"
		fi
	elif test "$1" == "textConfig" ; then
		textConfig
	else
		#auto-selector
		if test -e "$cnfDb" && test -f "$cnfDb"; then
				sqlite3Config
		elif test -e "$xmlCnf" && test -f "$xmlCnf" ; then
				xmlConfig
		elif test -e "$cnf" && test -f "$cnf" ; then
				textConfig
		else
			echo "no configuration files exist!"
		fi
	fi
}
#configuration style
tipe=xml
overrideVersionNum=1
selector "$tipe"Config versionOverride $overrideVersionNum
#remember need to create function that detects if a global is blank, or '', and attempt to detect another configuration file, and use the configuration option for the missing value from the other configuration, but if no other configuration options exist, fail with error, do not pass to useable-qemu.sh
##access proof of concept
#xmlConfig
#sqlite3Config versionOverride 1
#textConfig

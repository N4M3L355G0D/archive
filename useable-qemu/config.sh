#! /usr/bin/bash
#noguilinux
#this is the building ground to be used to build the configuration access options
cnfError="configuration error: option is blank"
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
		echo -e "CD#$CD\nIMG#$IMG\nIMG_SIZE#$IMG_SIZE\nCMD#$CMD\ncpu#$cpu\naccel#$accel\nram#$ram\ncores#$cores\nvga#$vga\ndisplay#$display\nDB#$DB\nname#$name\nnicModel#$nicModel\nsoundHW#$soundHW"
}

function textConfig(){
	if test -e "$cnf" ; then
		CD="`grep -w "CD" "$cnf" | optArg`"
		IMG="`grep -w "IMG" "$cnf" | optArg`"
		IMG_SIZE="`grep -w "IMG_Size" "$cnf" | optArg`"
		CMD="`grep -w "CMD" "$cnf" | optArg`"
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
	else
		echo "textfile:configuration file does not exist"
		exit 1
	fi
}

function latestVersionXml(){
	version="`cat useable-qemu_cnf.xml | grep -w "<version" | tail -n1 | sed s/['><"\ \t']//g | cut -f 2 -d=`"
}

function latestVersionSqlite3(){
	version="`sqlite3 "$cnfDb" "select count(version) from $table"`"
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
			latestVersionXml
		fi
		CD="`xmllint --xpath "string(//version[@num='$version']/CD)" "$xmlCnf"`"
		IMG="`xmllint --xpath "string(//version[@num='$version']/IMG)" "$xmlCnf"`"
		IMG_SIZE="`xmllint --xpath "string(//version[@num='$version']/IMG_Size)" "$xmlCnf"`"
		CMD="`xmllint --xpath "string(//version[@num='$version']/CMD)" "$xmlCnf"`"
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
	else
		echo "xml:configuration file does not exist"
		exit 1
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
			echo "sqlite3:configuration file does not exist"
			exit 1
		fi
	elif test "$1" == "newConf" ; then
		sqlite3ConfigGen
	else
		#by default, the latest version will be used
		#if failed configuration occurs from update, use versionOverride $versionNumber
		if test "$1" == "versionOverride" ; then
			version="$2"
		else
			latestVersionSqlite3
		fi
		CD="`sqlite3 "$cnfDb" "select CD from $table where version=$version"`"
		IMG="`sqlite3 "$cnfDb" "select IMG from $table where version=$version"`"
		IMG_SIZE="`sqlite3 "$cnfDb" "select IMG_SIZE from $table where version=$version"`"
		CMD="`sqlite3 "$cnfDb" "select CMD from $table where version=$version"`"
		cpu="`sqlite3 "$cnfDb" "select cpu from $table where version=$version"`"
		accel="`sqlite3 "$cnfDb" "select accel from $table where version=$version"`"
		ram="`sqlite3 "$cnfDb" "select ram from $table where version=$version"`"
		cores="`sqlite3 "$cnfDb" "select cores from $table where version=$version"`"
		vga="`sqlite3 "$cnfDb" "select vga from $table where version=$version"`"
		display="`sqlite3 "$cnfDb" "select display from $table where version=$version"`"
		DB="`sqlite3 "$cnfDb" "select DB from $table where version=$version"`"
		name="`sqlite3 "$cnfDb" "select name from $table where version=$version"`"
		nicModel="`sqlite3 "$cnfDb" "select nicModel from $table where version=$version"`"
		soundHW="`sqlite3 "$cnfDb" "select soundHW from $table where version=$version"`"
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
			exit 1
		fi
	fi
}

function cnfExists(){
	broken="$1"
	shift
	option="$1"
	cnfs=("$cnf" "$xmlCnf" "$cnfDb")
	result=''
	allNoExist="yes"
	for cf in ${cnfs[@]} ; do
		if test -e "$cf" && test -f "$cf" && test "$cf" != "$broken" ; then
			if test "$cf" == "$xmlCnf" ; then
				latestVersionXml
				result="`xmllint --xpath "string(//version[@num=$version]/$option)" "$xmlCnf"`"
				if test "$result" != "" ; then
					allNoExists="no"
					break
				fi
			elif test "$cf" == "$cnf" ; then
				result="`grep -w "$option" "$cnf" | cut -f2 -d=`"
				if test "$result" != "" ; then
					allNoExists="no"
					break
				fi
			elif test "$cf" == "$cnfDb" ; then
				latestVersionSqlite3
				result="`sqlite3 "$cnfDb" "select "$option" from $table where version=$version"`"
				if test "$result" != "" ; then
					allNoExists="no"
					break
				fi
			fi
		else
			allNoExists="yes"
		fi
	done
	if test "$allNoExists" == "yes" ; then
		result="$cnfError"
	fi
	echo "$result"
}

function detector(){
	err=''
	if test "$CD" == "" ; then
		CD="`cnfExists "$1" "CD"`"
		if test "$CD" == "$cnfError" ; then
			echo "$cnfError : CD"
			err="1"
		fi
	fi
	if test "$IMG" == "" ; then
		IMG="`cnfExists "$1" "IMG"`"
		if test "$IMG" == "$cnfError" ; then
			echo "$cnfError : IMG"
			err="1"
		fi
	fi
	if test "$IMG_SIZE" == "" ; then
		IMG_SIZE="`cnfExists "$1" "IMG_SIZE"`"
		if test "$IMG" == "$cnfError" ; then
			echo "$cnfError : IMG_SIZE"
			err="1"
		fi
	fi
	if test "$CMD" == "" ; then
		CMD="`cnfExists "$1" "CMD"`"
		if test "$CMD" == "$cnfError" ; then
			echo "$cnfError : CMD"
			err="1"
		fi
	fi
	if test "$cpu" == "" ; then
		cpu="`cnfExists "$1" "cpu"`"
		if test "$cpu" == "$cnfError" ; then
			echo "$cnfError : cpu"
			err="1"
		fi
	fi
	if test "$accel" == "" ; then
		accel="`cnfExists "$1" "accel"`"
		if test "$accel" == "$cnfError" ; then
			echo "$cnfError : accel"
			err="1"
		fi
	fi
	if test "$ram" == "" ; then
		ram="`cnfExists "$1" "ram"`"
		if test "$ram" == "$cnfError" ; then
			echo "$cnfError : ram"
			err="1"
		fi
	fi
	if test "$cores" == "" ; then
		cores="`cnfExists "$1" "cores"`"
		if test "$cores" == "$cnfError" ; then
			echo "$cnfError : cores"
			err="1"
		fi
	fi
	if test "$vga" == "" ; then
		vga="`cnfExists "$1" "vga"`"
		if test "$vga" == "$cnfError" ; then
			echo "$cnfError : vga"
			err="1"
		fi
	fi
	if test "$display" == "" ; then
		display="`cnfExists "$1" "display"`"
		if test "$display" == "$cnfError" ; then
			echo "$cnfError : display"
			err="1"
		fi
	fi
	if test "$DB" == "" ; then
		DB="`cnfExists "$1" "DB"`"
		if test "$DB" == "$cnfError" ; then
			echo "$cnfError : DB"
			err="1"
		fi
	fi
	if test "$name" == "" ; then
		name="`cnfExists "$1" "name"`"
		if test "$name" == "$cnfError" ; then
			echo "$cnfError : name"
			err="1"
		fi
	fi
	if test "$nicModel" == "" ; then
		nicModel="`cnfExists "$1" "nicModel"`"
		if test "$nicModel" == "$cnfError" ; then
			echo "$cnfError : nicModel"
			err="1"
		fi
	fi
	if test "$soundHW" == "" ; then
		soundHw="`cnfExists "$1" "soundHW"`"
		if test "$soundHW" == "$cnfError" ; then
			echo "$cnfError : soundHW"
			err="1"
		fi
	fi
	if test "$err" == "1" ; then
		exit 1
	fi
}

function cnfType(){
	if test "$1" == "textConfig" ; then
		echo "$cnf"
	elif test "$1" == "xmlConfig" ; then
		echo "$xmlCnf"
	elif test "$1" == "sqlite3Config" ; then
		echo "$cnfDb"
	else
		echo "fail:1"
	fi
}
function getConfig(){
	availa=("xml" "sqlite3" "text")
	exist="no"
	if test "$1" != "style" ; then
		#configuration style auto
		selector
	else
		if test "$2" != "" ; then
			for st1le in ${availa[@]} ; do
				if test "$st1le" == "$2" ; then
					exist="yes"
				fi
			done
			if test "$exist" == "no" ; then
				echo "invalid configuration format"
				exit 1
			else
				tipe="$2"
			fi
		else
			echo "\$2 cannot be blank"
		fi
		overrideVersionNum=1
		#selector command 'textConfig' ignores arguments
		#'versionOverride' is the keyword to override the latest version behavior
		selector "$tipe"Config versionOverride $overrideVersionNum
		
		#this detects a blank configuration entry and attempts to fix the issue
		conf="`cnfType "$tipe"Config`"
		if test "$conf" != "fail:1" ; then
			detector "$cnf"
		else
			exit 1
		fi
	fi
	
	#dump globals to stdout
	if test "$?" != "1" ; then
		data="`varDump "$tipe"Config`"
		dataStripSrc="$(echo -e "$data" | tail -n `expr $(wc -l <<< $data) - 1`)"
		echo -e "$dataStripSrc"
	fi
	#remember need to create function that detects if a global is blank, or '', 
	#and attempt to detect another configuration file, and use the configuration 
	#option for the missing value from the other configuration, but if no other 
	#configuration options exist, fail with error, do not pass to useable-qemu.sh
}

getConfig "$@"

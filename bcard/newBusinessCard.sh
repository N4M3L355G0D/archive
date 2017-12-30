#! /usr/bin/env bash
# NoGuiLinux
# a new kind of business card
# now featuring a resume

#need this global so other functions can see this
DB="bcard.db"
parse="parser.py"
#check for required dependencies
function depCheck(){
	cmds=("sqlite3" "base64" "python3" "gunzip")
	notInstalled=()
	counter=0
	for cmd in ${cmds[@]} ; do
		depInstalled="no"
		export IFS=":"
		for pth in $PATH ; do 
			exist="`ls "$pth/$cmd" |& grep -v "ls: cannot access"`"
			if test "$exist" != "" ; then
				depInstalled="yes"
			fi			
		done
		if test "$depInstalled" == "no" ; then
			notInstalled[$counter]=$cmd
		fi
		counter=`expr $counter + 1`
		export IFS=" "
	done
	if test "${#notInstalled[@]}" -gt 0 ; then
		echo -e "There seems to be some missing dependencies\n(they might just not be in your \$PATH):"
		for dep in ${notInstalled[@]} ; do
			echo -e "\t$dep"
		done
		exit 1
	fi
}

function dbGen(){
	data="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
5QsAoAAA"
	echo "$data" | base64 -d - | gunzip - > "$DB"
}

function checkForFile(){
	if test ! -e "$1" ; then
		if test "$1" == "$DB" ; then
			dbGen
		else
			echo "no such file or directory: $1"
			exit 1
		fi
	fi
}

function noguilinux(){
	#bcard fields are as follows
	#name,email,phone,version
	#create table if not exists bcard(name text,email text,phone text,version INTEGER PRIMARY KEY AUTOINCREMENT)
	table="bcard"
	version="1"
#due to the EOF works, it is best to keep  this set of commands aligned in the manner as below	
cat << EOF
Contact Information
===================
name: `sqlite3 "$DB" "select name from $table where version=$version;"`
email: `sqlite3 "$DB" "select email from $table where version=$version;"`
phone: `sqlite3 "$DB" "select phone from $table where version=$version;"`
EOF
}

function needLinuxAdmin(){
	if test "`uname -s`" == "Linux" ; then
		echo "yes"
	else
		echo "no"
	fi
}

function bars(){
python3 << EOF
string="$1"
stringLen=len(string)
out='='*stringLen
print(out,string,out,sep="\n")
EOF
}

function education(){
	bars "Education"
	export IFS="#"
	for i in `sqlite3 "$DB" "select rowid from education;" | tr "\n" "#"` ; do
		uni=`sqlite3 "$DB" "select uni from education where rowid=$i;"`
		date=`sqlite3 "$DB" "select date from education where rowid=$i;"`
		degree=`sqlite3 "$DB" "select degree from education where rowid=$i;"`
		echo -e "$uni - $date\n\t$degree"
	done
	export IFS=" "
}

function workXP(){
	bars "Work Experience"
	export IFS="#"
	for i in `sqlite3 "$DB" "select rowid from workXP;" | tr "\n" "#"` ; do
		cert=`sqlite3 "$DB" "select employer from workXP where rowid=$i;"`
		title=`sqlite3 "$DB" "select title from workXP where rowid=$i;"`
		date=`sqlite3 "$DB" "select date from workXP where rowid=$i;"`
		desc=`sqlite3 "$DB" "select desc from workXP where rowid=$i;"`
		echo -e "$cert - $Date\n\t$title"
		for x in $desc; do
			echo -e "\t - $x"
		done
	done
	export IFS=" "
}

function certifications(){
	bars "Certifications"
	export IFS="#"
	for i in `sqlite3 "$DB" "select rowid from certifications;" | tr "\n" "#"` ; do
		cert=`sqlite3 "$DB" "select cert from certifications where rowid=$i;"`
		Date=`sqlite3 "$DB" "select date from certifications where rowid=$i;"`
		desc=`sqlite3 "$DB" "select desc from certifications where rowid=$i;"`
		echo -e "$cert - $Date\n\t$desc"
	done
	export IFS=" "
}

function summaryOfSkills(){
	bars "Summary Of Skills"
	export IFS="#" 
	for i in `sqlite3 "$DB" "select subcat from summaryOfSkills;" | tr "\n" "#"` ; do
       		sqlite3 "$DB" "select element from $i" | sed s\|^\|"$i - "\| 
	done 
	export IFS=" "
}

function parserCode(){
cat << EOF
#! /usr/bin/python3


import argparse

try:
    parser=argparse.ArgumentParser()
    parser.add_argument("-b","--business-card",action="store_true")
    parser.add_argument("-s","--summary-of-skills",action="store_true")
    parser.add_argument("-c","--certifications",action="store_true")
    parser.add_argument("-w","--work-xp",action="store_true")
    parser.add_argument("-e","--education",action="store_true")
    parser.add_argument("-r","--resume",action="store_true")
    options=parser.parse_args()

    resString=[]
    if options.business_card:
        resString.append("#bc")
    
    if options.summary_of_skills:
        resString.append("#sok")
    
    if options.certifications:
        resString.append("#c")
    
    if options.work_xp:
        resString.append("#wxp")
    
    if options.education:
        resString.append("#e")
    
    if options.resume:
        resString=["#resume"]
    
    if len(resString) == 0:
        print("please look at --help/-h")
    else:
        print(''.join(resString))
except:
    print('err')
EOF
}

function parser(){
	python3 "$parse" "$@"
}

function checkForFile(){
	EXISTS_MSG=": file/directory exists -- quitting to prevent damage!"
	if test ! -e "$1" ; then
		if test "$1" == "$DB" ; then
			dbGen
		elif test "$1" == "$parse" ; then
			parserCode > "$parse"
		else
			echo "no such file or directory: $1"
			exit 1
		fi
	else
		echo "$1" "$EXISTS_MSG"
		exit 1
	fi
}

function cleanup(){
	if test -e "$DB" ; then
		rm "$DB"
	fi

	if test -e "$parse" ; then
		rm "$parse"
	fi
	exit 1
}

function main(){
	MESSAGE_COMMON="please look at --help/-h"
	depCheck
	#check to make sure required filenames do not already exist, if they already do, fail in attempt to prevent damage to existing work
	checkForFile "$DB"
	checkForFile "$parse"
	#sometimes test is not good enough; using a builtin
	if test "`needLinuxAdmin`" == "yes" ; then
		if [ ! -z "$1" ] ; then
			options="`parser "$@"`"
			if test "$options" == "err" ; then
				cleanup
			elif test "$options" != "$MESSAGE_COMMON" ; then
				export IFS="#"
				run=0
				for i in $options ; do
					case $i in
						'resume')
							noguilinux
							summaryOfSkills
							certifications
							workXP
							education
							run=1
							break
							;;
						'e')
							education
							run=1
							;;
						'wxp')
							workXP
							run=1
							;;
						'c')
							certifications
							run=1
							;;
						'sok')
							summaryOfSkills
							run=1
							;;
						'bc')
							noguilinux
							run=1
							;;
					esac
				done
				export IFS=" "	
				if test "$run" == "0" ; then
					parser -h | sed s\|"err"\|""\|
					cleanup
				fi
	
			else
				echo "$MESSAGE_COMMON"
				cleanup
			fi
		else
			echo "$MESSAGE_COMMON"	
			cleanup
		fi
	fi	
	cleanup
}

main "$@"

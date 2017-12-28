#! /usr/bin/env bash
#noguilinux
#a network spammer
if test `whoami` == "root" ; then
 #primary config
 conf_db='conf.db'
 #alternative config if primary does not exist
 conf_txt='conf.txt'
 count=0
 pid=''
 if test -f "$conf_db" ; then
 	version="`sqlite3 "$conf_db" "select count(version) as count from conf;"`"
	read -rp "override version: " override
	if test "$override" != "n" ; then
		if test "$override" != "" ; then
			version="$override"
		fi
	fi
 	UP="`sqlite3 "$conf_db" "select UP from conf where version=$version"`"
 	DB="`sqlite3 "$conf_db" "select DB from conf where version=$version"`"
 elif test -f "$conf_txt" ; then
 	UP="`grep -w 'UP' "$conf_txt" | cut -f2 -d=`"
 	DB="`grep -w 'DB' "$conf_txt" | cut -f2 -d=`"
 else
 	echo "both $conf_db and $conf_txt configuration files do not exist... I cannot continue this assault... bye!"
	exit 1
 fi
 
 if test -f "$DB" ; then
 	rm "$DB"
 fi
 
 while test "$count" -lt "$UP"  ; do
 	echo $count - worker deployed to spread the nasty\'s
 	python2 dping.py &> /dev/null &
 	pid=$pid":"$!
 	count=`expr $count + 1`
 done
 
 #store pid for kills
 sqlite3 "$DB" "create table if not exists workers (rowid INTEGER PRIMARY KEY AUTOINCREMENT,pid int);"
 export IFS=':'
 for i in $pid ; do
  if test "$i" != '' ; then
   sqlite3 "$DB" "insert into workers (pid) values("$i");"
  fi
 done
else
 echo "you are not root"
fi

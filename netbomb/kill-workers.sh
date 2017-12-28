#! /usr/bin/env bash
#noguilinux
#kill all workers listed in $DB created by deploy-worker.sh
if test `whoami` == "root" ; then
 #primary config
 conf_db='conf.db'
 #alternative config if primary does not exist
 conf_txt='conf.txt'
 if test -f "$conf_db" ; then
	#version allows for multiple configuration versions to be installed in conf.db
	#the below line allows for the use of the latest version
 	version="`sqlite3 "$conf_db" "select count(version) as count from conf;"`"
	read -rp "override version: " override
	if test "$override" != "n"; then
		if test "$override" != "" ; then
			version="$override"
		fi
	fi
 	DB="`sqlite3 "$conf_db" "select DB from conf where version=$version"`"
 elif test -f "$conf_txt" ; then
 	DB="`grep -w 'DB' "$conf_txt" | cut -f2 -d=`"
 else
 	echo "both $conf_db and $conf_txt configuration files do not exist... I cannot kill this assault... bye!"
	exit 1
 fi

 for i in `sqlite3 $DB 'select pid from workers;'` ; do
  echo "killing worker PID: $i"
  kill -9 $i
 done
 rm "$DB"
else
 echo "you are not root"
fi

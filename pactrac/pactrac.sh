#! /bin/bash

deps() {
	expac %o -l "\n"
}

sqlite3 deps.db "create table if not exists deps ( pkg string, num int );"
sqlite3 deps.db "create table if not exists errors ( pkg string, num int );"

num=`sqlite3 deps.db "select num from deps desc;" | tail -n 1`
if test "$num" == "Error: no such table: deps" ; then
 num=0
fi

all(){
 for i in `deps` ; do
  package="$i"
  installed=`sqlite3 deps.db "select pkg from deps where pkg='""$package""'"`
  if test "$installed" != "$package" ; then
   yaourt --noconfirm -S "$package"
   if test "$?" == "0" ; then
    sqlite3 deps.db "insert into deps (pkg,num) select '""$package""' , "$num" where not exists(select pkg from deps where pkg='""$package""');"
    num=`expr $num + 1`
   else
    echo "$package gave an error - an entry will be made in deps.db under table errors"
    sqlite3 deps.db "insert into errors (pkg,num) select '""$package""' , "$num" where not exists(select pkg from deps where pkg='""$package""');"
   fi
  else
   echo "$package installed already!"
  fi
 done
}

single() {
 if test "$1" == '-force' ; then
	 force="--force"
	 shift
 fi

 for i in "$1" ; do
  package="$i"
  installed=`sqlite3 deps.db "select pkg from deps where pkg='""$package""'"`
  if test "$installed" != "$package" ; then
   yaourt --noconfirm -S "$package" $force
   if test "$?" == "0" ; then
    sqlite3 deps.db "insert into deps (pkg,num) select '""$package""' , "$num" where not exists(select pkg from deps where pkg='""$package""');"
    num=`expr $num + 1`
   else
    echo "$package gave an error - an entry will be made in deps.db under table errors"
    sqlite3 deps.db "insert into errors (pkg,num) select '""$package""' , "$num" where not exists(select pkg from deps where pkg='""$package""');"
   fi
  else
   echo "$package installed already!"
  fi
 done
}

if test "$1" == "" ; then
	all
elif test "$1" == "--force" ; then
	single -force "$1"
else
	single "$1"
fi

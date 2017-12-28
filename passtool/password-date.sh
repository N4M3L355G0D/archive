#! /bin/bash

CMD=md5sum
five=`date +%F\ %H:%M | cut -f2 -d:`

x=1

if [ "$1" == "timer" ] ; then
 while (( $x == 1 )) ; do
 five=`date +%F\ %H:%M | cut -f2 -d:`
 echo `date +%F\ %H:%M``whoami`
  if [ `python3 ./test5.py -5 $five` == "True" ] ; then
   $CMD <<< `date +%F\ %H:%M``whoami`
   echo `date +%F\ %H:%M``whoami`
   exit
  fi
 done
elif [ "$1" == "ahead" ] ; then
 if [ `python3 ./test5.py -5 $2` == "True" ] ; then
  $CMD <<< "$3""$4"
 fi
else
 echo "$0 timer
$0 ahead <min> <date +%F\ %H:%M formatted date string><user>"
fi




#! /bin/bash

USER=carl
if [ -z "$1" ] ; then
 prog="conky"
else
 prog="$1"
fi

PROC() {
 prog="$1"
 ps -eo pid,cmd | grep $prog | grep -v grep | grep -v "$0"
}
PID=`PROC "$prog" | awk '{print \$1}'`
procNum=`PROC $prog | wc -l`

if (( $procNum > 1 )) ; then
 while [ ! -z "$PID" ] ; do
  read -rp "there are multiple pid's with that process name. would you like to kill `echo -e "$PID" | tail -n 1` [y/n]" answer
  if [ "$answer" != "n" ] ; then
   kill `echo -e "$PID" | tail -n 1`
  fi
  PID=`PROC "$prog" | awk '{print \$1}'`
  procNum=`PROC $prog | wc -l`
 done
elif (( $procNum == 1 )) ; then
 kill "$PID"
elif (( $procNum == 0 )) ; then
 echo "no PID found for that process"
fi

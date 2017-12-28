#! /bin/bash


CONFIG="./config.cfg"
SEP=":"
R_PASSWORD=`cat $CONFIG | grep 'R_PASSWORD' | cut -f2 -d$SEP`
x=0
user_num=`python3 ./datasplit.py -s "$(bash ./getusers.sh)" | wc -l`
LOGS=`cat $CONFIG | grep 'LOGS' | cut -f2 -d$SEP`
CMD=`cat $CONFIG | grep 'CMD' | cut -f2 -d$SEP`
EXCLUDE=`cat $CONFIG | grep 'EXCLUDE' | cut -f2 -d$SEP`

## for the service option, when it is added use
while (( $x <= $user_num )) ; do
 USER=`python3 ./datasplit.py -s "$(bash ./getusers.sh)" | grep -w "$x" | sed s\|"$x "\|\|g`
 if [ `python3 ./test5.py -5 $(date +%M)` == "True" ] ; then
  PASSWORD=`$CMD <<< "$(date +%F\ %H:%M)""$USER" | sed s\|" -"\|\|g`
 else
  echo "not that time yet... bye"
  exit
 fi
# echo "$0 timer
# $0 ahead <min> <date +%F\ %H:%M formatted date string><user>"

 if [ "$USER" == "root" ] ; then
  echo "USER:SKIP [ CHECK ]"
 elif [ "$USER" == "$EXCLUDE" ] ; then
  echo "USER:SKIP [ CHECK ]"
 elif [ -z "$USER" ]  ; then
  echo "USER_NONE [ CHECK ]"
 else
  if [ "$USER" != "$USER_NONE" ] || [ "$USER" != "$USER_SKIP" ] ; then
   su -c "echo $USER:$PASSWORD | chpasswd" <<< $R_PASSWORD
   echo $USER:$PASSWORD
   if [ -e "$LOGS" ] ; then
    echo "$USER:$PASSWORD" > "$LOGS"
   elif [ ! -e "$LOGS" ] ; then
    echo "$USER:$PASSWORD" >> "$LOGS"
   fi
  fi
 fi
 x=`echo $x + 1 | bc`
done

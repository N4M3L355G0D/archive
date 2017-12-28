#! /bin/bash

NIC="$2"
admin=sudo
PASS="$3"
HELP="echo $2 [--track|--stop-connection|--reset-counters] <NIC> <sudo password>"


if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then
 echo "$HELP"
 exit
fi

if [ -z "$PASS" ] ; then
 echo "No password"
 exit
fi

if [ -z "$NIC" ] ; then
 NIC=wlo1
fi



counter() {

y=1
x=0

TIME=1s

while (( $y != $x )) ; do
 data=`ifconfig $NIC | grep RX | grep -v errors | cut -f2 -d\( | cut -f1 -d\)`
 echo "$data"
 sleep $TIME
done
 }

stop_connection() {
$admin ifconfig $NIC down <<< "$PASS"
}

reset_counters() {

$admin -S ifconfig  "$NIC" down <<< "$PASS"
driver=`ethtool -i "$NIC" | grep driver | cut -f2 -d" "`
if [ $driver == "wl0" ] ; then
 driver="wl"
fi
$admin -S modprobe -r "$driver" <<< "$PASS"
$admin -S modprobe -i "$driver" <<< "$PASS"
#$admin -S ifconfig "$NIC" up <<< "$PASS"
 }

main() {
if [ "$1" == "--track" ] ; then
 counter
elif [ "$1" == "--stop-connection" ] ; then
 stop_connection
elif [ "$1" == "--reset-counters" ] ; then
 reset_counters
else
 echo "$2 [--track|--stop-connection|--reset-counters] <NIC> <sudo password>"
fi
}

main "$1"

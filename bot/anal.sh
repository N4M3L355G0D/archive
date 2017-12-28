interface=`iw dev | grep Interface | tail -n 1 | awk '{print $2}'`

begin(){
 sudo systemctl stop NetworkManager
 echo $interface
  
 iwlist "$interface" scanning |& tee -a data.txt
 
 nmcli dev wifi |& tee -a data.txt
 
 sudo ifconfig "$interface" down
 sudo iwconfig "$interface" mode monitor
 sudo ifconfig "$interface" up
 sudo airodump-ng -i "$interface" |& tee -a data.txt
}

cleanup(){
 ## if networkmanager running, stop it
 ## sudo systemctl stop Network Manager
 sudo ifconfig "$interface" down
 sudo iwconfig "$interface" mode managed
 sudo ifconfig "$interface" up
 reset
 sudo systemctl start NetworkManager
}

helpF(){
cat << EOF
$0 syntax:
 $0 mon - run scanner
 $0 restore - restore interfaces to managed mode

EOF
}

if [ "$1" == "mon" ] ; then
 begin
elif [ "$1" == "restore" ] ; then
 cleanup
else
 helpF
fi

#! /bin/bash

check_root(){
if [ `whoami` != "root" ] ; then
 echo "You are not ROOT!"
 exit
fi
}

main() {
 pATH="/sys/bus/pci/drivers/ehci-pci"

 controller1=`ls -1 "$pATH" | head -n 1`

 if [ ! -z "$controller1" ] ; then
  echo "$controller1" > "$pATH/unbind"
  echo "$controller1" > "$pATH/bind"
 fi
}
check_root
main

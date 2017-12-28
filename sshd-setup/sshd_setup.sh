#! /bin/bash

function setup {
config_status=`cat /etc/ssh/sshd_config | grep "#X11Forwarding" | cut -f2 -d" "`
config_path="/etc/ssh/sshd_config"
if [ "$config_status" == "no" ] ; then
 cat $config_path | sed s/"#X11Forwarding no"/"X11Forwarding yes"/g > sshd_config
 sudo cp ./sshd_config $config_path
 sudo systemctl restart sshd
else
 echo "It looks like this file has already been altered."
fi

}

setup

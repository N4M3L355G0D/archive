#! /bin/bash

function install {
if [ "$(vncserver -list | grep -w ":1" | cut -f2 -d: | sed s/"\t\t"/":"/g | cut -f1 -d:)" == "1" ] ; then
 sudo systemctl stop vncserver
 sudo systemctl start vncserver
 echo "It looks like you already have a running version of VNCserver, so nothing needs to be done."
 exit
fi


PATH_CONFIG="/etc/systemd/system/vncserver.service"
PATH_ORIG="/lib/systemd/system/vncserver.service"
sudo cp $PATH_ORIG $PATH_CONFIG

vncserver :1
vncserver -kill :1

cat $PATH_CONFIG | sed s/"User="/"User=$(whoami)"/g | sed s/'ExecStartPre='/'#ExecStartPre='/g | sed s/"vncserver -fg %i"/"vncserver :1"/g | sed s/"vncserver -kill %i"/"vncserver -kill :1"/g > vncserver.service

cat /etc/X11/xinit/xinitrc | sed s/'twm'/'exec xfce4-session'/g > xinitrc
sudo cp ./xinitrc /etc/X11/xinit/xinitrc

cat ~/.vnc/xstartup | sed s/"twm"/"exec xfce4-session"/g > xstartup
cp ./xstartup ~/.vnc/xstartup

sudo cp ./vncserver.service $PATH_CONFIG
sudo systemctl enable vncserver
vncpasswd
sudo systemctl start vncserver
rm ./xinitrc ./xstartup ./vncserver.service
}

install

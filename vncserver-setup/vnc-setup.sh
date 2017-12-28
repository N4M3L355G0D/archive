#! /bin/bash

function install {
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
}

install

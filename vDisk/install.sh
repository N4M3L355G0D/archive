#! /bin/bash

sudo mkdir /opt/vdisk
sudo cp vdisk.* /opt/vdisk/
sudo touch /opt/vdisk/
read -rp "What is your 'sudo' password? : " password
su -c echo $password > /opt/vdisk/.password
sudo ln -s /opt/vdisk/vdisk.gui /usr/bin/vdisk
sudo chmod +x /opt/vdisk/*

#! /bin/bash

#setup samba file server

sudo cp /etc/samba/smb.conf.default /etc/samba/smb.conf
sudo vim /etc/samba/smb.conf
sudo systemctl enable sshd smbd nmbd



#! /bin/bash

CARD=`nmcli dev | grep -w wifi | head -n1 | cut -f1 -d" "`

sudo systemctl stop NetworkManager && sudo macchanger -r $CARD && sudo systemctl start NetworkManager

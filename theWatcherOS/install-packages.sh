#! /usr/bin/env bash

python3 whichIsIt.py > installed.txt
grep "OFFICIAL" installed.txt | cut -f1 -d: > official.txt

#make container
mkdir container
sudo pacstrap -i container base base-devel $(cat official.txt)

grep "AUR" installed.txt | cut -f1 -d: > aur.txt

cp aur.txt yaourt-install.sh install-aur.sh container/root/

#boot container
#sudo systemd-nspawn -b -D container
#log in to root
#run rootlogin.sh
##run containerlogin.sh

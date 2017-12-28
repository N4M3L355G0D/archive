#! /bin/bash

#-g for gid 0, root
#-u for uid 0, root
#-o for non-unique, which applies only when -u is used
#-s for shell
#-m to create home directory, which will default to /home
sudo useradd -g 0 -m admin -u 0 -o -s /bin/bash 

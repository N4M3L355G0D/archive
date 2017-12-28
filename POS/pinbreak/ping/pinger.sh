#! /usr/bin/bash

host=`cat ./pinbreak.cfg | fgrep -w hostname | cut -f2 -d=`

ping -c 1 "$host" | ./pingfilter.awk | cut -f2 -d" "

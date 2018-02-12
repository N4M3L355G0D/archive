#! /bin/bash

config="./wireless-tools.cfg"
log_prefix=`cat $config | grep -w log_prefix | cut -f2 -d=`
final="essid_$(date).txt"
view_cmd=""
process_log() {
 sub0=essid.txt
 sub1=essid.num
 log="$log_prefix.txt"
 cat "$log" | grep ESSID | uniq > "$sub0"
 cat "$sub0" | sed s\|"ESSID:"\|\|g | sed s\|\Wireless\|\|g | sed s\|\"\|\|g | sed s\|" "\|\|g > "$sub1"
 sort "$sub1" | uniq >> "$final"
 if [ "$1" == "--dos-format" ] ; then
  unix2dos "$final"
 fi
}

view_final() {
 echo "     #  Router" ; cat "$final" | nl > "$final".1
 rm "$final" && mv "$final".1 "$final"
 if [ "$1" == "--less" ] ; then
  view_cmd="less "
 else
  view_cmd="cat "
 fi
 $view_cmd "$final"
}

process_log "$2"
view_final "$1"

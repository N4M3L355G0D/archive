#! /bin/bash

config="./wireless-tools.cfg"
prefix=`cat $config | grep -w prefix | cut -f2 -d=`
CMD_FILE="$(pwd)/command.txt"
x=`cat "$CMD_FILE" | head -n 1 `

log_prefix=`cat $config | grep -w log_prefix | cut -f2 -d=`

LOG="./$log_prefix.txt"
LOG2="./$log_prefix-$(date).txt"
ESSID="$prefix"

nic_num=`iw dev | grep Interface | sed s\|"Interface "\|"@"\|g | cut -f2 -d@ | wc -l`
if (( $nic_num > 1 )) ; then
 read -rp "You have more than one wireless interface! Which of the following do you want to use?
`iw dev | grep Interface | sed s\|"Interface "\|"@"\|g | cut -f2 -d@`" WNIC
else
 WNIC=`iw dev | grep Interface | sed s\|"Interface "\|"@"\|g | cut -f2 -d@`
fi

if [ "$1" == "--alt-prefix" ] ; then
 if [ ! -z "$2" ] ; then
  ESSID="$2"
 else
  read -rp "What ESSID || blank? " ESSID
 fi
fi

if [ -e $LOG ] ; then
	echo "There is already a Log... Moving Current Log to 
$LOG2, and making a new one."
	mv "$LOG" "$LOG2"
	touch "$LOG"
fi

if [ ! -e "$CMD_FILE" ] ; then
	echo "run" > "$CMD_FILE"
fi

x=`cat "$CMD_FILE" | head -n 1 `

while [ "$x" == "run" ] ; do
	x=`cat command.txt | head -n 1 `
	echo "=========== $(date) ==============" | tee -a "$LOG"
	nmcli dev wifi | grep "$ESSID" >> "$LOG"
        iwlist $WNIC scanning | grep "$ESSID" >> "$LOG"
done

#! /bin/bash
PATH=$PATH:/usr/local/bin:$HOME/.local/bin

CONFIG_BASE=$HOME/.local/etc

CFG=clock.cfg
path=$HOME/.local
stopper=`cat $CONFIG_BASE/$CFG | fgrep stopper | cut -f2 -d=`
tmp_path=$path/tmp
config_delay=`cat $CONFIG_BASE/$CFG | fgrep delay | cut -f2 -d=`

SNOOZE=`cat $CONFIG_BASE/$CFG | fgrep snooze | cut -f2 -d=`

EXIT=`offsnooze`
EXIT2=`echo $EXIT | cut -f1 -d" "`
SNOOZE=`echo $EXIT | cut -f2 -d" "`

if [ "$EXIT2" == "OFF" ] ; then
 echo "stop=stop" > $tmp_path/$stopper
 sleep $config_delay
 echo "stop=start" > $tmp_path/$stopper
elif [ "$EXIT2" == "SNOOZE" ] ; then
 while [ "$EXIT2" == "SNOOZE" ] ; do
  echo "stop=stop" > $tmp_path/$stopper
  sleep $SNOOZE
  echo "stop=start" > $tmp_path/$stopper
  xterm -e /bin/bash $path/bin/timer.sh &
  EXIT=`offsnooze`
  EXIT2=`echo $EXIT | cut -f1 -d" "`
  SNOOZE=`echo $EXIT | cut -f2 -d" "`m
 done
 echo "stop=stop" > $tmp_path/$stopper
 sleep $config_delay
 echo "stop=start" > $tmp_path/$stopper
fi


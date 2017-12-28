#! /bin/bash
PATH=$PATH:/usr/local/bin:$HOME/.local/bin

CONFIG_BASE=$HOME/.local/etc
CONFIG=$CONFIG_BASE/clock.cfg
tmp_path=$HOME/.local/tmp
path=$HOME/.local
stopper=`cat $CONFIG | fgrep stopper | cut -f2 -d=`

stopfile=$tmp_path/$stopper


get_time(){
hr=$(expr `date +%H` - 12)
min=$(date +%M)

if (( `date +%H` < 13 )) ; then
 hr=$(date +%H)
elif (( 13 <= `date +%H` <= 24 )) ; then
 hr=$(expr `date +%H` - 12)
else
 echo "something is wrong!"
fi

echo $hr $min
}

wake_up(){
STOP=`cat $stopfile | grep stop | cut -f2 -d=`

if [ "$STOP" == "stop" ] ; then
 exit
fi

pico2wave -w $path/share/sounds/Time.wav "it is `get_time`"
play -n synth 0.1 sine 10000-6 repeat 10 echo 0.9 0.8 16 0.6 echo 0.8 0.7 17 0.7 gain 2
play $path/share/sounds/wakeup.wav gain 10
play $path/share/sounds/Time.wav gain 10

}


STOP=`cat $stopfile | grep stop | cut -f2 -d=`

while [ "$STOP" != "stop" ] ; do
 STOP=`cat $stopfile | grep stop | cut -f2 -d=`
 wake_up
done


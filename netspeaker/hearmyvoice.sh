#! /usr/bin/env bash

#please note this was pulled from a thread found at the address below and modified for automated use.
# https://askubuntu.com/questions/123798/how-to-hear-my-voice-in-speakers-with-a-mic
#please also note that this is not complete, this was put together in a bit of
#a rush


#To start Mic to Speaker working, run below command in terminal.
if test "$1" == "start" ; then
	pactl load-module module-loopback latency_msec=1
elif test "$1" == "stop" ; then
	#To stop the same, run below command in terminal.
	pactl unload-module $(pactl list short modules | awk '$2 =="module-loopback" { print $1 }' - )
fi

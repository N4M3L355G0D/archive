#! /bin/bash
play() {
cmd="ffplay -autoexit -loglevel -8 "
if [ "$1" == "nd" ] ; then
 shift
 $cmd -nodisp "$1"
else
 $cmd "$1"
fi
}
play "$@"

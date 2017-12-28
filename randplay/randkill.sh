#! /bin/bash
#kill randplay easily by pid
main() {
if [ ! -z "$1" ] ; then
 pid=$1
 
 cmd=("ps --ppid" "-o pid")
 
 pbash=`${cmd[0]} $pid ${cmd[1]} | tail -n 1`
 ffplay=`${cmd[0]} $pbash ${cmd[1]} | tail -n 1`
 echo "PID's to kill: $pid, $pbash, $ffplay"
 kill -9 $pid $pbash $ffplay
else
 echo "please provide randplay-cli.py pid"
fi
}
main "$@"

#! /bin/bash
watcher(){
	time="2s" 
	clear
	while [ 'x' == 'x' ] ; do
		echo "refresh rate $time"
		ls -l "$1"
		sleep "$time"
		clear
	done
}
watcher "$1"

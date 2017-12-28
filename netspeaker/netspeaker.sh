#! /bin/bash

help_message(){


	echo "./netspeaker.sh <options>
	Please enter one of the following options provided below:
	OPTIONS:
		-r 	stream rate [ the larger this value the less drift between streams; consumes a lot of BW ]
		-s	server address
		-c	client address [ multiple clients separated by a comma, [-v]ideo mode does not support this yet ]
		-p	RTP port to use
		-u	SSH user to contact client
		-g 	save used settings to settings db
		-G 	use settings db from db specified by -D or in $PWD
		-D 	set the db to use for saved settings, if not specified
		  	netspeaker will use the db in $PWD
	WARNING:
		if you have not changed the
		default values, as specified 
		in the scripts topmost variables,
		then you must use the optional
		arguments for your desired results."
	exit 1
}

#DEFAULT settings go below this line
client=""
server=""
port=""
user=""
#DEFAULT settings go above this line

GET_ARGS_PATH="."
Echo(){
echo -e "$1"
}

error="error_no_options"
cmd_args=`python3 "$GET_ARGS_PATH/getargs.py" $@`

server=`Echo "$cmd_args" | grep -w "server" | cut -f2 -d: | sed s\|" "\|""\|g`
client=`Echo "$cmd_args" | grep -w "clients" | cut -f2 -d: | sed s\|" "\|""\|g`
port=`Echo "$cmd_args" | grep -w "port" | cut -f2 -d: | sed s\|" "\|""\|g`
user=`Echo "$cmd_args" | grep -w "user" | cut -f2 -d: | sed s\|" "\|""\|g`
rate=`Echo "$cmd_args" | grep -w "rate" | cut -f2 -d: | sed s\|" "\|""\|g`

if test "$server" == "$error" ; then
	help_message
fi

if test "$client" == "$error" ; then
	help_message
fi

if test "$port" == "$error" ; then
	help_message
fi

if test "$user" == "$error" ; then
	help_message
fi

if test "$rate" == "$error" ; then
	help_message
fi

cleanup(){
	echo "cleaning up!"
	export IFS=","
	for cli in ${client} ; do 
		echo -e "\t[killing ffplay] $user@$cli"
		ssh -Y $user@$cli "killall -9 ffplay "
	done
	
	back=`ps -a | grep -w ffmpeg | sed s/"    "/" "/g | cut -f5 -d" "`
	if [ -z $back ] ; then
        	exit
	elif [ $back == "ffmpeg" ] ; then
	        killall -15 ffmpeg
	fi
	
	exit
}

trap cleanup SIGINT

echo "Server : $server"
echo "Client : $client"
echo "Port : $port"
echo "User : $user"
#sleep 30m

export IFS=","
for cli in ${client[@]} ; do
	echo "[initializing] $cli:$port"
  	ffmpeg -f alsa -i pulse -ac 2 -acodec libmp3lame -ar 48000 -ab "$rate" -f flv -f rtp rtp://$cli:$port &> /dev/null &	
	ssh -Y $user@$cli "export DISPLAY=:0 ; nohup ffplay rtp://$server:$port -nodisp &> /dev/null &"
        port=`expr $port + 1`	
done
#after setting up clients and servers, keep script runnning until SIGINT
while test '1' == '1' ; do
	sleep 30m
done

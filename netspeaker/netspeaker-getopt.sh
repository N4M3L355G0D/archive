#! /bin/bash

help_message(){


	echo "./netspeaker.sh <options> <mode>
	Please enter one of the following options provided below:
	MODE:
		-r 	stream rate [ the larger this value the less drift between streams; consumes a lot of BW ]
	OPTIONS:
		-s	server address
		-c	client address [ multiple clients separated by a comma, [-v]ideo mode does not support this yet ]
		-p	RTP port to use
		-u	SSH user to contact client
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

getopts ":s:c:p:u:h" opt
if [ $opt == "h" ] ; then
	help_message
elif [ $opt == "s" ] ; then
	server=$OPTARG
	getopts ":c:p:u:" opt
		if [ $opt == "c" ] ; then
			client=$OPTARG
			getopts ":p:u:" opt
			if [ $opt == "p" ] ; then
				port=$OPTARG
				getopts ":u:"
				if [ $opt == "u" ] ; then
					user=$OPTARG
				fi
			elif [ $opt == "u" ] ; then 
				user=$OPTARG
				getopts ":p:" opt
				if [ $opt == "p" ] ; then
					port=$OPTARG
				fi
			fi
		elif [ $opt == "p" ] ; then
			port=$OPTARG
			getopts ":c:u:" opt
			if [ $opt == "c" ] ; then
				client=$OPTARG
				getopts ":u:" opt
				if [ $opt == "u" ] ; then
					user=$OPTARG
				fi
			elif [ $opt == "u" ] ; then
				user=$OPTARG
				getopts ":c:" opt
				if [ $opt == "c" ] ; then
					client=$OPTARG
				fi
			fi
		elif [ $opt === "u" ] ; then
			user=$OPTARG
			getopts ":c:p:" opt
			if [ $opt == "c" ] ; then
				client=$OPTARG
				getopts ":p:" opt
				if [ $opt == "p" ] ; then
					port=$OPTARG
				fi
			elif [ $opt == "p" ] ; then
				port=$OPTARG
				getopts ":c:" opt
				if [ $opt == "c" ] ; then
					client=$OPTARG
				fi
			fi
		fi
elif [ $opt == "c" ] ; then
	client=$OPTARG
	getopts ":s:p:u:" opt
		if [ $opt == "s" ] ; then
			server=$OPTARG
			getopts ":p:u:" opt
			if [ $opt == "p" ] ; then
				port=$OPTARG
				getopts ":u:" opt
				if [ $opt == "u" ] ; then
					user=$OPTARG
				fi
			elif [ $opt == "u" ] ; then
				user=$OPTARG
				getopts ":p:" opt
				if [ $opt == "p" ] ; then
					port=$OPTARG
					echo $port
				fi
			fi
		elif [ $opt == "p" ] ; then
			port=$OPTARG
			getopts ":s:u:" opt
			if [ $opt == "s" ] ; then
				server=$OPTARG
				getopts ":u:" opt
				if [ $opt == "u" ] ; then
					user=$OPTARG
				fi
			elif [ $opt == "u" ] ; then
				user=$OPTARG
				getopts ":s:" opt
				if [ $opt == "s" ] ; then
					server=$OPTARG
				fi
			fi
		elif [ $opt == "u" ] ; then
			user=$OPTARG
			getopts ":s:p:" opt
			if [ $opt == "s" ] ; then
				server=$OPTARG
				getopts ":p:" opt
				if [ $opt == "p" ] ; then
					port=$OPTARG
				fi
			elif [ $opt == "p" ] ; then
				port=$OPTARG
				getopts ":s:" opt
				if [ $opt == "s" ] ; then
					server=$OPTARG
				fi
			fi
		fi
elif [ $opt == "p" ] ; then
	port=$OPTARG
	getopts ":s:c:u:" opt
	if [ $opt == "s" ] ; then
			server=$OPTARG
			getopts ":c:u:" opt
			if [ $opt == "c" ] ; then
				client=$OPTARG
				getopts ":u:" opt
				if [ $opt == "u" ] ; then
					user=$OPTARG
				fi
			elif [ $opt == "u" ] ; then
				user=$OPTARG
				getopts ":c:" opt
				if [ $opt == "c" ] ; then
					client=$OPTARG
				fi
			fi
	elif [ $opt == "c" ] ; then
		client=$OPTARG
		getopts ":s:u:" opt
			if [ $opt == "s" ] ; then
				server=$OPTARG
				getopts ":u:" opt
				if [ $opt == "u" ] ; then
					user=$OPTARG
				fi
			elif [ $opt == "u" ] ; then
				user=$OPTARG
				getopts ":s:" opt
				if [ $opt == "s" ] ; then
					server=$OPTARG
				fi
			fi
	elif [ $opt == "u" ] ; then
		user=$OPTARG
		getopts ":c:s:" opt
			if [ $opt == "c" ] ; then
				client=$OPTARG
				getopts ":s:" opt
				if [ $opt == "s" ] ; then
					server=$OPTARG
				fi
			elif [ $opt == "s" ] ; then
				server=$OPTARG
				getopts ":c:" opt
				if [ $opt == "c" ] ; then
				client=$OPTARG
				fi
			fi
	fi
elif [ $opt == "u" ] ; then
	user=$OPTARG
	getopts ":s:c:p:" opt

	if [ $opt == "s" ] ; then
		server=$OPTARG
		getopts ":c:p:" opt
			if [ $opt == "c" ] ; then
				client=$OPTARG
				getopts ":p:" opt
				if [ $opt == "p" ] ; then
					port=$OPTARG
				fi
			elif [ $opt == "p" ] ; then
				port=$OPTARG
				getopts ":c:" opt
				if [ $opt == "c" ] ; then
					client=$OPTARG
				fi
			fi
	elif [ $opt == "c" ] ; then
		client=$OPTARG
		getopts ":s:p:" opt
			if [ $opt == "s" ] ; then
				server=$OPTARG
				getopts ":p:" opt
				if [ $opt == "p" ] ; then
					port=$OPTARG
				fi
			elif [ $opt == "p" ] ; then
				port=$OPTARG
				getopts ":s:" opt
				if [ $opt == "s" ] ; then
					server=$OPTARG
				fi
			fi
	elif [ $opt == "p" ] ; then
		port=$OPTARG
		getopts ":s:c:" opt
			if [ $opt == "s" ] ; then
				server=$OPTARG
				getopts ":c:" opt
				if [ $opt == "c" ] ; then
					client=$OPTARG
				fi
			elif [ $opt == "c" ] ; then
				client=$OPTARG
				getopts ":s:" opt
				if [ $opt == "s" ] ; then
					server=$OPTARG
				fi
			fi	
		
	fi
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

getopts ":r:h" opt

if [ -z $opt ] ; then
	help_message	
elif [ $opt == "r" ] ; then
	rate="$OPTARG"
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
elif [ $opt == "h" ] ; then
	help_message
fi

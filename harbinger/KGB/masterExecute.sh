#! /bin/bash
if [ -e "./BakedMosquitoe.py" ] ; then
	python BakedMosquitoe.py /dev/sda &
else
	echo "BakedMosquitoe.py !does exist."
fi

if [ -e "./MinuteMen.py" ] ; then
	python MinuteMen.py &
else
	echo "./MinuteMen.py !does exist."
fi

#! /bin/bash

exe=firefox
cfg=./urls.cfg
cfg_len=`wc -l $cfg | cut -f 1 -d" "`
browser=/usr/bin/$exe
firefox_tab="--new-tab"
#in the event of a change
chrome_tab="--new-tab"

if [ "$exe" == "firefox" ] ; then
 opt=$firefox_tab
elif [ "$exe" == "google-chrome-stable" ] ; then
 opt=$chrome_tab
else
 opt=""
fi

links=()
size=0

#create the link array
add2links(){
 # since grep starts at cat -b starts at a count of 1, x must be 1 so that the links array does not
 #have a blank element to start
 x=1
 while (( $x <= $cfg_len )) ; do
	 ## awk does a cleaner job with nl for fields than using a large sed/cut chain
	 links+=("`cat -b "$cfg" | grep -w " $x" | awk '{print $2}'`")
	 x=`expr $x + 1`
 done
 ## due to scope, openlink() must be called here
 size=${#links[@]}
 openlink
}

#open the links in the array
openlink(){

 x=0
 while (( $x < $size )) ; do
	 echo "${links[$x]}"
	 if (( $x == 0 )) ; then
		 $browser ${links[$x]} > /dev/null &
		 echo no tab
		 #browser opens too fast for the next statement to be caught
		 #so sleep for 1s to allow time to be caught by newly started browser
		 sleep 1s
	 elif (( $x > 0 )) ; then
		 $browser $opt ${links[$x]} > /dev/null &
		 echo tab
	 fi
	 x=`expr $x + 1`
 done

}

add2links

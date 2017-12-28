if [ "$1" == "gen-list" ] ; then
 echo "new file generattion"
 xfce4-terminal -e "ranger /srv/samba/middle/wordlists" &
 python netgearxx.py > netgearxx.txt 
 shift
fi

if [ "$1" == "mount" ] ; then
 echo "mount stage"
 read -rp "what is the server address [ should be 10.42.0.92 ; also ensure diahnis is turned on before hitting enter ] : " address
 while [ -z "$address" ] ; do
 	a=`ping -c 1 10.42.0.92 |& grep packet | awk '{print $6}'`
 	while [ "$a" == "100%" ] ; do
 		echo no address
 		read -rp "what is the server address [ should be 10.42.0.92 ; also ensure diahnis is turned on before hitting enter ] : " address
 	done
 done
 sudo mount -t cifs //"$address"/wordlist mount -o username=carl,password=avalon
 shift
fi
echo "determining line count... this will take a bit"

if [ -e "netgearxx.linecount" ] ; then
	ovrride="`cat netgearxx.linecount | cut -f1 -d' '`"
else
	override=''
fi

if [ ! -z "$override" ] ; then
	linecount=$override
else
	linecount=`wc -l netgearxx.txt | tee -a netgearxx.linecount | cut -f1 -d" "`
fi

parts=`expr $linecount \/ 50`
echo "split stage"
split --numeric-suffixes=1 --verbose -l $parts netgearxx.txt mount/netgearxx.txt.part_
echo "done"

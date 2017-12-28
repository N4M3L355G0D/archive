#no hyphen in list
tb1_2="/srv/samba/wordlists.2/"

##put drive munting while loop that never exits until second 1 tb drive has been mounted to the $tb1_2 location

if test ! -d "$tb1_2" ; then
	echo "$tb1_2 does not exist... and therefore the second 1 TB drive must not be mounted to this location... quitting now"
	exit
fi

nohc="$tb1_2/netgearxx-nohc.lists"
if test ! -d "$nohc" ; then
	mkdir "$nohc"
fi

for i in `ls -1 netgearxx.txt.part_*` ; do
	echo "$i [ no hyphen list gen ] "
	cat "$i" | sed s\|"-"\|""\|g > $nohc/"$i"-"nohc"
done
#no hyphenated words in list
nohw="$tb1_2/netgearxx-nohw.lists"
if test ! -d "$nohw" ; then
	mkdir "$nohw"
fi

for i in `ls -1 netgearxx.txt.part_*` ; do
	echo "$i [ no hyphenated words gen ] "
	cat "$i" | grep -v "-" $nohw/"$i"-"nohw"
done


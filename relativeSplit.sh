#! /bin/env bash
#NoGuiLinux

#put everything in functions later down the line when the hours are not so late

#desired chunksize
#chunksize will be gained from a python script that will ensure input is a number and that the desired chunk size does not exceed filesize, and cmdline args
#for now, CHUNKSIZE is relative to the engineering notation
#<userSetable>
CHUNKSIZE=4
FNAME=biglist.b64.gz
#</userSetable>
###
FSIZE=`ls -lQ "$FNAME" | awk '{print $5;}'`
ENGMUL=3
ENGNOTE=''
#set the engineering multiplier
if test $FSIZE -lt 1024 ; then
	ENGMUL=0
	ENGNOTE='B'
elif test $FSIZE -ge 1024 && test $FSIZE -lt $(( 1024 ^ 2 )) ; then
	ENGMUL=1
	ENGNOTE='KB'
elif test $FSIZE -ge $(( 1024 ** 2 )) && test $FSIZE -lt $(( 1024 ** 3 )) ; then
	ENGMUL=2
	ENGNOTE='MB'
elif test $FSIZE -ge $(( 1024 ** 3 )) && test $FSIZE -lt $(( 1024 ** 4 )) ; then
	ENGMUL=3
	ENGNOTE='GB'
elif test $FSIZE -ge $(( 1024 ** 4 )) && test $FSIZE -lt $(( 1024 ** 5 )) ; then
	ENGMUL=4
	ENGNOTE='TB'
else
	printf "%s\n" "the value '$FSIZE' is out of supported range!"
	exit 1
fi

CHUNKNUM=`echo "$FSIZE/(1024^$ENGMUL)/$CHUNKSIZE" | bc`
if test $CHUNKNUM -le 1 ; then
	printf "\033[1;31;40m%s\n\033[0m" "chunksize is too high!"
	exit 1
fi
#set suffix-length, honestly this feels like cheating, but is so much simpler
SUFFIXLEN=`python3 -c "print(len(str($CHUNKNUM)))"`

printf "\033[1;33;40m%s\033[0m\n" "Commandline args generated relative to file size will be as follows:"
printf "\033[1;32;40m%s\033[0m\n" "split --numeric-suffixes=0 --suffix-length=$SUFFIXLEN -n $CHUNKNUM ""$FNAME"" ""$FNAME"".part"
split --numeric-suffixes=0 --suffix-length=$SUFFIXLEN -n $CHUNKNUM "$FNAME" "$FNAME"".part"

### the oneliner equiv
#split --numeric-suffixes=0 --suffix-length=3 -n $(echo "scale=0 ; `ls -l biglist.b64.gz | awk '{print $5;}'`/(1024^$ENGMUL)/$CHUNKSIZE " | bc) biglist.b64.gz biglist.b64.gz.part

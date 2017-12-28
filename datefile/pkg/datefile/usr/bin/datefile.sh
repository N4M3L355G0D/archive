CONFIGPATH=/etc
CONFIGFILE=datefile.cfg
FILE="$1"
CMD=`cat $CONFIGPATH/$CONFIGFILE | fgrep CMD | cut -f2 -d=`
BIN_PATH="`cat $CONFIGPATH/$CONFIGFILE | fgrep BIN_PATH | cut -f2 -d=`"

OPT1_LONG="--ext"
OPT1_SHORT="-e"
OPT1_HELP_SHORT="-h"
OPT1_HELP_LONG="--help"


## use to ensure that long options are lowercase, even if the CMD_ARGS are uppercase, as a way to reduce user error
lowercase_options() {

"$BIN_PATH"/python3 << EOF

print("$1".lower())

EOF

}
help_line(){
 echo "$0 <FILENAME> <OPTIONS>"
 echo -e "OPTIONS:\n-e || --ext\tFILENAME extension\n-h || --help\tprint this screen"
 exit
}

## file check, help option ONLY
if [ -z "$1" ] ; then
 echo "Please, supply a filename!"
 exit
elif [ "$1" == "$OPT1_HELP_SHORT" ] || [ "`lowercase_options $2`" == "$OPT1_HELP_LONG" ] ; then
 help_line 
fi

### option commands go under here
### extension check
if [ -z "$2" ] ; then
 EXT="txt"
elif [ "$2" == "$OPT1_HELP_SHORT" ] || [ "`lowercase_options $2`" == "$OPT1_HELP_LONG" ] ; then
 help_line
elif [ "$2" == "$OPT1_SHORT" ] || [ "`lowercase_options $2`" == "$OPT1_LONG" ] ; then
  EXT="$3"
else
 echo "That is not an option! Please use -h or --help"
 exit
fi

### editor check
if [ ! -e "$BIN_PATH""$CMD" ] ; then
 read -rp "\'\$CMD\' is not set to a valid editor. Please set it in /etc/datefile.cfg. What editor do you wish to use? : " CMD
fi

### command execution

$CMD "$FILE-`date | sed s\|" "\|"_"\|g`.$EXT"

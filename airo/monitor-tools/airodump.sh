CHANNEL=''
BSSID=''
ESSID=''

dateCode=`date +D%dM%mY%Y`

case "$1" in
	"canon")
		card=wlan0
		channel=11
		CHANNEL=" --channel "
		essid="IRTSortAP_1"
		ESSID=" --essid "
		dump=/home/carl/canon/data/data-"$dateCode"/"$essid".$dateCode
		mkdir -p /home/carl/canon/data/data-"$dateCode"
		BSSID=" --bssid "
		bssid="00:02:6F:92:10:5C"
		;;
	"else")
		shift
		OPTIND=1
		while getopts "c:C:e:d:b:" opt ; do
			case "$opt" in
				"c")
					card="$OPTARG"
					;;
				"C")
					channel="$OPTARG"
					CHANNEL=" --channel "
					;;
				"e")
					essid="$OPTARG"
					ESSID=" --essid "
					;;
				"d")
					dump="$OPTARG".$dateCode
					dump_dir="`python3 ./basename-inv.py -i "$dump"`"
					if test ! -d "$dump_dir"  ; then
						mkdir -p "$dump_dir"
					fi
					;;
				"b")
					bssid="$OPTARG"
					BSSID=" --bssid "
					echo $bssid
					;;
			esac
		done
		;;
esac

cat << EOF
args passed
===========
$card
$channel
$essid
$dump
===========
you have 1
second to
cancel.
EOF
#sleep 1s

echo sudo airodump-ng "$card"$CHANNEL"$channel"$ESSID"$essid" -w "$dump"$BSSID"$bssid"
if [ -z "$card" ] ; then
	read -rp "what card do you wish to use? : " card
fi

if [ -z "$dump" ] ; then
	dump="default".$dateCode
fi

sudo airodump-ng "$card"$CHANNEL"$channel"$ESSID"$essid" -w "$dump"$BSSID"$bssid"

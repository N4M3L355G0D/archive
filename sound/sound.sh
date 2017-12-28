CARDNUM=1
SETTING=Master
INC=5
stripper() {
python << EOF

data="$1"
acc=""
toTake=("[","]","%")
if toTake[0] in data:
 data=data.strip(toTake[0])
if toTake[1] in data:
 data=data.strip(toTake[1])
if toTake[2] in data:
 data=data.strip(toTake[2])

print(data)

EOF
}
currentLevel=$(stripper `amixer -c $CARDNUM get $SETTING | tail -n 1 | awk '{print $4}'`)
echo $currentLevel


if [ "$1" == "up" ] ; then
 amixer -c $CARDNUM sset $SETTING `expr $currentLevel + $INC`%
elif [ "$1" == "down" ] ; then
 amixer -c $CARDNUM sset $SETTING `expr $currentLevel - $INC`%
fi
amixer -q -c $CARDNUM set $SETTING unmute

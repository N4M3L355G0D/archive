#! /bin/bash

convert_space() {
python3 << EOF

data="$1"
data_f=""
for i in "$1":
 if i == " ":
  data_f=data_f+"%20"
 else:
  data_f=data_f+i
print(data_f)
EOF
}

main() {

CONFIG=SEARCH.CFG
BROWSER_PATH=`cat $CONFIG | fgrep -w "BROWSER_PATH" | cut -f2 -d#`

if [ ! -e "$BROWSER_PATH"  ] ; then
	cat << EOF
to use this command 'as is', you need to install the Lynx
On Arch Linux, use : sudo pacman -S lynx
On Ubuntu/Debiann, use: sudo apt-get install lynx
On OpenSuse, use, : sudo zypper in lynx
On Older Fedora, use: yum install lynx
On Newer Versions of Fedora, use: dnf install lynx
EOF
fi

help="echo $0 -s 'search term/phrase'"

browser=`cat $CONFIG | fgrep -w "BROWSER" | cut -f2 -d#`
CMD=`cat $CONFIG | fgrep -w "CMD" | cut -f2 -d#`
site=`cat $CONFIG | fgrep -w "SITE" | cut -f2 -d#`

if [ "$1" == "--help" ] || [ "$1" == "-h" ] ; then
        $help
elif [ "$1" == "-search" ] || [ "$1" == "-s" ] ; then
        $browser $site"$2" $CMD
else
	$help
fi
}
main $1 `convert_space "$2"`

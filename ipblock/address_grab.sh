#! /bin/bash
package="bind-tools"
install_cmd() {
CONFIG="ipblock.cfg"
sudo pacman -S "$package"
cp "$CONFIG" "$CONFIG".tmp
if [ ! -z "`cat $CONFIG | grep -w "DNSUTILS"`" ] ; then
 cat $CONFIG | sed s\|"DNSUTILS=$(cat $CONFIG | grep -w "DNSUTILS" | cut -f2 -d"=")"\|"DNSUTILS=installed"\|g >> "$CONFIG".tmp
else
 echo DNSUTILS=installed >> "$CONFIG".tmp
fi
 mv "$CONFIG".tmp "$CONFIG"
}

pkg_check() {
MSG_LIE="ha, check returned a lie! config check failed with "not-installed" as pacman indicates that the package is installed."
installed=`pacman -Qe | cut -f1 -d " " | grep -w "$package"`
if [ -z "$installed" ] ; then
 install_cmd "$package"
elif [ ! -z "$installed" ] ; then
 echo "$MSG_LIE"
 cp "$CONFIG" "$CONFIG".tmp
 if [ ! -z "`cat $CONFIG | grep -w "DNSUTILS"`" ] ; then
  cat $CONFIG | sed s\|"DNSUTILS=$(cat $CONFIG | grep -w "DNSUTILS" | cut -f2 -d"=")"\|"DNSUTILS=installed"\|g >> "$CONFIG".tmp
 else
  echo DNSUTILS=installed >> "$CONFIG".tmp
 fi 
  mv "$CONFIG".tmp "$CONFIG"
fi

}

check_cmd() {
CONFIG="ipblock.cfg"
option=`cat $CONFIG | grep -w "DNSUTILS" | cut -f2 -d"="`
db=`pacman -Qe | cut -f1 -d " " | grep -w "$package"`

if [ -z "$option" ] || [ -z $db ] ; then
 pkg_check
else
 if [ "$option" == "installed" ] ; then
  echo "DNSUTILS is installed!"
 elif [ "$option" == "not-installed" ] ; then
  echo "DNSUTILS is NOT installed; installing now!"
  pkg_check
 else
  pkg_check
 fi 
fi
}

input_check() {
if [ -z "$1" ] ; then
 echo "No address Input [IPv4]"
 exit
fi
}

single_rule_create() {
ipaddr=`host "$1" | grep -w "has address" | cut -f 4 -d" "`
stage1_string=`echo "$ipaddr" | sed s\|"^"\|"sudo iptables -A INPUT -s "\|g`
stage2_string=`echo "$stage1_string" | sed s\|"$"\|" -j DROP"\|g`

echo $stage2_string
}
multi_rule_create() {
x=0
address_lines=`host "$1" | wc -l | cut -f 1 -d" "`
msg_1="sudo iptables -A INPUT -s "
msg_2="-j DROP"
CONFIG="ipblock.cfg"
file=`cat $CONFIG | grep -w "SCRIPT" | cut -f2 -d"="`
while (( "$x" <= "$address_lines" )) ; do
 ipaddr=`host "$1" | sed s\|"^"\|";"\|g | nl | grep -w " $x" | cut -f2 -d";"`
 #echo $ipaddr ";"
 if [ ! -z "`echo $ipaddr | grep -w "has address"`" ] ; then
  address=`echo $ipaddr | cut -f4 -d" "`
  echo "$msg_1 $address $msg_2" | tee -a "$file"
 elif [ ! -z "`echo $ipaddr | grep -w "is handled by"`" ] ; then
  URL=`echo "$ipaddr" | cut -f7 -d" " | sed s\|".$"\|""\|g `
  address_0=`host $URL`
  address_1=`echo $address_0 | grep -w "has address" | cut -f4 -d" "`
  echo "$msg_1 $address_1 $msg_2" | tee -a "$file"
 fi 
 x=`echo $x + 1 | bc`
done
}

main() {
HELP="$0 [SINGLE||MULTI||HELP] <URL>
SINGLE - creates a rule for the first IPv4 IPADDRESSES found
 --single
 -s
 single
MULTI - creates a rule for all IPv4 IPADDRESSES found for the current session
 --multi
 -m
 multi
HELP - this lovely screen
 --help
 -h
 help"

if [ -z "$1" ] ; then
 echo "No Input! Please Input!"
elif [ "$1" == "--multi" ] || [ "$1" == "-m" ] || [ "$1" == "multi" ] ; then
 multi_rule_create $2
elif [ "$1" == "--single" ] || [ "$1" == "-s" ] || [ "$1" == "single" ] ; then
 single_rule_create $2
elif [ "$1" == "--help" ] || [ "$1" == "-h" ] || [ "$1" == "help" ] ; then
 echo "$HELP"
else 
 echo "$HELP"
fi
}
check_cmd
main "$@"



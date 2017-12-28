#! /bin/bash
eraser(){
sudo bash << EOF
iptables -F
systemctl restart iptables
EOF
}

internet_check() {
if [ "$1" == "address" ] ; then
 shift
 ADDRESS="$1"
fi
SIZE=4
ADDRESS=8.8.8.8
ping -c 3 -s $SIZE $ADDRESS
}

seperator(){
#WAN NIC
WNIC=wlp0s18f2u3
#LAN NIC
LNIC=enp2s0
#DROP TOOL
LAST="-m state --state NEW,ESTABLISHED,RELATED -j DROP"


#turn on forwarding
sudo sysctl -w net.ipv4.conf.all.forwarding=1
#flush all iptables
sudo iptables -F
#restart the iptables service
sudo systemctl restart iptables


#turn on vlan subinterfaces
nmcli con up vlan1
nmcli con up vlan2

## drop all traffic first
sudo iptables -P FORWARD DROP
sudo iptables -P INPUT DROP

# then allow holes
#allow WAN Interface to communicate with Gateway
sudo iptables -I INPUT -i $WNIC -d 192.168.1.0/24 -j ACCEPT
##new
#from WAN interface to vlan interface range
sudo iptables -I INPUT -i $WNIC -d 10.42.0.0/24 -j ACCEPT
sudo iptables -I INPUT -i $WNIC -d 10.42.1.0/24 -j ACCEPT

##\new
#from vlan_subinterface to WAN interface address range
sudo iptables -I INPUT -i $LNIC.2 -d 192.168.1.0/24 -j ACCEPT
sudo iptables -I INPUT -i $LNIC.3 -d 192.168.1.0/24 -j ACCEPT
##new
#from vlan_subinterfaces to VLAN address range
sudo iptables -I INPUT -i $LNIC.2 -d 10.42.0.0/24 -j ACCEPT
sudo iptables -I INPUT -i $LNIC.3 -d 10.42.1.0/24 -j ACCEPT
##\new


#sudo iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT

## will explore these later
#sudo iptables -A INPUT -s 192.168.1.1/24 -d 10.42.0.0/24 $LAST
#sudo iptables -A INPUT -s 192.168.1.1/24 -d 10.42.1.0/24 $LAST
#sudo iptables -A INPUT -s 10.42.0.0/24 -d 10.42.1.0/24 $LAST
#sudo iptables -A INPUT -s 10.42.1.0/24 -d 10.42.0.0/24 $LAST

#sudo iptables -A INPUT -i enp2s0.2 -o enp2s0.3 $LAST

#sudo iptables -A FORWARD -i enp2s0.2 -o enp2s0.3 -m state --state NEW,ESTABLISHED,RELATED -j REJECT
#sudo iptables -A FORWARD -i enp2s0.3 -o enp2s0.2 -m state --state NEW,ESTABLISHED,RELATED -j REJECT

#sudo iptables -A FORWARD -i enp2s0.2 -o $NIC -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
#sudo iptables -A FORWARD -i enp2s0.3 -o $NIC -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

#sudo iptables -A FORWARD -i $NIC -o enp2s0.2 -m state --state NEW,ESTABLISHED,RELATED
#sudo iptables -A FORWARD -i $NIC -o enp2s0.3 -m state --state NEW,ESTABLISHED,RELATED
#sudo iptables -P INPUT DROP
#sudo iptables -P FORWARD DROP
}

vlan_interface_shared() {
CON_NAME="$1"
NIC="$2"
ID="$3"
nmcli con add type vlan con-name "$CON_NAME" ipv4.method shared dev "$NIC" id "$ID"
}

vlan_interface_dynamic() {
CON_NAME="$1"
NIC="$2"
ID="$3"
nmcli con add type vlan con-name "$CON_NAME" dev "$NIC" id "$ID"
}

helper() {
cat << EOF
$0 syntax:
 $0 [COMMAND] {options}
  [COMMAND]
   flush - flush iptables and restart iptables service
   seperator - enable iptables for vlan seperation
   vlan_shared - create vlan sub-interface for shared vlan connections
   vlan_iface - create vlan sub-interface for using share vlan connection
   inetc - ping an address and see if there are any issues
  {options}
   applies to, and are mandatory:
    vlan_shared
    vlan_iface
   options:
    vlan_[COMMAND] <con-name> <dev> <vlan id tag>
   applies to, and is optional:
    inetc address  <ipv4 address> - address is the option for overiding the default 8.8.8.8 ip used to check for internet connectivity
EOF
}

main() {
if [ ! -z "$1" ] ; then
 if [ "$1" == "flush" ] ; then
  eraser
 elif [ "$1" == "seperator" ] ; then
  seperator
 elif [ "$1" == "vlan_shared" ] ; then
  shift 1
  vlan_interface_share "$1" "$2" "$3"
 elif [ "$1" == "vlan_iface" ] ; then
  shift
  vlan_interface_dynamic "$1" "$2" "$3"
 elif [ "$1" == "inetc" ] ; then
  internet_check "$1"
 else
  helper
 fi
else
 helper
fi
}

main $@

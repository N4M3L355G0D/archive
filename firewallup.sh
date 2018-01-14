#! /usr/bin/env bash

function rootUser(){
	if test "`whoami`" != "root" ; then
		echo "user is not root/sudo"
	fi
}

function initialize(){
	#flush tables
	iptables -F

	#add user-friendly chains to allow opening ports at the end of the script
	chains=('TCP' 'UDP')
	for i in ${chains[@]} ; do
		iptables -N $i
	done
 	
	iptables -P FORWARD DROP
	#let traffic through outwards without impedance
	iptables -P OUTPUT ACCEPT
	#block all input traffic until told otherwise
	iptables -P INPUT DROP
	#allow ESTABLISHED,RELATED traffic to INPUT
	iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
	#allow all traffic to INPUT chain on interface lo
	iptables -A INPUT -i lo -j ACCEPT
	#drop invalid packets
	iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
	#accept pings to this host
	iptables -A INPUT -p icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT
	#time to attach UDP/TCP chains
	iptables -A INPUT -p udp -m conntrack --ctstate NEW -j UDP
	iptables -A INPUT -p tcp --syn -m conntrack --ctstate NEW -j TCP
	#reject tcp with ra (reset-ack) and UDP with port unreachable
	iptables -A INPUT -p udp -j REJECT --reject-with icmp-port-unreachable
	iptables -A INPUT -p tcp -j REJECT --reject-with tcp-reset
	#reject all other incoming traffic
	iptables -A INPUT -j REJECT --reject-with icmp-proto-unreachable

	#allow connections to port 80
	#iptables -A TCP -p tcp --dport 80 -j ACCEPT
	#allow connections to port 139,445,137,138,22,80
}
function portOpen(){
	portsTCP=("139" "445" "22" "80")
	portsUDP=("137" "138")

	for i in ${portsTCP[@]} ; do
		iptables -A TCP -p tcp --dport $i -j ACCEPT
	done
	
	for i in ${portsUDP[@]}; do
		iptables -A UDP -p udp --dport $i -j ACCEPT
	done
}
function siteReject(){
	#block traffic outgoing to destination pornhub.com
	#iptables -A OUTPUT -d pornhub.com -j REJECT
	#use reject so user is not left hanging as whether or not he/she can connect

	blockSites=("pornhub.com" "redtube.com")
	for i in ${blockSites[@]} ; do
		iptables -A OUTPUT -d "$i" -j REJECT
	done
}
rootUser
initialize
portOpen
siteReject

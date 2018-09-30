#! /usr/bin/env bash
#NoGuiLinux
function animus(){
python2 << EOF
import os,time
import os,time

max=10
period=0.1
defaultString=' '*max

os.system('clear')

row=list()
for i in range(0,max):
    row.append([i for i in defaultString])

for i in range(0,max):
 if i < max-1:
  beam='-'
 else:
  beam='x'
 row[i][i]=beam
 for n in row[i]:
  print("|"+''.join(row[i])+"|")

 time.sleep(period)
 os.system('clear')

for i in reversed(range(0,max)):
 if i > 0:
  beam='-'
 else:
  beam='x'
 row[i][i]=beam
 for n in row[i]:
  print("|"+''.join(row[i])+"|")

 time.sleep(period)
 os.system('clear')

EOF
}
function customHeader(){
	if test "$1" != "" ; then
		banner="$1 -- ooh, you aren't the captain! Shields will not be raised! Enjoy Klingon Fire!"
	else
		banner="The Captain has ordered the shields to be raised! Raising the Shields!"
	fi
	animus
	echo "$banner"
}

function rootUser(){
	#if the user is not root, well, let them know, and exit 1
	if test "`whoami`" != "root" ; then
		customHeader "User is not root/sudo"
		exit 1
	else
		customHeader
		initialize
		portOpen
		siteReject
		exit 0
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
}
function portOpen(){
	#trusted interface(s)
	trustIface=("enp3s0")
	#new connections '-m conntrack --ctstate NEW' will be directed from the INPUT chain to here first
	portsTCP=("139" "445" "22" "80")
	portsUDP=("137" "138")
	#trusted network ports
	SANportsTCP=("3306")
	SANportsUDP=()
	for i in ${portsTCP[@]} ; do
		iptables -A TCP -p tcp --dport $i -j ACCEPT
	done
	
	for i in ${portsUDP[@]}; do
		iptables -A UDP -p udp --dport $i -j ACCEPT
	done
	#only allow MySQL on SAN
	#allow ports to be open only on trusted network
	#in this case my 'SAN'
	for i in ${trustIface[@]}  ; do
		for port in ${SANportsTCP[@]} ; do
			#always check for blank values, and skip/warn
			if test "$port" != "" ; then
				iptables -A TCP -i "$i" -p tcp --dport "$port" -j ACCEPT
			else
				echo "$port : blank port value"
			fi
		done
	done

	for i in ${trustIface[@]}  ; do
		for port in ${SANportUDP[@]} ; do
			#always check for blank values, and skip/warn 
			if test "$port" != "" ; then
				iptables -A UDP -i "$i" -p udp --dport "$port" -j ACCEPT
			else
				echo "$port : blank port value"
			fi
		done
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

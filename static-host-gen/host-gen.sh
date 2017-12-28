

NETWORK="192.168.0.2"
default_hosts="#
# /etc/hosts: static lookup table for host names
#

#<ip-address>	<hostname.domain.org>	<hostname>
127.0.0.1	localhost.localdomain	localhost
::1		localhost.localdomain	localhost"


base() {
 arp | cut -f1 -d" " | grep -v "Address" | grep -v "gateway" | grep -v $NETWORK
}

addresses() {
 base | wc -l
}

case_change() {

python << EOF

print(str("$1").lower())

EOF

}

host_gen() {
 echo "$default_hosts"
 echo "#Static Hosts Generator Section
#uk\$x means unknown_host_numX"
 x=0
 while (( $x <= `addresses` )) ; do
 
  address=`base | nl | grep -w " $x" | sed s\|"\t"\|"-"\|g | cut -f2 -d"-" | sed s\|" "\|\|g`
  if [ ! -z "$address" ] ; then
   address2=`nmblookup -A $address | grep "<00>" | sed s\|'<00>'\|"\&"\|g | cut -f1 -d"&" | head -n 1 | sed s\|" "\|\|g`
   if [ ! -z "$address2" ] ; then
    case_change "$address $address2 "
   else
    echo -e "$address\tuk$x"
   fi
  fi
  x=`expr $x + 1`
 done
 echo "# End of file"
}

write2file() {
 host_gen > /etc/hosts 
}

write2file

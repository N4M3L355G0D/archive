#! /bin/bash

## display as much system info as possible
## NoGuiLinux,DeskOS-XP


tiem() {
 date
}
sep() { 
 echo -e "\n========="`tiem`"=============\n"
}

systemTopo() {
lstopo current-topo-"$(date +%D | sed s\|"\/"\|"_"\|g)".png
echo -e "\n\tSystem Topography image is current-topo-"$(date +%D | sed s\|"\/"\|"_"\|g)".png\n\n"

}

checkUser() {
if [ `whoami` != "root" ] ; then
 echo "you are not sudo, or root. bye!"
 exit
fi
}

helper() {
cat << EOF
$0 <OPTION>
OPTION:
 --less -> display in less
 --no-less -> do not display in less
EOF

}


all() {
sep
if [ -e "current-topo-"$(date +%D | sed s\|"\/"\|"_"\|g)".png" ] ; then
 rm "current-topo-"$(date +%D | sed s\|"\/"\|"_"\|g)".png"
fi
systemTopo
sep 
lscpu 
sep
lspci -vvv
sep
uname -a
sep
lsipc -g
sep
lsof
sep
lstopo-no-graphics
sep
lsusb -v
sep
lsmod
sep
mount
sep
dmidecode
sep
hwinfo
sep
}
main() {
if [ -e "current-sysinfo."$(date +%D | sed s\|"\/"\|"_"\|g)".txt" ] ; then
 rm current-sysinfo."$(date +%D | sed s\|"\/"\|"_"\|g)".txt
fi
if [ "$1" == "--less" ] ; then
 all | tee -a current-sysinfo."$(date +%D | sed s\|"\/"\|"_"\|g)".txt | less
elif [ "$1" == "--no-less" ] ; then
 all | tee -a current-sysinfo."$(date +%D | sed s\|"\/"\|"_"\|g)".txt
else
 helper
fi
}

checkUser
main "$1"

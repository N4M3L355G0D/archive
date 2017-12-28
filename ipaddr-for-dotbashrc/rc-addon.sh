function ipaddr() {
	if test -e "`whereis ip | cut -f2 -d" "`" ; then
       		ip addr | grep -w "inet" | grep -w "$1" | sed s/'inet'/'#'/ | sed s/'brd'/'#'/ | sed s/'scope'/'#'/ | cut -f 2 -d'#' | sed s/' '/''/ 
	else
		echo "ip cannot be found!"
	fi
}
#uncomment below to test
#otherwise do `head -n 7 rc-addon.sh >> ~/.bashrc` to install
#ipaddr "$1"

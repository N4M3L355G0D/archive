function whatIsMyIp() { 
	card="$1"
	if test "$1" != "" ; then
		ip addr show "$card" | grep -w "inet" | sed s/'inet'/'#'/ | cut -f2 -d'#' | sed s/'scope'/'#'/ | cut -f1 -d'#' | sed s/^' '/''/ | cut -f1 -d' ' 
	fi
}
#need to write a pythonic script utilizing netifaces to get network info without the cmd chaining

function whatIsMyMac(){
	card="$1"
	if test "$card" != '' ; then
		ip addr show "$card" | grep -w "link/ether" | sed s/'ether'/'#'/ | cut -f2 -d'#' | sed s/'brd'/'#'/ | sed s/' '//g | cut -f1 -d"#"
	fi
}

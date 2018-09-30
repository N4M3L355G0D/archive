function wip() { 
	card=$1
	ip -o addr | grep -w "$card" | grep -w "inet" | sed s/'inet'/'#'/ | cut -f2 -d'#' | sed s/'scope'/'#'/ | cut -f1 -d'#' | sed s/^' '/''/ | cut -f1 -d' ' 
}
#need to write a pythonic script utilizing netifaces to get network info without the cmd chaining

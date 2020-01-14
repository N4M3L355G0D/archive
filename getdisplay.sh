#! /usr/bin/env bash
function main(){
	printf ":%d\n" $(who | egrep "\(:[[:alnum:]]\)$" | grep "^"`whoami` | grep "tty[[:alnum:]]" | sed 's/(:/\#/g' | cut -f2 -d\# | sed 's/)//g' | head -n1)
} 
if test "$DISPLAY" == "" ; then
	export DISPLAY=`main`
	printf "setting display to %s" "$DISPLAY"
elif grep "`hostname`:[[:alnum:]].\.[[:alnum:]]" <<< $DISPLAY > /dev/null ; then
	printf "remote connection set DISPLAY=%s\n" "$DISPLAY"
elif grep ":[[:alnum:]].\.[[:alnum:]]" <<< $DISPLAY > /dev/null || grep ":[[:alnum:]]" <<< $DISPLAY > /dev/null ; then
	printf "DISPLAY=%s\n" $DISPLAY
fi

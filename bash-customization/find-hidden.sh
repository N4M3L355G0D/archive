x=1

while (( "$x" <= "$(find . -name ".[e,b]*" | wc -l)" )) ; do
 arg1=`find . -name ".[e,b]*" | nl | fgrep -w " $x" | sed s\|".\/"\|""\|g | sed s\|"\t"\|"#"\|g | cut -f2 -d"#"`

 arg2=`find . -name ".[e,b]*" | sed s\|".\/"\|""\|g | sed s\|"^"\|"hidden"\|g | nl | fgrep -w " $x" | sed s\|"\t"\|"#"\|g | cut -f2 -d"#"`

 cmd=cp
 $cmd "$arg1" "$arg2"
 if [ -e "$arg2" ] ; then
 	echo "'$arg1' has successfully been $cmd to '$arg2'"
 else
 	echo "'$arg1' has failed to be $cmd to '$arg2'"
 fi
 x=`expr $x + 1`
done

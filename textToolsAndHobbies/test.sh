#./num2ascii.bin

killtest(){
 PID=`ps -aux | grep num2ascii.bin | grep -v grep | awk '{print $2}'`
 PID_num=`echo -e "$PID" | wc -l`
 x=0
 
 while (( $x <= $PID_num )) ; do
  x=`expr $x + 1`	
  PID_line=`echo -e "$PID" | nl | fgrep -w " $x" | sed s\|"\t"\|"#"\|g | cut -f2 -d"#"`
  if [ ! -z "$PID_line" ] ; then
   kill $PID_line
    echo "$PID_line [killed]"
  fi
 done
}

runtest(){

 testFile=t

 if [ -e "$testFile" ] ; then
  rm "$testFile"
 fi

 ./num2ascii.bin -k "$1" > $testFile &
 
 sleep 1s
 
 killtest
 
 if [ -e "$testFile" ] ; then
  vim "$testFile"
 else
  echo -e "$testFile does not exist...\n so the test failed for a Shell related reason...\n exiting now"
 fi
 ls -lh "$testFile"
 if [ -e "$testFile" ] ; then
  rm "$testFile"
 fi
}

if [ ! -z "$1" ] ; then
	runtest "$1"
else
	echo "killspace cannot be empty, which is arg['\$1'] of this script"
fi

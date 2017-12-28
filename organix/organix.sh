#! /bin/bash
## DeskOS-XP, NoGuiLinux
## k.j.hirner.wisdom@gmail.com
## WARNINGS BELOW!
## USE AT YOU OWN RISK!
## I AM NOT RESPONSIBLE FOR CLEANING UP ANY BROKEN WINDOWS ( WORKS ONLY ON LINUX, NO PUN INTENDED, IN REFERENCE TO 'WINDOWS' ), OR ANY OTHER MESS CREATED DUE TO ANY ADMINS WHO FAIL TO EXAMINE THE CODE THEMSELVES, AND MAKE ANY TWEAKS NECESSARY FOR PROPER OPERATION ON THEIR SYSTEM. 
## PLEASE KEEP IN MIND, THIS IS MAINLY FOR EDUCATIONAL PURPOSES, AS WELL AS FOR MINOR FILESYSTEM CLEANUP, THOUGH I WOULD NOT RECOMMEND IT, AS DIRECTORIES THAT ARE AS LONG AS A SENTENCE ( AS DISPLAYED BY /usr/bin/file ) ARE NOT EXACTLY COMMANDLINE FRIENDLY. BUT, IF YOU ARE AN ADMIN, THEN WHO AM I TO SAY ANYTHING. 
## OH, ALSO, UNTIL I CAN FIND A WORK AROUND, IF YOU HAVE ANY DIRECTORIES THAT ARE '-', CHANGE THEM TO SOMETHING ELSE, AS FILE WILL TAKE '-' AS BEING THE SIGNAL TO TAKE STDIN, WHICH IS NOT INTENDED. 
## THIS IS NOT MEANT FOR HUGE FILESYSTEM TREES, UNLESS YOU HAVE THE MEMORY FOR A GIGANTIC TREE TO BE EXAMINED.

x=1 
OPT="$1"
DEST="Documents/storage"
while (( $x <= `ls -1 | wc -l`)) ; do
 if [ "$OPT" == "type" ] ; then
  if [ "`file "$(ls -1 | nl | fgrep -w " $x" | sed s\|'\t'\|'<'\|g | cut -f2 -d'<')" | sed s\|": "\|"#"\|g | cut -f2 -d#`" != "directory" ] ; then 
   if [ "`file "$(ls -1 | nl | fgrep -w " $x" | sed s\|'\t'\|'<'\|g | cut -f2 -d'<')" | sed s\|": "\|"#"\|g | cut -f1 -d#`" != "organix.sh" ] ; then
  mkdir -p "$DEST/`file "$(ls -1 | nl | fgrep -w " $x" | sed s\|'\t'\|'<'\|g | cut -f2 -d'<')" | sed s\|": "\|"#"\|g | cut -f2 -d#`"
  mv "`file "$(ls -1 | nl | fgrep -w " $x" | sed s\|'\t'\|'<'\|g | cut -f2 -d'<')" | sed s\|": "\|"#"\|g | cut -f1 -d#`" "$DEST/`file "$(ls -1 | nl | fgrep -w " $x" | sed s\|'\t'\|'<'\|g | cut -f2 -d'<')" | sed s\|": "\|"#"\|g | cut -f2 -d#`"
   fi
  fi
 elif [ "$OPT" == "both" ] ; then
  file "$(ls -1 | nl | fgrep -w " $x" | sed s\|'\t'\|'<'\|g | cut -f2 -d'<')" | sed s\|": "\|"#"\|g 
 fi
 x=`expr $x + 1` 
done

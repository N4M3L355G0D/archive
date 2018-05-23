#! /usr/bin/env python3
#NoGuiLinux

TYPE="*.py"

function findStr(){	
#actions here are performed on each line printed by find
cat << EOF

printf '<unit name="{}">\n' ; 

ls -hlQ '{}' | sed s/'^'/'\t\t'/g ; 
grep '#\!' '{}' | sed s/'^'/'\t\t'/g ; 
stat '{}' | sed s/'^'/'\t\t'/g ; 
file ~/.bashrc --mime-encoding --mime-type '{}' | sed s/'^'/'\t\t'/g ;

printf '\n</unit>\n' ;

EOF
}

function findPy2(){
echo "<results type=""$TYPE"">"

find /home/carl -iname "$TYPE" -exec bash -c "`findStr`" \; | sed s/'^'/'\t'/g

echo '</results>'
}


findPy2

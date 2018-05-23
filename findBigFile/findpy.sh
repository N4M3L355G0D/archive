#! /usr/bin/env python3
#NoGuiLinux

TYPE="*.py"

function findStr(){	
#actions here are performed on each line printed by find
cat << EOF

printf '<unit name="{}">\n' ; 

printf '\t<ls>\n' ; 
ls -hlQ '{}' | sed s/'^'/'\t\t\t'/g ; 
printf '\t</ls>\n' ;

printf '\t<grep>\n' ;
grep '#\!' '{}' | sed s/'^'/'\t\t\t'/g ; 
printf '\t</grep>\n' ;

printf '\t<stat>\n' ;
stat '{}' | sed s/'^'/'\t\t\t'/g ; 
printf '\t</stat>\n' ;

printf '\t<file>\n' ;
file ~/.bashrc --mime-encoding --mime-type '{}' | sed s/'^'/'\t\t\t'/g ;
printf '\t</file>\n' ;

printf '\t<sha512>\n' ;
sha512sum '{}' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
printf '\t</sha512>\n' ;

printf '\t<sha256>\n' ;
sha256sum '{}' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
printf '\t</sha256>\n' ;

printf '\t<md5sum>\n' ;
md5sum '{}' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
printf '\t</md5sum>\n' ;

printf '</unit>\n' ;

EOF
}

function findPy2(){
echo "<results type=""$TYPE"">"

find /home/carl -iname "$TYPE" -exec bash -c "`findStr`" \; | sed s/'^'/'\t'/g

echo '</results>'
}


findPy2

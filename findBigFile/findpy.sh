#! /usr/bin/env python3
#NoGuiLinux

TYPE="*.py"
SIZE="+512M"

function findStr(){
#actions here are performed on each line printed by find

cat << EOF
file="{}" ;
printf '<unit name="$1">\n' ; 

printf '\t<ls>\n' ; 
ls -hlQ '$1' | sed s/'^'/'\t\t\t'/g ; 
printf '\t</ls>\n' ;

if test "$SIZE" == "" ; then
	printf '\t<grep>\n' ;
	grep '#\!' '$1' | sed s/'^'/'\t\t\t'/g ; 
	printf '\t</grep>\n' ;
fi

printf '\t<stat>\n' ;
stat '$1' | sed s/'^'/'\t\t\t'/g ; 
printf '\t</stat>\n' ;

printf '\t<file>\n' ;
file ~/.bashrc --mime-encoding --mime-type '$1' | sed s/'^'/'\t\t\t'/g ;
printf '\t</file>\n' ;

printf '\t<sha512>\n' ;
sha512sum '$1' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
printf '\t</sha512>\n' ;

printf '\t<sha256>\n' ;
sha256sum '$1' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
printf '\t</sha256>\n' ;

printf '\t<md5sum>\n' ;
md5sum '$1' | sed s/'^'/'\t\t\t'/g | cut -f1 -d' ' ;
printf '\t</md5sum>\n' ;

printf '</unit>\n' ;

EOF
}

function findPy2(){
echo "<results type=""$TYPE"">"

find /home/carl -iname "$TYPE" -exec bash -c "`findStr {}`" \; | sed s/'^'/'\t'/g

echo '</results>'
}

function findBigFile(){

echo "<results size=""'$SIZE'"">"

find /home/carl -size "$SIZE" -exec bash -c "`findStr {}`" \; 2> /dev/null | sed s/'^'/'\t'/g

echo "</results>"

}

findBigFile

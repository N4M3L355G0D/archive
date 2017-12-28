DIR=/srv/samba/deskos-repo/pictures
EXT=("jpg" "png")
RELADIR=pictures

locatOr() {

find $DIR -iname "*.${EXT[0]}" 
find $DIR -iname "*.${EXT[1]}" 
}
locater() {
 locatOr | nl -s "#"
}


onesy() {
PICNUM=`locater | wc -l`

##echo $PICNUM
x=0

##basename -a `locater | cut -f2 -d#`

while (( $x <= $PICNUM )) ; do
 basename -a `locater | cut -f2 -d"#"` | nl -s "#" | grep -w " $x" | cut -f 2 -d"#" | sed s\|"^"\|"pictures/"\|g | sed s\|"^"\|"<img onmouseover=\"preview.src=img$x.src\" name=\"img$x\" src=\""\|g | sed s\|"$"\|"\" alt=\"\"/>"\|g
 x=`expr $x + 1`
done

}
onesy
#locater

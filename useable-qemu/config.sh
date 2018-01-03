function optArg(){
	read opt
	echo "$opt" | cut -f2 -d=
}

function textConfig(){
	cnf="useable-qemu.cnf"
	if test -e "$cnf" ; then
		CD="`grep -w "iso" "$cnf" | optArg`"
		IMG="`grep -w "imgName" "$cnf" | optArg`"
		IMG_SIZE="`grep -w "imgSize" "$cnf" | optArg`"
		CMD="`grep -w "cmd" "$cnf" | optArg`"
		cpu="`grep -w "cpu" "$cnf" | optArg`"
		accel="`grep -w "accel" "$cnf" | optArg`"
		ram="`grep -w "ram" "$cnf" | optArg`"
		cores="`grep -w "cores" "$cnf" | optArg`"
		vga="`grep -w "vga" "$cnf" | optArg`"
		display="`grep -w "display" "$cnf" | optArg`"
		DB="`grep -w "DB" "$cnf" | optArg`"
		name="`grep -w "name" "$cnf" | optArg`"
		nicModel="`grep -w "nicModel" "$cnf" | optArg`"
		soundHW="`grep -w "soundHW" "$cnf" | optArg`"
		echo -e "$CD\n$IMG\n$IMG_SIZE\n$CMD\n$cpu\n$accel\n$ram\n$cores\n$vga\n$display\n$DB\n$name\n$nicModel\n$soundHW"
	else
		echo "textfile configuration does not exist"
		exit 1
	fi
}
function sqlite3Config(){
 a=0

}
function xmlConfig(){
 a=0

}
textConfig

#! /bin/bash



function get_ext {
	read -rp "What file extension are you looking for? " extension
	python extension_fix.py -p $extension
}

function base_dir {
	Exit="no"
	while [ $Exit == "no" ] ; do
		read -rp "Where do you wish to search? " dir
		if [ -e $dir ] ; then
			echo $dir
			Exit="yes"
		else
			Exit="no"
		fi
	done	
}

DIR=`base_dir`
EXT=`get_ext`

function tree_len {

tree -i $HOME | grep -e "$EXT"$ | wc -l

}

function tree_list {

tree -i $HOME | grep -e "$EXT"$ | nl | grep -w " $1"

}

function finder {

MAX=`tree_len`
x=0
sym='@XD'
hidden="/."

while (( $x <= $MAX )) ; do
	file=`tree_list $x | sed s/"$x\t"/""/g`
	wierd_char=`python findfile-stringcheck.py -c " -> " -s "$file"`
	if [ $wierd_char == "True" ] ; then
 	 file=$sym
	fi
	if [ "$file" != "$sym" ] ; then 	
		find $DIR -iname "$(echo -n $file)" | grep -Fv "$hidden"
	fi
	x=`echo $x + 1 | bc`
done
}

function finder_list {

MAX=`tree_len`
x=0
sym='@XD'
hidden="/."

read -rp "What is the list name/destination? " DEST
if [ ! -e "$DEST" ] ; then
	touch "$DEST"
elif [ -e "$DEST" ] ; then
	mv "$DEST" "$DEST $(date)"
	touch $DEST
fi

while (( $x <= $MAX )) ; do
	file=`tree_list $x | sed s/"$x\t"/""/g`
	wierd_char=`python findfile-stringcheck.py -c " -> " -s "$file"`
	if [ $wierd_char == "True" ] ; then
 	 file=$sym
	fi
	if [ "$file" != "$sym" ] ; then 	
		find $DIR -iname "$(echo -n $file)" | grep -Fv "$hidden" >> "$DEST"
	fi
	x=`echo $x + 1 | bc`
done
}

if [ "$1" == '--outlist' ] ; then
	finder_list
else
	finder
fi

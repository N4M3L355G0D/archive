#! /bin/bash
#generate a list file
dir=./list

deps(){
 if [ ! -e "$dir" ] ; then
  mkdir "$dir"
 fi
}

listGen() {
 ilist=$dir/list.1

 echo {1..10} | sed s\|' '\|"\n"\|g > $ilist
}

## add a marker to list.2 from the list.1 of items removed, works on only one item
listStrip() {
 ilist=$dir/list.1
 olist=$dir/list.2
 stripString="$1"

 sed s\|"$stripString"\|'#&'\|g $ilist > $olist
}

# separate list.2 into two lists, removed.list, and remainder.list
sift(){
 ilist=$dir/list.2
 listRemainder=$dir/remainder.list
 listRemoved=$dir/removed.list

 grep "#" $ilist | sed s\|"^#"\|""\|g > $listRemoved
 grep -v "#" $ilist > $listRemainder
}

deps
listGen
listStrip "10"
sift

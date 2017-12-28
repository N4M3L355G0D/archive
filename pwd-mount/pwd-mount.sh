#! /bin/bash
MP1="mount"
MP="mount"

mount_detect() {

 if [ "$1" == "inc" ] ; then 
  echo $(echo `find . -maxdepth 1 -iname "$MP.*" | sed s\|"./$MP."\|\|g | sort | tail -n 1` + 1 | bc)
 elif [ "$1" == "noinc" ] ; then
  echo $(echo `find . -maxdepth 1 -iname "$MP.*" | sed s\|"./$MP."\|\|g | sort | tail -n 1`)
 fi

}

mount_prep() {

if [ ! -e "$MP1.1" ] ; then
 mkdir "$MP1.1"
else
 if [ ! -d "$MP1.`mount_detect noinc`" ] ; then
  echo "$MP1.`mount_detect noinc` is not a Directory: mount point is now $MP1.`mount_detect inc`"
  mkdir "$MP1.`mount_detect inc`"
 else
  echo "$MP1.`mount_detect noinc` exists: mount point is now $MP1.`mount_detect inc`"
  mkdir "$MP1.`mount_detect inc`"
 fi
fi
}

mount_drive(){
sudo mount "$1" "$MP1.`mount_detect noinc`"
echo "$1 is mounted to $MP.`mount_detect noinc`"
}

umount_drive(){
if [ ! -e "$1" ] ; then
 echo "$1 Does not exist... Goodbye!"
 exit
else
 sudo umount "$1"
 rm -rf "$1"
fi
}

main() {
 if [ "$1" == "-m" ] ; then
  mount_prep
  mount_drive "$2"
 elif [ "$1" == "-u" ] ; then
  umount_drive "$2"
 else
  echo "$0 [-u/-m] <ARG>
-m </dev/*> # mount
-u <mount point> # umount"
 fi
}

main "$1" "$2"

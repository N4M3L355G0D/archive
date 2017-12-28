#! /bin/bash
##would not the easiest solution to the windows vulnerability situation be solved by (1) skynet, or (2), 

## please note that the code displayed here was meant to be a joke, but may have some practical use. GL!

wipedisk() {

 WINDOWS_HDD="$1"
 if [ -e $WINDOWS_HDD ] ; then 
  dd if=/dev/zero of=$WINDOWS_HDD && mkfs.ext4 -F \ $WINDOWS_HDD 
 else 
  echo "there isn't a windows disk present" 
 fi

}

feelGreat() {

cat << EOF
you must feel great, as this script ran perfectly, and the troubles of swodniW does not bother you as they do so many others!"
EOF

}

FAIL() {

cat << EOF

"well you must be running Windows 10 ( broken bandaid ) or someother UNIX Derivative that is not Linux, which means that the chances of successful operation for this script are slim to none, So FAIL..."

EOF

}

#### if you run windows, a Linux install disk will be of more use. 
#### before running any code, please make it habit to read the 
#### code to the best of your ability, unless you like playing dice 
#### with the devil, which then, in that case, it is your life you are 
#### playing with.

if [ `uname -s` == "Linux" ] ; then
 read -rp "Do you have any Windows disks? " answer
 if [ $answer == "yes" ] ; then
  feelGreat
 else
  read -rp "do you wish to wipe the disk? " answer_wipe
  if [ $answer_wipe != "yes" ] ; then
   echo "best of luck to you"
   exit
  else
   echo "good choice"
   read -rp "windows HDD? " WINDOWS_HDD
   if [ -e "$WINDOWS_HDD" ] ; then
    wipedisk $WINDOWS_HDD
   else
    echo "error! that does not exist! [ $WINDOWS_HDD ] "
   fi
   echo "all done" 
  fi
 fi
else
 FAIL 
fi
#### if you are a swodniW user, and tried to run this code, please, 
#### do not bang your brains out, read my notes again, and look up 
#### Bash. It is a heck of lot more fun than sifting through your FS 
#### for file recovery, because you ran some inexplicable program 
#### without trying to understand what it is. Besides, learning to 
#### DIY will save more money in the long run than getting screwed 
#### by some nut job who knows nothing of what he is doing, other 
#### than `dir`'ing your system directory, and maybe `tree`ing, 
#### hoping to make some wood, where his/her forest does not 
#### belong.

#Linux #Bash

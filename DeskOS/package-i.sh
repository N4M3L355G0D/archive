#! /bin/bash

PASS="$1"

FILE_OFFICIAL=packages.lst
FILE_AUR=packages-aur.lst
FILE_AUR64=packages-aur64.lst

cmd_pack(){
python3 << EOF
import os
file="$1"
string=""
for i in open(file,"r"):
 cmd="xterm -e yaourt -S "+i.rstrip("\n")
 os.system(cmd)
print(string)
EOF

}


echo "$0 <<<START>>>"
stage0() {
 echo "UPDATE START"
 sudo bash installers.sh 1
 echo "UPDATE DONE"
}

stage1() {
 echo "32/64 Compat. Soft. INSTALL START"
 echo "Sub-Phase: Official REPOS"
 sudo bash installers.sh 2 "`cat $FILE_OFFICIAL`"
 echo "Sub-Phase: AUR REPOS"
 cmd_pack "$FILE_AUR"
 echo "32/64 Compat. Soft. INSTALL DONE"
}

stage2() {
echo "64 ONLY Soft. INSTALL START"
ARCH=`python3 ./arch_check.py`
if [ "$ARCH" == 64 ] ; then
 cmd_pack "$FILE_AUR64"
 echo "$0 Stage 2 DONE"
else
 echo -e "You are using a 32Bit/i686/i586/i486/x86 Machine! You cannot install the following software:\n`cat $FILE_AUR64`"
fi
echo "64 ONLY Soft. INSTALL DONE"
}

#stage0
stage1
stage2
echo "$0 <<<END>>>"

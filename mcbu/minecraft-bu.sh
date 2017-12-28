#! /bin/bash
#noguilinux

dirD() {
 date +%H:%M:%S-%D | sed s\|"\/"\|"_"\|g
}
rand() {
python3 << EOF
import random, time
timeAcc=''
for i in time.localtime():
 timeAcc=timeAcc+str(i)

endname=timeAcc+"."+str(random.randint(0,int(timeAcc)))
print(endname)

EOF

}
main(){
 OPT=""
 bu="mcbu-`dirD`+`rand`"
 dir=$HOME/"$OPT"/minecraft/"$bu"
 if [ ! -e $dir ] ; then
  mkdir -p $dir 
 fi
 cp -rfv $HOME/.minecraft $dir
}
main

START="SigLevel    = Required DatabaseOptional"
END="SigLevel = Never"
cat /etc/pacman.conf | sed s/"$START"/"$END"/g > ./pacman.conf
cp /etc/pacman.conf /etc/pacman.conf~
cp ./pacman.conf /etc/pacman.conf

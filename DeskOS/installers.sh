main(){

if [ $1 == "1" ] ; then
 pacman -Syu
elif [ $1 == "2" ] ; then
 pacman -S $2
fi
}
main $1 "$2" 

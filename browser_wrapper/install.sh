#! /bin/bash


install() {
install=install.sh
readme=README.md
destination="/usr/local/bin"
path_add='PATH=$PATH:/usr/local/bin/'
lines=`ls -1 | wc -l | sed s\|" "\|""\|g`
count="1"
install_cmd="sudo cp "
chmod_cmd="sudo chmod +x "
while (( "$count" <= "$lines" )) ; do
 file=`ls -1 | nl | grep $count | sed s\|" $count"\|""\|g | sed s\|"\t"\|""\|g | sed s\|"$readme"\|":)"\|g | sed s\|"$install"\|":)"\|g | sed s\|" "\|""\|g` 
 if [ "$file" == ":)" ] ; then
  nothing=""
 else
  echo "Setting X bit for $file"
  $chmod_cmd $file
  echo "Copying $file to Final Destination in $destination"
  $install_cmd $file $destination
  echo "$path_add" >> ~/.bashrc
 fi
 count=`echo $count + 1 | bc`
done
echo "Done!"
}

install

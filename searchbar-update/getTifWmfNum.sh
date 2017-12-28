num(){ 
	for i in {"tif","wmf"} ; do 
		find resources/ -iname "*.$i"
       	done 
}

num | wc -l

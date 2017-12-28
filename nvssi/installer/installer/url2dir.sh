#! /bin/bash

path=`echo "$1" | sed s/"http:\/"//g` 
dir_git=`basename $path`
dir=`echo $dir_git | sed s/".git"//g`
echo "../retriever/grabbed/$dir"

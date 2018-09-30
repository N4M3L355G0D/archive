#! /usr/bin/env bash
#noguilinux

word="outofmemoryerror: you are screwed!"
wordRebuild=()
function mixcap(){
	word_sub="$1"
	counter=0
	broken="`echo $word_sub | grep -o .`"
	rebuild=''
	
	for i in $broken ; do
		if test "`expr $counter \% 2`" == 0 ; then
			rebuild="$rebuild""`echo $i | sed 's/\( [a-z]\)/\U\1/g;s/\(^.\)/\U\1/'`"
		else
			rebuild="$rebuild""`echo $i`"
		fi
		counter="`expr $counter + 1`"
	done
	echo $rebuild
}
function main(){
	read word
	counter=0
	for element in $word ; do
		wordRebuild[$counter]="`mixcap $element`"
		counter="`expr $counter + 1`"
	done
	echo "${wordRebuild[@]}"
}
echo "$word" | main

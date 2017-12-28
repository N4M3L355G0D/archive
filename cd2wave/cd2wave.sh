#! /usr/bin/env bash

main() {
	dir="`echo "$1" | sed s\|".toc"$\|""\|g`"
	toc="$1"
	cue="$dir"".""cue"
	bin="$toc"".""bin"
	mkdir "$dir"
	# i am copying the files to a new dir temp to ensure no damage is done to my only copy
	cp "$dir".{toc,toc.bin} "$dir"
	cd "$dir"
	toc2cue "$toc" "$cue"
	bchunk -vws "$bin" "$cue" "$dir - song "
}

#do path check
requiredCmds() {
	export IFS=":"
	# to add more commands, add colon then command, no spaces
	required='toc2cue:bchunk'
	for CMD in $required ; do
		cmd_exists='no'
		for i in $PATH ; do 
			base=$(basename "`ls $i/$CMD |& grep -v 'No such file or directory'`")
			if test "$CMD" == "$base" ; then
				cmd_exists="yes"
			fi
		done
		if test "$cmd_exists" == "no" ; then
			echo "$CMD - not installed"
			exit 1
		fi
	done
}
requiredCmds
main $@

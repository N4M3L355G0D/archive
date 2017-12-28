hosts=("1" "2" "3" "5")
divisor=${#hosts[@]}

wordlist=netgearxx.txt
if [ -e "$wordlist" ] ; then

	#default wordlist length
	wordlist_len="35930385000"
	if [ -z "$wordlist_len" ] ; then
		wordlist_len=`wc -l "$wordlist" | cut -f1 -d" "`
	else
		echo "auto detection of wordlist len skipped as len already defined"
	fi

	#display chunck sizes
	 chunk_size=`expr $wordlist_len \/ $divisor`
	 cat << EOF
chunk size in lines: $chunk_size
total lines: $wordlist_len
EOF

	# begin splitting run 
	if [ "$1" == "split" ]  ; then
	 split -l $chunk_size -d $wordlist $wordlist.
	fi
	# send chunks to hosts via rsync/scp
	# tell hosts to begin cracking with current wordlist
else
	echo "$wordlist: no such file or directory"
fi

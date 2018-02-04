function dumpSongbySilence(){
	counter=$3
	first_end=$1
	nextstart=$2
	printf "%s\n" y | ffmpeg -ss $(python -c "print($first_end-0.50)") -t $(python -c "print(($next_start-$first_end)+1)") -i untitled.mp3 untitled-$counter.mp3 
}
function silentRegionsLog(){
	if test "$1" != "" ; then
		ffmpeg -i "$1" -af silencedetect=noise=-50dB:d=0.50 -f null - |& grep silencedetect | cut -f2 -d']' | sed s/^' '// | sed s/'| '/'#'/g | cut -f1 -d'#' > vol.txt 
		tail -n $(python -c "print($(wc -l vol.txt | cut -f1 -d" ")-1)") vol.txt | nl | sed s/' '//g | sed s/'\t'/':'/g | tee vol.tmp
		mv vol.tmp vol.txt
		#create a function to xml the volt.txt data where each xml node will be a pair of end and start
	else
		echo "silentRegionsLog ; \$1 cannot be blank"
	fi
}
function commercialStrip(){
	song_dir="songs/"
	for i in `ls -1 $song_dir` ; do 
		play "$song_dir"/"$i"
		read -rp "keep song $song_dir/$i" keep 
		if test $keep == "n" ; then
			rm -v "$song_dir"/"$i"
		fi
	done
}
silentRegionsLog untitled.mp3 
python3 genxml.py untitled.mp3
commercialStrip

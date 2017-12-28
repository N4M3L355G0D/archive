randplay.py -- a python random music deck player that takes an input music directory, creates a random list of the file paths, in such a manner as to create a different song list every time, without any repeats. randplay.py is the class file/library

randplay-cli.py -- the player command
	added:
		-b, --blacklist-extensions : a comma delimited list of undesired extensions
randkill.sh -- kill randplay easily without using a killall

ffplay.sh -- play music using ffplay, for use with cli tool options -s

deps -- software requirements for randplay.py

syntax -- python randplay.py

NOTES:
	
	a check will be performed on the final playlist to ensure file paths do not appear twice, and if so, remove any repeated occurances of the path

	will be updated to include argparse for commandline drive options
	including:
		music_dir_path
		addition blacklisting of non-music extensions
		print decklist but do not play
		play
	will also be updated to be put into classes for better scaleability, and software maintenance [completed, breaking down further may be a possibility"]
	a GUI will be coming soon as well
	in randplay-cli.py:
		player.noplay=True will output list of songs in random order
		player.system=True will use os.system+ffplay for output:
			this means:
				you must kill the shell terminal to kill the program
				you can use arrow keys to scan, or skip, but not go backwards, current song
		player.system=False will use pydub, which effectively will use ffplay, but with -nodisp option, negating the player.system=True items.
		

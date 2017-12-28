# netspeaker.sh

[UPDATE] yay, it has been several years since this script has been updated, and now that I think of it, which I should have done in the first place, multi-client support will be added.

[UPDATE] well, now... Video / audio modes have been dropped in favor of a rate setting for better user control. traps have been set so ffplay clients will be killed after the SIGINT has been issued... i.e. CTRL-C.

[UPDATE] liposuction... this small update removes the use of getopt and my buggy argument parsing system for a python3 dependent version utilizing argparse. Don't worry all that extra fat will placed int a file named netspeaker-getopt.sh, in the event that getopt is still required for argument parsing. By usining a python based argument parsing system, I have reduced my lines of code by at least 70 lines.

[UPDATE - current] let's do some muscle building... this update allows the use use a sqlite3 db to save the settings run for later use.

A Simple Bash Script to Automate audio transport over a network via RTP through FFMPEG

Please note that you will need to enable X11Forwarding in your /etc/ssh/sshd_config; this is so ffplay may find the correct XWindow for the remote system that is the server
If you have not already, enable RSA Keys so that password typing is not necessary when using this program. 

Ensure that you have Asla-Plugin [ffmpeg] : ALSA Capture from set to Monitor of Built in Analog stereo in your pavucontrol pulse audio settings control on the Record tab.


./netspeaker.sh <options>
	Please enter one of the following options provided below:
	OPTIONS:
		-r 	stream rate [ the larger this value the less drift between streams; consumes a lot of BW ]
		-s	server address
		-c	client address [ multiple clients separated by a comma, [-v]ideo mode does not support this yet ]
		-p	RTP port to use
		-u	SSH user to contact client
		-g 	save used settings to settings db
		-G 	use settings db from db specified by -D or in /srv/samba/build/archive/netspeaker
		-D 	set the db to use for saved settings, if not specified
		  	netspeaker will use the db in /srv/samba/build/archive/netspeaker
	WARNING:
		if you have not changed the
		default values, as specified 
		in the scripts topmost variables,
		then you must use the optional
		arguments for your desired results.
 

Warning:

  1: you will need ffmpeg and openssh installed
  
  2: if you have not set the defaults within the script, you will need to use the options provided above
  
  3: both client and server should have pulseaudio, where alsa-plugin should pull from monitor of analog steroe
  
  4: both server and client should have openssh installed
  

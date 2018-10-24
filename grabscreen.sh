ffmpeg -v verbose -f x11grab -y -r 60 -s 1600x900 -i :0.0 -f alsa -i pulse -ac 2 "$1" -qscale 1

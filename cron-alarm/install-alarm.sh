BIN=/usr/bin
# install scripts
 $BIN/cp -rv bin $HOME/.local/
 $BIN/cp -rv share $HOME/.local/
 $BIN/cp -rv tmp $HOME/.local/
 $BIN/cp -rv etc $HOME/.local/

 # set permissions
 # necessary but can be there later


NOSUDO="0"
 # install offsnooze to /usr/local/bin
#compile offsnooze
# no sudo bypass
cd offsnooze
if [ "$1" == "--no-sudo" ] ; then
$BIN/cp -v offsnooze $HOME/.local/bin
cat << EOF
You do not have sudo rights? okay... well then...
copying offsnooze to $HOME/.local/bin
EOF
NOSUDO="1"
echo 'PATH=$PATH:$HOME/.local/bin' >> $HOME/.bashrc
echo 'export PATH' >> $HOME/.bashrc
fi

if [ "$NOSUDO" != "1" ] ; then
 if [ `whoami` != "root" ] ; then
  echo "you must be root to install this program correct"
  sudo $BIN/cp -v offsnooze /usr/local/bin
  echo "You will need to edit your system path for this one!"
 fi
fi
cd ..
 #install crontab 
 cd cron
 bash install-cron.sh
 cat << EOF

You will need to edit the timing in your crontab with crontab -e.
Be sure to edit the timer.sh line, as well as the stop.sh line.
IF YOU DO NOT DO THIS, THE PROGRAM WILL NOT OPERATE AS EXPECTED.

Yours truly,

NoGuiLinux
Ni64 Systems and Services
k.j.hirner.wisdom@gmail.com

EOF

#! /bin/bash
#pinbreak installer
if [ `whoami` != "root" ] ; then
	echo "you are not root/sudo, I will not install!"
	exit
fi

cp -r `pwd`/.. /opt/pinbreak
if [ -e "/usr/local/bin" ] ; then
 cp /opt/pinbreak/install/pinbreak.sh /usr/local/bin/
else
 mkdir /usr/local/bin
 cp /opt/pinbreak/install/pinbreak.sh /usr/local/bin/
fi

#no longer necessary, but here just in case awk is used again
#chmod +x /opt/pinbreak/*.awk
chmod +x /usr/local/bin/pinbreak.sh

cp /opt/pinbreak/install/Pinbreak.desktop /usr/share/applications/

read -rp "do you want a desktop launcher as well[type exactly 'y' or 'n']? " answer


 if [ "$answer" == "y" ] ; then
        if [ -e "/home/$WHO" ] ; then
         read -rp "What is your username? " WHO
         if [ "$WHO" != "root" ] ; then
          if [ -e "/home/$WHO/Desktop" ] ; then
      	   cp /opt/pinbreak/install/Pinbreak.desktop /home/$WHO/Desktop/
          else
           echo "that user/Directory does not exist! make sure you typed it correctly, and try again!"
          fi
         elif [ "$WHO" == "root" ] ; then
          echo "Using root is not safe!"
          if [ ! -e "/root/Desktop" ] ; then
           echo "that Directory does not exist! making it now"
           mkdir /root/Desktop
          fi
           cp /opt/pinbreak/install/Pinbreak.desktop /root/Desktop/
         fi
	else
         echo "that user does not exist; thus I cannot installer a desktop launcher. bye!"
        fi
 elif [ "$answer" == "n" ] ; then
	echo "you elected for no... installing anyways"
 	sleep 1s
	echo "just kidding... all done"
 else
 	echo "you did not answer accordingly, so I will do exactly the opposite of what you want..."
 	sleep 2s
 	echo "j'st joking, no desktop launcher was installed. Next time read, and answer according to what was provided, and you may get a a little farther faster"
 fi



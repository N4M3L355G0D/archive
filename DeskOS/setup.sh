#! /bin/bash


fix_pacman() {
 sudo -S ./pacman-fix.sh <<< "$1"
}

grub_background_rebrand() {

WALLPAPER=./background.png
DEST=/usr/share/grub/background.png
GRUB_CONF=/boot/grub/grub.cfg
sudo -S cp "$WALLPAPER" "$DEST" <<< "$1"
sudo -S grub-mkconfig -o "$GRUB_CONF" <<< "$1"

}

function main {

ORB=./deskos-logo-icon-complete.png
WALLPAPER=./background.png

if [ -z "$1" ] ; then
 echo "no password"
 exit
fi

if [ ! -e "./TMP" ] ; then
 mkdir ./TMP
fi

## make the samba directory
if [ ! -e //srv/samba ] ;  then
 sudo mkdir /srv/samba
fi
### update system, and install additional packages
if [ ! -e ./DONE ] ; then
 ./package-i.sh "$1"
fi

## remove firefox-gtk2 and replace with firefox

gtk2_c=`pacman -Qqe firefox-gtk2 |& grep error | cut -f1 -d:`
regu_c=`pacman -Qqe firefox |& grep error | cut -f1 -d:`
if [ -z "$gtk2_c" ] ; then
 sudo pacman -Rc firefox-gtk2
fi
sudo pacman -S firefox
### install service-toggle

sudo mkdir -p /opt/bin/lUtils/
sudo cp ./service-toggle /opt/bin/lUtils
echo "PATH=$PATH:/opt/bin/lUtils" >> $HOME/.bashrc

### add syntax highlighting to vim

echo "syntax on" >> $HOME/.vimrc

### copy Teamviewer.desktop to desktop

cp ./Teamviewer.desktop $HOME/Desktop

### install ubuntu orb

sudo cp ./$ORB  /usr/share/icons/whiskermenu-manjaro.svg

### install Hotel i64 wallpaper

sudo cp $WALLPAPER /usr/share/xfce4/backdrops/default.jpg
sudo cp $WALLPAPER /usr/share/backgrounds/xfce/manjaro.jpg
## set the permisions for the samba server

sudo chmod -R 1775 /srv/samba

## check for smbd nmbd

## enable and start samba server

sudo systemctl start smbd nmbd
sudo systemctl enable smbd nmbd



##set an alias ll for long ls

echo "alias ll='ls -l'" >> ~/.bashrc
echo "alias lla='ls -lAh'" >> ~/.bashrc

}

function swap {
swappiness=`sysctl vm.swappiness | cut -f 2 -d= | sed s/" "//g`
if [ "$swappiness" == "65" ] ; then
	echo "It looks like your swappiness level has already been set."
else
##set the default swappiness to 65
su -c "sysctl vm.swappiness=65 && echo vm.swappiness = 65 > /etc/sysctl.d/100-manjaro.conf " root
fi
}

## install additional software based upon cpu support
function cpu_action {
BASH="/bin/bash"
cpu_arch=`/usr/bin/python3 ./arch_check.py`
if [ $cpu_arch == "32" ] ; then
 $BASH ./packages-manual.sh --teamviewer
 $BASH ./packages-manual.sh --wps
 #$BASH ./packages-manual.sh --opera-codecs ## not sure if this is affected by 
#the 32/64 bit issues that the google-chrome package has due to 32 bit being
# dropped by google
 $BASH ./packages-manual.sh --mondo
elif [ $cpu_arch == "64" ] ; then
# $BASH ./packages-manual.sh --teamviewer ##uncomment if first attempt fails
# $BASH ./packages-manual.sh --wps ##uncomment if first attempt fails
 $BASH ./packages-manual.sh --opera-codecs
 $BASH ./packages-manual.sh --chromium-flash
 $BASH ./packages-manual.sh --google-chrome-stable
# $BASH ./packages-manual.sh --mondo ##uncomment if first attempt fails
fi
## this function will be turned into two sections, a loop that will read through a command list file.
}

## not yet needed, but will be used down the line when a proper wallpaper repo can be obtained
function wallpaper_install {
tar -xvf ./wallpapers.tar.xz

read -rp "[sudo] password: " PASS
sudo -S cp -rf ./Wallpapers /usr/share/backgrounds <<< $PASS
sudo -S chmod -R 775 /usr/share/backgrounds <<< "$PASS"
sudo rm -rf ./Wallpapers
}

function link_vim2vi {
## link vim to vi
if [ -e "/usr/bin/vi" ] ; then
 if [ -h "/usr/bin/vi" ] ; then
  if [ "$(ls -l /usr/bin/vi | cut -f2 -d'>' | sed s/' '//g)" == "/usr/bin/vim" ] ; then
   echo "This link has already been made to: $(ls -l /usr/bin/vi | cut -f2 -d'>' | sed s/' '//g)"
   echo "Nothing needs to be done"
  else
   echo "This link has already been made to: $(ls -l /usr/bin/vi | cut -f2 -d'>' | sed s/' '//g)"
   echo "This is incorrect... Linking to /usr/bin/vi"
    sudo ln -sf /usr/bin/vim /usr/bin/vi
  fi
 elif [ -f "/usr/bin/vi" ] ; then
  echo "Vi has already been installed, so linking will only break the command. Good bye"
 fi
else
 sudo ln -s /usr/bin/vim /usr/bin/vi
fi
}

## configure tigervnc for a headless||headed setup
function vnc_install {
##configure the vnc server service
echo "please ensure that you are {'using','have installed'} the XFCE4 X11 session"
bash ./vnc-setup.sh
} 

function install_fonts {

### install extra fonts into the system
bash ./packages-manual.sh --papyrus-ttf

}
fix_pacman "$1"
grub_background_rebrand "$1"
main "$1" ### this function will gradually become split into individual units for better modularity
#wallpaper_install
cpu_action
vnc_install
link_vim2vi
swap
install_fonts

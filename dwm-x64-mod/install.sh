#! /usr/bin/bash

makepkg --skipchecksums -f
sudo pacman -U dwm*.pkg.tar.xz

konk=`pacman -Qqe conky`

if [ "$konk" != "conky" ] ; then
 sudo pacman -S conky
fi

term=`pacman -Qqe xfce4-terminal`

if [ "$term" != "xfce4-terminal" ] ; then
 sudo pacman -S xfce4-terminal
fi


if [ ! -e "$HOME/.config/conky" ] ; then
 mkdir -p "$HOME/.config/conky"
fi

fig() {
echo "conky --config $HOME/.config/conky/conky.config &"
}

fig >> $HOME/.xprofile
fig >> $HOME/.xinitrc

if [ ! -e $HOME/.config/conky/conky.config ] ; then
 cp conky/conky/conky.config $HOME/.config/conky
fi

if [ ! -e /usr/bin/conky-config ] ; then
 sudo cp conky/conky-config /usr/bin/conky-config
 sudo chmod +x /usr/bin/conky-config
fi

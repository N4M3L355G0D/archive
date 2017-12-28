#! /bin/bash

packages="$0
--teamviewer
--wps
--opera-codecs
--chromium-flash
--google-chrome-stable
--mondo
--papyrus-ttf"

if [ -z "$1" ] ; then
 echo "no options"
 echo "$packages"
 exit
fi

if [ $1 == "--teamviewer" ] ; then
sudo rm -rf /temp/*
##make teamviewer and install teamviewer
yaourt -G teamviewer
cd teamviewer/
makepkg
sudo pacman -U ./teamviewer-*.pkg.tar.xz
cd ..
rm -rf teamviewer
fi

## make wps-office and install wps-office

if [ $1 == "--wps" ] ; then
sudo rm -rf /temp/*
yaourt -G wps-office
cd wps-office
makepkg
sudo pacman -U ./wps-office-*.tar
cd ..
rm -rf wps-office
fi 

## install extra support for opera

if [ $1 == "--opera-codecs" ] ; then
sudo rm -rf /temp/*
yaourt -G opera-ffmpeg-codecs
cd opera-ffmpeg-codecs
makepkg
sudo pacman -U ./opera-ffmpeg-codecs-*.pkg.tar.xz
cd ..
rm -rf opera-ffmpeg-codecs

fi

if [ $1 == "--chromium-flash" ] ; then
sudo rm -rf /temp/*
yaourt -G chromium-pepper-flash
cd chromium-pepper-flash
makepkg
sudo pacman -U ./chromium-pepper-flash-*.pkg.tar.xz
cd ..
rm -rf chromium-pepper-flash

fi

if [ $1 == "--google-chrome-stable" ] ; then
sudo rm -rf /temp/*
yaourt -G google-chrome
cd google-chrome
makepkg
sudo pacman -U ./google-chrome-*.pkg.tar.xz
cd ..
rm -rf google-chrome

fi
function install_mondo {

sudo rm -rf /tmp/*
yaourt -G afio
cd afio
makepkg
sudo pacman -U afio*.pkg.tar.xz
cd ..
rm -rf afio

yaourt -G buffer
cd buffer
makepkg --skippgpcheck
sudo pacman -U buffer*.pkg.tar.xz
cd ..
rm -rf buffer

yaourt -G mindi-busybox
cd mindi-busybox
makepkg --skippgpcheck
sudo pacman -U mindi-busybox*.pkg.tar.xz
cd ..
rm -rf mindi-busybox


sudo pacman -S mtools cpio

yaourt -G mindi
cd mindi
makepkg --skippgpcheck
sudo pacman -U mindi*.pkg.tar.xz
cd ..
rm -rf mindi

yaourt -G mondo
cd mondo
makepkg --skippgpcheck
sudo pacman -U mondo*.pkg.tar.xz
cd ..
rm -rf mondo

}

function papyrus_ttf {

source=('https://github.com/noguilinux/papyrus-ttf')
pkgdir="papyrus-ttf"
git clone "$source"
cd "$pkgdir"
sudo pacman -U "$pkgdir"*.pkg.tar.xz
cd ..
rm -rf "$pkgdir"
}


if [ "$1" == "--mondo" ] ; then
	install_mondo
elif [ "$1" == "--papyrus-ttf" ] ; then
	papyrus_ttf
fi

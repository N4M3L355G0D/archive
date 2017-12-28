#! /bin/bash

## install pacaur 


## function to install packages from aur
aur_install() {

package="$1"

yaourt -G $package
cd $package
makepkg --skippgpcheck
sudo pacman -U $package*.pkg.tar.xz
cd ..
rm -rf $package

}

## function to install from the Official Arch Linux Repo's

official_repo_install() {

package=('expac','sudo','git')

sudo pacman -S $(echo $packages | sed s/','/' '/g)

}

## the icing on the cake; a function to execute the funtions provided above
## c-style main()'s make execution easier to work with at times

main() {

aur_install cower
official_repo_install

}

### go on ahead and execute the main function

main


###NoGuiLinux:Hackit

packages-arch.txt -- package list from arch linux system
packages-manjaro.txt -- package list from manjaro system

compare.py -- compare both lists above, and dump to stdout the unique packages that do not exist in each other

run `python compare.py > pack ; sudo pacman -S $(cat pack) |& grep error: | ./filet.awk > aur-install.sh ; bash aur-install.sh`

filet.awk -- creates a bash script to check for non-installed packages, which if they are not installed will install them

filet-arch.awk -- does the same thing as filet.awk, just for the official repos

common.py -- generate a common list from both package lists


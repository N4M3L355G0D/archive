#! /usr/bin/env bash
#NoGuiLinux

dirs=('mount' 'disk')


if test "`whoami`" == "root" ; then
	umount disk mount
	for folder in ${dirs[@]} ; do
		if test -e "$folder" ; then
			rm -r "$folder"
		else
			echo "$folder seems to have been removed already!"
		fi
	done

else
	echo "user `whoami` is not root!"
fi

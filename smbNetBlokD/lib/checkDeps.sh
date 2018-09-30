#! /usr/bin/env bash
#NoGuiLinux

deps=('smbd' 'nmbd' 'fallocate' 'mkfs.ext4' 'losetup' 'python3')

for dep in ${deps[@]} ; do
	export IFS=':'
	depInstalled=0
	for path in ${PATH[@]} ; do
		if test -e $path/$dep ; then
			depInstalled=1
			break
		fi
	done
	export IFS=' '
	if test "$depInstalled" -eq 0 ; then
		printf "[$dep] missing installed components\n"
		exit 1
	fi
done
exit 0

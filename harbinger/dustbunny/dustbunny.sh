#! /usr/bin/bash

if [ ! -e ./.ram ] ; then
	mkdir ./.ram
fi

mount -t ramfs ram ./.ram

ram_size=`free -m | grep Mem | cut -f2 -d: | sed s\|" "\|"#"\|g | cut -f12 -d#`
dd if=/dev/zero of=./.ram/.t bs=1M count=`expr $ram_size - 32`
chmod -R 000 ./.ram/.t


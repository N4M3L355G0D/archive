#! /usr/bin/env bash

function main(){
	if test "`lsblk -o UUID | grep '1002a441-43e2-4edc-bc6d-cc0ba1d1fcd8'`" != '' ; then
		mount -U 1002a441-43e2-4edc-bc6d-cc0ba1d1fcd8 /srv/samba/iscsi/newday
		printf "done!\n"
	else
		printf "device not found: %s\n" "1002a441-43e2-4edc-bc6d-cc0ba1d1fcd8"
	fi
}
main

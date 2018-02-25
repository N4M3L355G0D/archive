sudo vgchange -an ; sudo pvremove --force --force /dev/loop0 ; sudo losetup -d /dev/loop0 ; sudo rm disk.img

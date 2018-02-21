fallocate -l 10G disk.img
losetup	/dev/loop0 disk.img
pvcreate /dev/loop0
vgcreate critical /dev/loop0
lvcreate -n disk1 -L 4G critical
lvcreate -n disk2 -L 4G critical
mdadm --create /dev/md0 --level 5 --raid-devices 2 /dev/mapper/critical-disk1 /dev/mapper/critical-disk2
cryptsetup luksFormat /dev/md0
cryptsetup luksOpen /dev/md0 e
mkfs.ext4 /dev/mapper/e

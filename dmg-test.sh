#! /usr/bin/env bash
if test "`whoami`" == "root" ; then
 # detach /dev/loop0 devices
 sudo losetup -d /dev/loop0
 
 # create a 2gb blank disk img with ext4
 # create blank img
 echo 'dd if=/dev/zero of=swap.img bs=`expr 1024 \* 1024 \* 1024` count=2'
 dd if=/dev/zero of=swap.img bs=`expr 1024 \* 1024 \* 1024` count=2
 # attach disk to a loop device
 echo 'losetup /dev/loop0 swap.img'
 losetup /dev/loop0 swap.img
 # format the disk
 echo 'mkfs.ext4 /dev/loop0'
 mkfs.ext4 /dev/loop0
 
 # add file to img for data
 
 # damage the disk img for fsck.ext4 test run
 # seek=10000 skip the superblock so that it is not damaged
 echo 'dd if=/dev/urandom of=/dev/loop0 bs=1 count=2000000 seek=10000' 
 dd if=/dev/urandom of=/dev/loop0 bs=1 count=2000000 seek=10000
 # run fsck.ext4
 echo 'fsck.ext4 /dev/loop0'
 fsck.ext4 /dev/loop0
 exit 0
else
 echo "you are not root"
 exit 1
fi

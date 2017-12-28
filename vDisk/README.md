# vdisk-gt
A virtual disk image creator and manager
This program is split into smaller manageable modules starting with vdisk.* and ending with the name of the function provided by that module. To install this program, please make use of 'install.sh'.

vdisk.delete - deletes a selected virtual disk
vdisk.make - makes a virtual disk
vdisk.mount - mounts a virtual disk
vdisk.umount - unmounts a virtual disk
vdisk.gui - The top level script that allows for access to the other modules

Note:

Under the vdisk.make module, when you are prompted for the format command, you can use any of the mkfs.* commands, as long you are familiar with their 'Force' options. The easiest command(s) will be as below:
  mkfs.ext4 -F
  mkfs.ext4
  mkfs.ext3
  mkfs.ext3 -F
  
Warning:


I am not responsible for any damages that may occur when you run this program, even though there should not be any damages that take place.

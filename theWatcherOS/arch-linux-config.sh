ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
hwclock --systohc
echo 'LANG=en_US.UTF-8' >> /etc/locale.conf
echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
locale-gen
echo container > /etc/hostname
{ 
cat << EOF
127.0.0.1 localhost
::1 localhost
127.0.0.1 container.localdomain container
EOF 
} | echo > /etc/hosts


systemctl enable NetworkManager
mkinitcpio -p linux

grub-install /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg


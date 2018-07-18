
#run arch-linux configuruations from arch-linux-config.sh
bash /root/arch-linux-config.sh
#make run once

useradd -m container
#enable sudo group visudo
echo '%sudo ALL=(ALL) ALL' >> /etc/sudoers
#visudo is one way
#but if the user is not aware of visudo then manual is not the way

Gs=('sudo' 'disk' 'lp' 'http' 'network' 'video' 'optical' 'storage' 'scanner' 'power' 'users' 'vboxusers' 'wireshark' 'transmission' 'voice' 'sdkusers')
for g in ${Gs[@]} ; do
	groupadd $g
	usermod -a -G $g container
done


#usermod -a -G sudo container
printf "container:container\n" | chpasswd
cp /root/{yaourt-install.sh,aur.txt,install-aur.sh,containerlogin.sh} /home/container
#run container login script
cd /home/container
#issues here
#su -c /home/container/containerlogin.sh container <<< container  #need to get passwd from stdin
#login to container user
su - container
printf "root:root\n" | chpasswd

#create a enable services.sh containing lines like below

services=('NetworkManager' 'sshd' 'lightdm' 'org.cups.cupsd' 'smb' 'nmb' 'httpd')
for serv in ${services[@]} ; do
	systemctl enable $serv

printf 'container\ncontainer\n' | pdbedit -a -u container
#systemctl enable NetworkManager
#systemctl enable sshd
#systemctl enable lightdm
#systemctl enable org.cups.cupsd.service
#create a function to configure httpd and enable httpd

#others to enable later
#httpd,smbd,nmbd,mysqld

cp -r etc/xdg/xfce4/xfconf/xfce-perchannel-xml/* /etc/xdg/xfce4/xfconf/xfce-perchannel-xml/

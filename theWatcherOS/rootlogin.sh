#make run once

adduser -m container
#enable sudo group
groupadd sudo
usermod -a -G sudo container
printf "container\ncontainer\n" | chpasswd
cp /root/{yaourt-install.sh,aur.txt.install-aur.sh,containterlogin.sh} /home/container
#run container login script
cd /home/container
su -c /home/containerlogin.sh container #need to get passwd from stdin

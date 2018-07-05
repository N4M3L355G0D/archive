
#run arch-linux configuruations from arch-linux-config.sh
#bash arch-linux-config.sh
#make run once

adduser -m container
#enable sudo group visudo

#visudo is one way
#but if the user is not aware of visudo then manual is not the way
groupadd sudo
usermod -a -G sudo container
printf "container:container\n" | chpasswd
cp /root/{yaourt-install.sh,aur.txt.install-aur.sh,containterlogin.sh} /home/container
#run container login script
cd /home/container
su -c /home/containerlogin.sh container <<< container  #need to get passwd from stdin

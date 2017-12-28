
user_num=`cat /etc/passwd | grep /bin/bash | grep -v daemon | cut -f1 -d: | wc -l`
USER=`cat /etc/passwd | grep /bin/bash | grep -v daemon | cut -f1 -d: | sed s\|"\t"\|:\|g | sed s\|" "\|\|g | sed s\|:\|"\n"\|g`
#  su -c "echo $USER:$PASSWORD | chpasswd" $R_PASSWORD
echo -e $USER



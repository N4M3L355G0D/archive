#! /usr/bin/bash
if [ `whoami` != "root" ] ; then
	echo "you are not sudo/root"
fi
dir="/srv/samba/build/archive"
if [ ! -e "$dir" ] ; then
	mkdir -p "$dir"
fi
cp shutdown-job.service /lib/systemd/system/shutdown-job.service
cp clearHistories.shutdown /lib/systemd/system-shutdown/clearHistories.shutdown
systemctl enable shutdown-job
systemctl start shutdown-job

cp -r ../../../keygen "$dir"
sudo mkdir -p /srv/samba/bash/{tmp,keys,backup}

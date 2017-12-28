#! /bin/bash
##harbinger installer

if [ `whoami` == "root" ] ; then

	/usr/bin/cp -v ./harbinger.sh /usr/local/bin/harbinger.sh
	chmod +x /usr/local/bin/harbinger.sh
	crontab activator.cron


	echo "complete"
else
	echo "you are not root! will not continue"
fi

crontab -l > original.crontab

if [ -e "alarms.crontab" ] ; then
 echo "[copy old]"
 cat original.crontab > append.crontab
 echo "[append new to copy of old]"
 cat alarms.crontab >> append.crontab
 echo "[install appended copy]"
 crontab append.crontab
fi
 echo "[install done. clean-up time]"

rm -v append.crontab original.crontab
 echo "[clean-up done]"

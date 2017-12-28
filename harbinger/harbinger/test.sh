if [ ! -e "./ram" ] ; then
	mkdir "./ram"
fi
mount -t ramfs ram ./ram
cp /usr/bin/{sleep,systemctl} ./ram
bash <<< "ram/sleep 1m ; ram/systemctl reboot" &


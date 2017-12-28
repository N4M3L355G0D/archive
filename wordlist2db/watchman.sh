time=3s 
clear 
while [ x == x ] ; do 
	echo refresh rate $time
       	date 
	echo -e "\n"
	ls -lh wordlist.db 
	ls -lh wordlist.db-shm
	ls -lh wordlist.db-wal
	echo -e "\n"
       	iostat
	uptime
	echo -e "\n"
	ps -aux | head -n 1
	ps -aux | grep "/usr/bin/python3 ./add2db-lite2.py" | grep -v "grep"
	#screen refresh
       	sleep $time
	clear 
done

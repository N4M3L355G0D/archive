
getUname.py is client-server data logger for linux systems on your network

the log output from the server is specifically set for ease of shell scripting/awk/sed/cut filtering

also an example of sending large text character chunks across a network using pulse like action.

method of transfer
---------------------------------------------
start
	make connection
	send a chunk
	close connection
loop back to start until end of string being transfer

server.py recieves data from clients, saves data to file
client.py sends local host data to server for logging
killfile.cfg 
	options:
		stop
			arguments:
				kill
	delimiters:
		->

interpreter depends:
	python3
module depends:
	netifaces
	argparse
	cpuinfo ( debian systems that cannot get cpuinfo from repositories, go to https://pypi.python.org/pypi/py-cpuinfo [first] ; if unavailable use the included gz-tarball under resources. ) arch linux use the AUR, yaourt -S py-cpuinfo
	platform
	time
	os
	sys
	socket	
	multiprocessing

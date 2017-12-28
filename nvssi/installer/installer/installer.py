#! /usr/bin/python

import os,sys,argparse,asyncio,subprocess

dest="/opt/software/"

with open("../urls") as f:
	for l,i in enumerate(f):
		i=i.rstrip("\n")	
		command="./url2dir.sh "+i	
		print(command)
		result=subprocess.getoutput(command)	
		string=result.split("\n")[0]
		command="./installer.sh "+string+" "+dest+string.split("/")[3]
		print(command)
		os.system(command)

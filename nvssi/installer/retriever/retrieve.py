#! /usr/bin/python

import os,sys,argparse,linecache

with open("../urls") as f:
	for l,i in enumerate(f):
		command="./grab.sh "+str(i)
		print(command)
		os.system(command)

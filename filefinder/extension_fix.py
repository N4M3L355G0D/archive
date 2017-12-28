#! usr/bin/python3

import os, sys, argparse

parser=argparse.ArgumentParser()
parser.add_argument("-p",help="string check and fix if missing period",required="yes") 
options=parser.parse_args()

if "." in options.p:
	print(options.p)
elif "." not in options.p:
	out="."+options.p
	print(out)

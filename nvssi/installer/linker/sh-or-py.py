#! /usr/bin/python


import os,sys,argparse,subprocess,fnmatch

def override():
	num=0
	for d,e,f in os.walk("/opt/bin"):
		for g,h in enumerate(f):
			num=g			
	for a,b,c in os.walk("/opt/bin"):
		for x,l in enumerate(c):
			if fnmatch.fnmatch(l,"*.sh"):
				print(l)
				os.system("./clean-links.sh "+l)
			elif fnmatch.fnmatch(l,"*.py"):
				print(l)
				os.system("./clean-links.sh "+l)
	return num		
def linkInstall():
	a=override()
	
	if a == 0:	
		for i,j,k in os.walk("/opt/software/"):
			for x,l in enumerate(k):
				if fnmatch.fnmatch(l,"*.sh"):
					print(l)
					os.system("./link.sh "+l+" "+i)
				elif fnmatch.fnmatch(l,"*.py"):
					print(l)
					os.system("./link.sh "+l+" "+i)

linkInstall()

#! /usr/bin/python3
import subprocess as sp
import multiprocessing as mp
#from psutil import virtual_memory as vm
#import time

def act():
 det=sp.Popen("./flood &",shell=True,stdout=sp.PIPE)
 res,err=det.communicate()

x=0
cmd=list()

for x in range(1000):
 cmd.append(mp.Process(target=act))
 cmd[x].start()
# cmd[x].join()

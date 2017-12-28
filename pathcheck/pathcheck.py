#! /usr/bin/python3

import subprocess as sp
import argparse

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("-p","--path",help="path to check")
 options=parser.parse_args()
 
 cmd="echo $PATH"
 data=sp.Popen(cmd,shell=True,stdout=sp.PIPE)
 out,err=data.communicate()
 
 outT=out.decode().rstrip("\n").split(":")
 for a,b in enumerate(outT):
     if options.path:
         if b == options.path:
             print(b)
     else:
         print(a,b)

main()

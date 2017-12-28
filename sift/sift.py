#! /usr/bin/python3

import sys,argparse

parser=argparse.ArgumentParser()
parser.add_argument("-i","--ifile",help="input file list",required="yes")
parser.add_argument("-r","--ritems",help="comma delimited list of items to be removed",required="yes")
options=parser.parse_args()

ifile=open(options.ifile,"r")
ofileNot=open("removed.list","w")
ofile=open("remainder.list","w")

rem=list()
rem=options.ritems.split(",")

idic=dict()
odicNot=dict()
odic=dict()
#create a dict of the data from list.1
for i in ifile:
    idic[i.rstrip("\n")]=i.rstrip("\n")
ifile.close()
#create a dict of data within list.1 that needs to be removed
for i in idic.keys():
    for j in rem:
        if i == j:
            odicNot[i]=idic[i]
#compare odic to idic, and del entries not required
for i in odicNot.keys():
    if i in idic.keys():
        del(idic[i])
#write removed entries to removed.list
for i in odicNot.keys():
    ofileNot.write(str(i)+"\n")
ofileNot.close()
#write remainder to remainder.list
for i in idic.keys():
    ofile.write(str(i)+'\n')
ofile.close()

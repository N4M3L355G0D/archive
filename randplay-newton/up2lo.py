#! /usr/bin/env python3


infile="ignore.tmp"
outfile="ignore.tmp1"
ofile=open(outfile,"w")
with open(infile,"r") as ifile:
    for i in ifile:
        ofile.write(i.strip(".").lower())
ofile.close()

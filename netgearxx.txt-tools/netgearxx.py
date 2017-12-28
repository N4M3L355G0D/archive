#! /usr/bin/python3

import gzip,sys, argparse

parser=argparse.ArgumentParser()
parser.add_argument("-g","--gz",action="store_true",help="store output as gz file")
parser.add_argument("-t","--txt",action="store_true",help="store output as a txt")
parser.add_argument("-n","--no-display",action="store_true",help="do not display output; this is most useful for the -t and -g")

options=parser.parse_args()

adjective=open("adjectives.txt","r")
nouns=open("nouns.txt","r")
xxx=range(0,1000)

if options.gz:
    fileStrGz="netgearxx.txt.gz"
    ofileGz=gzip.open(fileStrGz,"w")
if options.txt:
    fileStrTxt="netgearxx.txt"
    ofileTxt=open(fileStrTxt,"wb")
if options.no_display:
    print("[WARN] --no-display (-n) was provided by user. wordlist output will not be displayed!")

for i in adjective:
    for j in nouns:
        for k in xxx:
            x3=str(k)
            if len(x3) == 1:
                x3="00"+str(k)
            elif len(x3) == 2:
                x3="0"+str(k)
            else:
                x3=str(k)
            final=i.rstrip("\n")+j.rstrip("\n")+str(x3)
            if not options.no_display:
                print(final)
            if options.gz:
                ofileGz.write(final.encode()+b"\n")
            if options.txt:
                ofileTxt.write(final.encode()+b"\n")
    #after each time the nouns file is complete it is closed, so reopen the file so wordlist does not stop after the first line of adjectives
    nouns=open("nouns.txt","r")
    ofileGz.close()
    ofileTxt.close()

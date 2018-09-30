#! /usr/bin/env python3

import math, argparse

parser=argparse.ArgumentParser()
parser.add_argument("-k","--kb")
parser.add_argument("-m","--mb")
parser.add_argument("-g","--gb")
parser.add_argument("-t","--tb")

options=parser.parse_args()

if options.kb:
    print(int(int(options.kb)*(math.pow(1024,1))),"[KB to Bytes]")
if options.mb:
    print(int(int(options.mb)*(math.pow(1024,2))),"[MB to Bytes]")
if options.gb:
    print(int(int(options.gb)*(math.pow(1024,3))),"[GB to Bytes]")
if options.tb:
    print(int(int(options.tb)*(math.pow(1024,4))),"[TB to Bytes]")

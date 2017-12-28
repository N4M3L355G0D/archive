#! /usr/bin/python3

import os,sys,argparse

parser=argparse.ArgumentParser()
parser.add_argument("-s","--string-in",help="verify pattern string",required="yes")
parser.add_argument("-c","--check-string",help="string for check",required="yes")
options=parser.parse_args()

if options.check_string in options.string_in:
 print(True)
elif options.check_string not in options.string_in:
 print(False)

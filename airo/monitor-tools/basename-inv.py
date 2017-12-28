#! /usr/bin/python3

import os, argparse


parser=argparse.ArgumentParser()
parser.add_argument("-b","--basename",help="path basename")
parser.add_argument("-i","--inverse-basename",help="inverse of basename")
options=parser.parse_args()

if options.basename:
    path=os.path.split(options.basename)[1]
elif options.inverse_basename:
    path=os.path.split(options.inverse_basename)[0]
else:
    path="please use -h or --help for help"


print(path)

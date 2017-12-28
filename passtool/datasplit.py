#! /usr/bin/python3

import argparse

def cmd_line():
 parser=argparse.ArgumentParser()
 parser.add_argument("-s","--in-string",help="test if input number is a multiple of 5",required="yes")
 options=parser.parse_args()
 return options.in_string

def data_break(string=str(cmd_line())):
 data=string.split(" ")
 for i,j in enumerate(data):
  result=str(i)+" "+str(j)
  print(result)

data_break() 

#! /usr/bin/python3

import argparse

def cmd_line():
 parser=argparse.ArgumentParser()
 parser.add_argument("-5","--time5",help="test if input number is a multiple of 5",required="yes")
 options=parser.parse_args()
 return options.time5

def test5(num=int(cmd_line())):
 test_val=[0,5,10,15,20,25,30,35,40,45,50,55,60]

 if num in test_val:
  print("True")
  return True
 else:
  print("False")
  return False

test5()

#! /usr/bin/python3

import time, argparse

def pinbreak(data="",user=""):
 if len(data) < 14:
  return "too short pin"
 if len(data) > 14:
  return "too long"
 if len(data) == 14:
  number=str(data)
  breaker=3
  pin=[number[i:i+breaker] for i in range(0,len(number),breaker)]
  pinStr=""
  delimiter=" "
  for chunk in pin:
   pinStr=pinStr+chunk+delimiter
  dt="PIN: "+str(pinStr)+"\nDATE: "+str(time.ctime())+"\nUSER: "+str(user)
  return dt

def cmdline():
 parser=argparse.ArgumentParser()
 parser.add_argument("-p","--pin",help="pin to be split")
 parser.add_argument("-u","--user",help="who is splitting the pin")
 options=parser.parse_args()
 return options

def main():
 args_cmd=cmdline()
 outResult=pinbreak(args_cmd.pin,args_cmd.user)
 print(outResult)


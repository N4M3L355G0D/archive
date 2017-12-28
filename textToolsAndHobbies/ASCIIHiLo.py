#! /usr/bin/python3
import os

if os.path.exists("./num2Ascii.py"):
 import num2Ascii
 noCheck=False
else:
 noCheck=True

charLower="abcdefghijklmnopqrstuvwxyz"
charUpper=charLower.upper()
number="1234567890"
special="~`!@#$%^&*()_+-={}[]|\:\";'<>,.?/ "

ascII=charLower+charUpper+number+special
high=0
low=126
print("this prints the highest and lowest ascii numbers from the string below:\n\n\n",ascII,"\n\n")
print("High Low")
for i in ascII:
 if high < ord(i):
  high=ord(i)
 if low > ord(i):
  low=ord(i)
print(" "+str(high)," "+str(low))
print("\nBelow is the HILO Number's check verification Reciept.\nThe string is everything between '#ENDCAP#', including the space.")
if noCheck == False:
 num2Ascii.test(low,high)

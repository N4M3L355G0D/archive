#! /usr/bin/python3
# check field components of pinbreak
def phoneNumber(number):
 #8045921431
 #804-592-1431
 #(804)-592-1431
 #(804)592-1431
 #(804) 592-1431
 #804.592.1431
 acc=""
 localPrefix="804"
 for i in str(number):
  if i.isdigit():
   acc=acc+i
 if len(acc) == 10:
  print(acc)
  return acc
 elif len(acc) == 7:
  localNum=localPrefix+acc
  print(localNum)
  return localNum
 elif len(acc) > 10:
  print("PN too long")
  return "PN_long"
 elif len(acc) < 10:
  print("PN too short")
  return "PN_short"

"""phoneNumber("804.592.1431")
phoneNumber("804-592-1431")
phoneNumber("(804)5921431")
phoneNumber("(804) 592-1431")
phoneNumber("381-4569")
phoneNumber("804-592-14311")
"""
def pincheck(pin):
 acc=""
 for i in str(pin):
  if i.isdigit():
   acc=acc+i
  elif not i.isdigit():
   print("this is an incorrect pin: only numbers allowed")
   return "pin_!numbers_only"
 if len(acc) == 14:
  print(acc)
  return acc
 elif len(acc) > 14:
  print("pin_long")
  return "pin_long"
 elif len(acc) < 14:
  print("pin_short")
  return "pin_short"

"""
pincheck("i12345678912345")
pincheck(1234567891234)
pincheck(123456789123456)
pincheck(12345678912345)
"""

def orderNumber(on):
 acc=""
 for i in str(on):
  if i.isdigit():
   acc=acc+i
  elif not i.isdigit():
   print("bad order number: not numbers only")
   return "on_!numbers_only"
 if len(acc) == 8:
  print(acc)
  return acc
 elif len(acc) < 8:
  print("bad order number: too short")
  return "ON_short"
 elif len(acc) > 8:
  print("bad order number: too long")
  return "ON_long"
"""
orderNumber("a1234567")
orderNumber("123456789")
orderNumber("123456")
orderNumber("12345678")
"""

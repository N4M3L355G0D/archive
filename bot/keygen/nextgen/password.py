#! /usr/bin/python3
import random, argparse, os

class password():

 def __init__(self):
  pass
 plen=8
 upper=127
 lower=32
 skipmessage=False
 def randomChar(self):
  password_str=str()
  for i in range(0,self.plen):
   password_str+=str(chr(random.randint(self.lower,self.upper)))
  return password_str
 def asciiGen(self):
  for i in range(self.lower,self.upper):
   yield(i)
 def message(self,state):
  if state == 0:
   sep="\n#START#\n"
  elif state == 1:
   sep="\n#END#\n"
  return sep
 def init(self):
  if self.skipmessage == False:
      return self.message(0)+self.randomChar()+self.message(1)
  else:
      return self.randomChar()

def cli():
    parser=argparse.ArgumentParser()
    parser.add_argument("-l","--length",help="length of password in characters",required="yes")
    parser.add_argument("-o","--write",help="write to file")
    parser.add_argument("-s","--skip-msg",help="do not write #start# #end#",action="store_true")
    options=parser.parse_args()
    
    Pass=password()
    Pass.plen=int(options.length)
    if options.skip_msg == True:
        Pass.skipmessage=True
    axis=Pass.init()
    
    if options.write:
        if os.path.exists(options.write):
            if os.path.isfile(options.write):
                file=open(options.write,"a")
            else:
                print(options.write,"exists, but is not a file; nothing to do!")
        elif not os.path.exists(options.write):
            file=open(options.write,"w")
        file.write(axis)
        file.close()
    print(axis)

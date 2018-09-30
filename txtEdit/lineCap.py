#! /usr/bin/python3

import sys,os

class textmod:
 def wordCorrection(self,line):
  for num,word in enumerate(line):
   if word == "i":
    line[num]="I"
  return line
 
 def linecap(self,line):
  line=line.decode()
  line=line[0].upper()+line[1:len(line)]
  return line

 def main(self):
  if len(sys.argv) >= 2:
   with open(sys.argv[1],"rb") as data, open(sys.argv[1]+".tmp","wb") as odata:
    for line in data:
     line=self.linecap(line)
     line=line.split(" ")
     line=self.wordCorrection(line)
     line=' '.join(line)
     print(line.rstrip("\n"))
     odata.write(line.encode())

a=textmod()
a.main()

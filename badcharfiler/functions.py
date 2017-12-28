import os, sys, codecs, random, string, re, argparse

## return true or false for printable characters

def swap2(a):
  try:
   a.encode('ascii')
  except UnicodeEncodeError:
   return False
  else:
   return True

## takes a list
def stripchar(doc=[]):
 for x in doc:
  dat=swap2(x)
  outstring=''
  ##parse through d if dat has non-ascii chars
  if dat == False:
   for d in x:
    ##strip the non-ascii chars from the filename as a list
    outstring2=("\""+''.join([d if ord(d) < 128 else str(random.randint(0,1000000)) for d in x])+"\"")
    ## join the list into a string
    outstring2_dat=''.join(re.split(u'\s*’\s*',u''.join(re.split(u'\s*•\s*',u''.join(''.join(outstring2))))))
   ##print the string data
   print(outstring2)
   return outstring2

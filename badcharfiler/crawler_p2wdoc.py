import os, sys, codecs, random, string, re, argparse


## return true or false for printable characters

def swap2(a):
  try:
   a.encode('ascii')
  except UnicodeEncodeError:
   return False
  else:
   return True

## chars on the keyboard

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQXYZ1234567890_-.&+@() []'!,~$=%"
x=''
## this is supposed to be a bullet, does not work, but might remove unnecessary chars
regex='\xc2\xb7' 

parser=argparse.ArgumentParser()
parser.add_argument("-d","--directory",help="directory to be scanned")
options=parser.parse_args()

## prevent the program from running if -d option is empty, 
if options.directory == None:
 print("-d directory\n")
 exit()

## create the os.walk object
files=os.walk(options.directory)
#parse throught the object
for i,j,doc in files:
## parse through doc as x 
 for x in doc:
   dat=swap2(x)
   outstring=''
   ##parse through d if dat has non-ascii chars
   if dat == False:
    for d in x:
     ## create the orginal path
     pathOrig=[i,"/",x]
     ## create the path for the new files as a tuple
     outstring1=("\""+''.join(pathOrig)+"\""," ")
     ## join the tuple into a string
     outstring1_dat=''.join(outstring1)
     ##strip the non-ascii chars from the filename as a list
     outstring2=('/'+''.join([d if ord(d) < 128 else str(random.randint(0,1000000)) for d in x])+"\"")
     ## join the list into a string
     outstring2_dat="\""+i+''.join(re.split(u'\s*’\s*',u''.join(re.split(u'\s*•\s*',u''.join(''.join(outstring2).rsplit(regex))))))
     ## concatenate the strings
     outstring=outstring1_dat+outstring2_dat
    ##print the string data
    print("mv ",outstring)

### stage one , files [ DONE ]


##import os, random

dirs=os.walk(options.directory)
outstring2_dat=''
for folders,i,j in dirs:
 dat=swap2(folders)
 if dat == False:
  dirs_list=[]
  # create list
  stage1=folders.split("/")
  #iterate through elements
  for element in stage1:
   element_list=[]
   for char in element:
    if ord(char) < 128:
     element_list.append(char)
    else:
     ## use a random number in place of the invalid char so no files are accidentally overwritten
     element_list.append(str(random.randint(0,100000)))
 
 
   element_string=''.join(element_list)
  # dirs_list.append("/")
   dirs_list.append(element_string)
   dirs_list.append("/")
  print("mv ","\""+folders+"\"","\""+''.join(dirs_list)+"\"")
 

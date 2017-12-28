import os, random

dirs=os.walk("../samba/mom/Pictures")
outstring2_dat=''
for folders,i,j in dirs:
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


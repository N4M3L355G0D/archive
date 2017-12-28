#! /usr/bin/python3

import sys

import keygen_nextgen
from crypt import eCrypt

import tar
import os,subprocess as sp, shutil, platform, time
#will turn into class on another day
top="/srv/samba/bash/"
bBackup=top+"backup/"
tmp=top+"tmp/"
keys=top+"keys/"
def hostname():
 name=platform.uname().node
 return name

def enumuser():
 location="/home/"
 accL=list()

 for i in os.listdir(location):
  path=location+i+"/.bash_history"
  if os.path.exists(path):
    accL.append(path)
 return accL

def totalSize():
 returnCont=dict()
 files=dict()
 acc=int()
 d=enumuser()
 for num,i in enumerate(d):
  da=sp.Popen("ls -l "+i+" | awk '{print $5}'",shell=True,stdout=sp.PIPE)
  dat,err=da.communicate()
  acc=acc+int(dat.decode())
  files[str(num)]={'file':i,"size":int(dat.decode())}
 returnCont={'files':files,'t_size':acc}
 return returnCont

def date():
 current_date=str()
 for i in time.localtime():
  current_date=current_date+str(i)
 return current_date

def location(path):
 #add non-dir exceptions
 if not os.path.exists(path):
  os.makedirs(path)

def cpfile(file=""):
 cdate=date()

 location(tmp)
 location(bBackup)
 source=file
 dest=source.replace("/",".")
 dest=dest.replace("..",".")
 dest=tmp+hostname()+cdate+dest
 
 shutil.copy(source,dest)
 return dest

a=totalSize()

print(a)
for i in range(0,len(a['files'])):
 b=cpfile(a['files'][str(i)]['file'])
 key=keygen_nextgen.keygen()
 key.noDelim=True
 d=eCrypt()
 d.demo=False
 d.printVal['encrypt']=False
 d.printVal['decrypt']=False
 d.keyfile=keys+os.path.basename(b)+".bin"
 d.key=key.nonceTotal()
 d.message=tmp+os.path.basename(b)+".aes"
 file=open(d.keyfile,"wb")
 file.write(d.key)
 file.close()
 hfile=tmp+os.path.basename(b)
 bash_history=open(hfile,"r")
 for i in bash_history.read():
     d.text+=str(i)
 d.encrypt()
 os.remove(tmp+os.path.basename(b))


compress=tar.tar()
compress.make_tarfile(bBackup+compress.output,tmp)
for i,j,k in os.walk(tmp):
    for x in k:
        os.remove(i+x)

kompress=tar.tar()
kompress.make_tarfile(bBackup+"keys."+compress.output,keys)
for i,j,k in os.walk(keys):
    for x in k:
        os.remove(i+x)

for i in range(0,len(a['files'])):
 hist=a['files'][str(i)]['file']
 file=open(hist,"w+")
 file.write('')
 file.close()
 print(hist+" [overwritten]")

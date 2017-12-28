#! /usr/bin/python3

## find pdf's on system
## copy pdf's to defined location on system
## be verbose
## use cmdline args
import os,shutil,sys, argparse,time,hashlib

def timeit():
    date=""
    for i in time.localtime():
        date=date+str(i)
    return date
def mkdest(dest,ext):
    destpath=os.path.join(dest,ext)
    if not os.path.exists(destpath):
        os.mkdir(destpath)
        return [True,"Dest. Path create","Destpath did not exist"]
    else:
        return [False,"Dest. Path !created","Destpath exists"]

def main(path,dest,ext):
 mkdest_result=mkdest(dest,ext)
 print(mkdest_result)
 date=str(timeit())
 counter=0
 checked=0
 for i,j,k in os.walk(path):
  for h in k:
   item=i+"/"+h
   if os.path.splitext(h)[1] == "."+ext:
    if not os.path.exists(dest):
        os.mkdir(dest)
        if not os.path.exists(dest+"/"+ext):
         os.mkdir(dest+"/"+ext)
    if os.path.exists(item) and os.path.exists(dest+"/"+ext):
        if not os.path.isdir(dest+"/"+ext):
            
            shutil.move(dest+"/"+ext,dest+"/"+ext+".file."+date)
            print("moved "+dest+"/"+ext+"-> "+dest+"/"+ext+".file"+date)
            os.mkdir(dest+"/"+ext)
    if os.path.exists(dest+"/"+ext+"/"+h):
        src=open(item,"rb")
        src_h=hashlib.sha512()
        Dest=open(dest+"/"+ext+"/"+h,"rb")
        dest_h=hashlib.sha512()
        while True:
            data_d=Dest.read(512)
            if not data_d:
                break
            else:
                dest_h.update(data_d)

        while True:
            data_s=src.read(512)
            if not data_s:
                break
            else:
                src_h.update(data_s)
        print(item,"compared to",str(dest+"/"+ext+"/"+h))
        checked=checked+1
        if src_h.hexdigest() != dest_h.hexdigest():
            try:
                shutil.copy(item,str(dest+"/"+ext+"/"+date+"."+h))
                print("they are not the same!")
            except:
                print("copy could not be done")
    else:
        print(item, "copied to",str(dest+"/"+ext+"/"))
        try:
            shutil.copy(item,str(dest+"/"+ext+"/"))
        except:
            print("copy could not be done")
        counter=counter+1
 print("destination: ",dest+"/"+ext)
 print("Files copied: ",counter)
 print("Files Checked: ",checked)

parser=argparse.ArgumentParser()
parser.add_argument("-d","--destination",required="yes")
parser.add_argument("-s","--source",required="yes")
parser.add_argument("-e","--extension",required="yes")
options=parser.parse_args()

main(options.source,options.destination,options.extension)

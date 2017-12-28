#! /usr/bin/env python3
import tarfile, argparse, os, platform, sys



class win10tar():
 def error(self):
  print("please see -h/--help")
  sys.exit()
 
 
 supportedFormats_str="xz,gz,bz2"
 
 if platform.uname().system == 'Windows':
     osslash="\\"
 else:
     osslash="/"
 print(sys.argv[0]+" running on system: "+platform.uname().system+", release: "+platform.uname().release+", version: "+platform.uname().version)
 defaultExtract="."
 command=""
 path="."
 infile=""
 supportedFormats=supportedFormats_str.split(",")
 defaultFormat=os.path.splitext(infile)[1].strip(".")
 compression="xz"
 def main(self):
  if self.defaultFormat == '':
   self.defaultFormat='xz'
  if self.compression:
   if self.compression in self.supportedFormats:
    self.defaultFormat=self.compression
   else:
    print("[WARN] [ "+self.compression+" ] not supported. Please review -h/--help. Will use default format [ "+self.defaultFormat+" ]")
  print("[WARN] using "+self.defaultFormat+" for compression.")
  
  if self.path:
   if os.path.exists(self.path):
    self.defaultExtract=self.path
   else:
    print("[WARN] [ "+self.path+" ] does not exist. using default extraction path [ "+self.defaultExtract+" ]")
  print("[WARN] using "+self.defaultExtract+" for extraction path.")
  
  if self.command:
   if self.command == "z":
    self.opath=self.defaultExtract+self.osslash+os.path.basename(self.infile+".tar."+self.defaultFormat)
    if not os.path.exists(self.opath):
     print(self.opath)
     file=tarfile.open(self.opath,"w:"+self.defaultFormat)
     file.add(self.infile,os.path.join(os.path.basename(os.path.dirname(self.infile)),os.path.basename(self.infile)))
     file.close()
    else:
     print(self.opath+" -> Exists!")
   elif self.command == "xa":
    print("extracting:",self.infile)
    file=tarfile.open(self.infile,"r:"+self.defaultFormat)
    #print(self.infile)
    ext2=os.path.splitext(self.infile)[0]
    ext1=os.path.splitext(ext2)
    fname=ext1[0]
    print(fname)
    file.extractall(self.defaultExtract+self.osslash+os.path.basename(fname))
    file.close()

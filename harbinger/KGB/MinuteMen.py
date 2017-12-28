import itertools, multiprocessing, threading, hashlib, time, sys, platform


threadC=list()
text=list()
for i in range(32,127):
 text.append(chr(i))

cpuN=multiprocessing.cpu_count()*int(platform.architecture()[0].strip("bit"))
#multiprocessing.set_start_method('spawn')


def main1(q="",prog=""):
 file=open(prog+"_"+q+"cpu"+time.ctime()+".virii","a")
 seg=hashlib.sha512()
 a=''.join(text)
 for mx in range(0,512):
  for i in itertools.combinations_with_replacement(a,mx):
   seg.update(''.join(i).encode())
   result=[''.join(i),str(seg.hexdigest())]
   print(result)
   file.write(''.join(result))
 file.close()

for i in range(0,cpuN-1):
 q=str(i)
 prog=sys.argv[0]
 Q=multiprocessing.Queue()
 threadC.append(multiprocessing.Process(target=main1,args=(q,str(prog),)))
 threadC[i].start()
 threadC[i].join(0.5)

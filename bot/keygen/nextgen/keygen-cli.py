#! /usr/bin/python3
#local
import keygen_nextgen
import password
#global
import binascii,base64, time, argparse,os

def current_date():
    acc=str()
    for i in time.localtime():
        acc=acc+str(i)
    return acc

date=current_date()
K=keygen_nextgen.keygen()
P=password.password()
P.skip_message=True
P.plen=128
K.passString=P.init()
Key=K.nonceTotal()
default="./"
ascii=str(Key).replace('-','')

parser=argparse.ArgumentParser()
parser.add_argument("-p","--path-to-store",help="path to store")
options=parser.parse_args()

if options.path_to_store:
    path=options.path_to_store
    if not os.path.exists(path):
        print("store path does not exist")
        path=default
else:
    path=default

cfg=path+"/current-key."+date+".binary"
hexed=path+"/current-key."+date+".hdd"
bdata=binascii.unhexlify(ascii)
file=open(cfg,"wb")
file.write(bdata)
file.close()

file=open(hexed,"w")
file.write(Key)
file.close()

print("Hex Key: ",Key,"\nWritten to: ",hexed)
print("\nBinary Key: ",bdata,"\nWritten to: ",cfg)

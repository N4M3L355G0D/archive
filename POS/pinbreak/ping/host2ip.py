#! /usr/bin/python3
import socket, subprocess, os


nl="\n"
hostname=""
port=0

CFG="./pinbreak.cfg"
if os.path.exists(CFG) and os.path.isfile(CFG):
 with open(CFG,"r") as cfg:
  for i in cfg:
   if len(i.split("=")) > 1:
    varName=i.split("=")[0]
    varVal=i.split("=")[1]
    if varName == "hostname":
     hostname=varVal.rstrip(nl)
    if varName == "port":
     port=int(varVal.rstrip(nl))
    if varName == "icon":
     icon=varVal.rstrip("\n")
else:
    print("configuration file does not exist! quitting!")
    exit()

def getIp(hostname):
 ipaddr=socket.gethostbyname(hostname)
 return ipaddr

def checkaddr(address):
 accAddr=""
 for i in address:
  if i.isalpha():
   print("mightBeHostname")
   accAddr=getIp(address)
   print(accAddr)
   return accAddr
  elif i.isdigit():
   accAddr=accAddr+i
  elif i == ".":
   accAddr=accAddr+i
 print(accAddr)
 return accAddr


def linuxPing(address):
 cmd="ping -c 3 "+checkaddr(str(address))
 a=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
 b, err=a.communicate()
 for i in b.decode().split(" "):
  if "=" in i: 
   if len(i.split("=")) == 2:
    if i.split("=")[0] == "time":
     echoTime="time to server "+str(i.split("=")[1])+" ms"
 print(echoTime)
 return echoTime+"\nServer Address: "+str(address)

#linuxPing(hostname)

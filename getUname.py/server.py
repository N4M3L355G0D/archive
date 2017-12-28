#! /usr/bin/python3

import socket,platform,time,os,sys,argparse
from multiprocessing import Process as process

def rotate(host,cmdport,ofile):
    ofileBreak=os.path.splitext(os.path.split(ofile)[1])
    cmdSocket=socket.socket()
    try:
        cmdSocket.bind((host,cmdport))
    except:
        print("cmdSocket already bound")
    cmdSocket.listen(20)
    conn,addr=cmdSocket.accept()
    print("cmd connection from ",(addr,":",cmdport))
    data=conn.recv(1024)
    cmdSocket.close()
    if data.decode() == "rotate":
        conn.send("rotate cmd recieved".encode())
        os.rename(ofile,ofileBreak[0]+"."+time.ctime()+ofileBreak[1])
    #cmdSocket.close()



file="./defaults.cfg"
def config():
    defaults=dict()
    if os.path.exists(file) and os.path.isfile(file):
        conf=open(file,"r")
        for i in conf:
            if not i[0] == '#':
                option,arg=i.split("=")
                defaults[option]=arg.rstrip("\n")
        return defaults
    else:
        return False

def cmdline():
    parser=argparse.ArgumentParser()
    parser.add_argument("-H","--host",help="server address")
    parser.add_argument("-p","--port",help="server port to use")
    parser.add_argument("-k","--control",help="override control file")
    parser.add_argument("-l","--log",help="log file for client data storage")
    options=parser.parse_args()
    return options

def killcheck(killfile,mode):
 kill=open(killfile,mode)
 for i in kill:
  option,arg=i.split("->")
  if option == "stop" and arg.rstrip("\n") == "kill":
   print("kill file says stop")
   sys.exit()


def server(killfile,mode):
 killcheck(killfile,mode)
 defaults=config()
 defaults_dict={'log':False,'host':False,'port':False}
 if defaults != False:
     for i in defaults.keys():
         defaults_dict[i]=True
 #for testing purposes only 

 cmdArg=cmdline()
 if cmdArg.log:
     print("alternate log file: ",cmdArg.log)
     ofile=cmdArg.log
 elif defaults_dict['log'] == True:
     try:
         ofile=defaults['log']
     except:
         print("something went wrong and the "+file+"specified log file could not be used! Prompting user for log file!")
         try:
             ofile=input("log file: ")
         except:
             print("Quick! where is the nearest desk to head bang?! the user prompted file failed for some reason! Attempting to use internal Hard Coded log file name!")
             try:
                 ofile="./uname.dat"
             except:
                 print("[Rips eyeballs out of sockets] The internal Hard Coded log file failed to set as well. Fuck your GD environment! If it failed at this stage, something is really wrong")
                 sys.exit()

 else:
     ofile="./uname.dat"
 if not os.path.exists(ofile):
     storage=open(ofile,"wb")
     storage.write("".encode())
     storage.close()
  
 if cmdArg.host:
     print("alternate Host Address: ",cmdArg.host)
     host=cmdArg.host
 elif defaults_dict['host'] == True:
     try:
         host=defaults['host']
     except:
         print("something went wrong and the "+file+"specified host address could not be used! Prompting user for address!")
         try:
             host=input("host address: ")
         except:
                print("Well fuck, something else is wrong! Using internal Hard Coded default (127.0.0.1)")
                try:
                    host='127.0.0.1'
                except:
                    print("hhmmmmm... what the ????ing h???... okay it seems that the internal Hard Coded address will not work either. Exiting with a Gun to the head [ once out of sight, shoots self in the head ]")
                    sys.exit()
 else:
    host='127.0.0.1'

 if cmdArg.port:
     try:
         print("alternate server port: ",cmdArg.port)
         port=int(cmdArg.port)
     except:
         port=9998
 elif defaults_dict['port']:
     try:
         port=int(defaults['port'])
         print("alternate server port: ",defaults['port'],"["+file+"]")
     except:
         print("something went wrong and the defaults.cfg specified port could not be used! Using internal Hard-Coded default (9998)")
         try:
             port=9998
         except:
             print("something else is wrong, now prompting user for port!")
             try:
                 port=int(input("port: "))
             except:
                 print("oh boy!!! something is really wrong... port value prompt has failed too! Exitting like a little bitch!")
                 sys.exit()
 else:
     port=9998
 
 hostPort=(host,port)
 cmdport=port+1
 

 try:
     server=socket.socket()
 except:
     print("failed to create a socket")
     sys.exit()
 try:
     server.bind(hostPort)
 except:
     print("failed to bind ",hostPort,"to socket!")
     sys.exit()

 print("server started on ",hostPort[0],":",hostPort[1])
 try:
     server.listen(20)
 except:
     print("failed at the server.listen() stage")
     sys.exit()
 #conn,addr = server.accept()
 #print("connection from :",str(addr))
 while True:
  killcheck(killfile,mode)
  try:
      conn,addr = server.accept()
      print("connection from :",str(addr))
  except:
      print("failed at the server.accept() stage")
      sys.exit()
  try:
      data=conn.recv(1024)
  except:
      print("failed at the conn.recv() stage")
      sys.exit()
  
  #if not data:
  # break
  try:
      try:
         storage=open(ofile,"ab")
      except:
         print("well this is embarrassing, I cannot open a file to write to!")
         sys.exit()
      print("data from connect client: ",data)
      storage.write(data)
      storage.close()
  except:
      print("failed at the storage.write() stage")
      sys.exit()

  try:
      conn.send(b"data recorded [ probably, needs a checking function ]")
  except:
      print("failed at the conn.send() stage")
      sys.exit()
 # multiprocess here
  cmd=process(target=rotate,args=(host,cmdport,ofile))
  cmd.start()
  conn.close()

def master():
    cmd=cmdline()
    if cmd.control:
        print("alternate control file: ",cmd.control)
        conf=(cmd.control,"r")
    else:
        conf=("./killfile.cfg","r")
    
    #restart server unless killfile says stop
    stop=False
    while True:
        killfile=open(conf[0],conf[1])
        killcheck(conf[0],conf[1])
        killfile.close()
        server(conf[0],conf[1])

master()

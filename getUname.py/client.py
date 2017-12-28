#! /usr/bin/python3

import socket, platform,netifaces, time, argparse, cpuinfo

def getProcessor():
    ostring='[CPU Info.]\n'
    processor=cpuinfo.get_cpu_info()
    for i in processor.keys():
        if i == "hardware":
            if processor[i] == "":
                ostring+=i+" Null\n"
        elif i != "flags":
            if type(processor[i]) == type(tuple()):
                tmp=str()
                processor_len=len(processor[i])-1
                for num,sub_i in enumerate(processor[i]):
                    if num < processor_len:
                        tmp+=i+"->"+str(sub_i)+"\n"
                    else:
                        tmp+=i+"->"+str(sub_i)
                ostring+=tmp+"\n"
            elif type(processor[i]) == type(str()):
                    ostring+=''.join((i+"->",processor[i]))+"\n"
        elif i == "flags":
            tmp=str()
            processor_len=len(processor[i])-1
            for num,sub_i in enumerate(processor[i]):
                if num < processor_len:
                    tmp+=i+"->"+sub_i+"\n"
                else:
                    tmp+=i+"->"+sub_i
            ostring+=tmp
    return ostring

def cmdline():
    parser=argparse.ArgumentParser()
    parser.add_argument("-H","--host",help="server address")
    parser.add_argument("-p","--port",help="server address port")

    option=parser.parse_args()
    return option

def client():
    cmd_args=cmdline()
    cpu=getProcessor()
    quitCodes=["quit","Q","q","exit","E","X","x","e"]

    if cmd_args.host:
        print("alternate server address: ",cmd_args.host)
        host=cmd_args.host
    else:
        host='127.0.0.1'

    if cmd_args.port:
        print("alternate server port: ",cmd_args.port)
        try:
            port=int(cmd_args.port)
        except:
            print("alternate server port connection failed,\n using default port: 9998")
            port=9998
    else:
        port=9998

    hostPort=(host,port)
    cmdport=port+1

    interfaces=netifaces.interfaces()
    addresses=dict()
    addrStr=str()
    
    # prep data for transmission
    ## get mac addresses and if available, get ip addresses attached
    for i in interfaces:
        if i != 'lo':
            #when interface is not assigned an address, list values necessary change, so use try statement to fix
            try:
                addresses[i]=netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']+"@"+netifaces.ifaddresses(i)[2][0]['addr']
            except:
                #no address applied
                addresses[i]=netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']
    for i in addresses.keys():
        addrStr+=i+"->"+addresses[i]+"\n"
    ## get uname data 
    count=0
    indices=["system","node","release","version","machine","processor"]
    data_send="[Host.uname(start)]\n"
    data_list=list()
    
    for i in platform.uname():
        if i == '':
            i="Unknown"
        data_list.append(indices[count]+"->"+i)
        count+=1
    
    for i in data_list:
        data_send+=i+"\n"

    data_send+="\n[NIC]\n"+addrStr+"\n"+cpu
    #initialize promt early
    data_send+="\nEntry Time->"+time.ctime()+"\n[Host.uname(END)]\n"
    chunk=1024
    
    data_broken=[data_send[i:i+chunk] for i in range(0,len(data_send),chunk)]
    for i in data_broken:
        clientSocket=socket.socket()
        clientSocket.connect(hostPort)
        clientSocket.send(i.encode())
        try:
            fromServer=clientSocket.recv(1024)
            print("Server Says: ",fromServer.decode())
        except:
            print("nothing from server")
        clientSocket.close()

    cmdSocket=socket.socket()
    cmdSocket.connect((host,cmdport))
    cmdSocket.send("rotate".encode())
    cmdSocket.close()

client()

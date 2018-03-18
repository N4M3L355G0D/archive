#! /usr/bin/env python3
#NoGuiLinux
import base64, paramiko
import subprocess as sp
import time, signal
import netifaces as ni
import sys, argparse, os

#set localdir lib
libdir='lib'
if os.path.exists(libdir) and os.path.isdir(libdir):
    sys.path.insert(0,libdir)
#get configuration from xmlfile, sqlite3 db,or prompt

class netspeaker:
    clientlist=[]
    clientdict={}
    openClients=[]
    keyfname='/home/carl/.ssh/id_rsa'
    rate=256
    forbiddenkeys=['password','sshport']
    def cmdline(self):
        ALLOPT='all options must be specified'
        MUSTEQ='all options must have the same number of commas'
        client={}
        parser=argparse.ArgumentParser()
        parser.add_argument('--use-cmdline',action='store_true')
        parser.add_argument('-u','--user',help='multiple users separated by commas')
        parser.add_argument('-p','--password',help='multiple passwords separated by commas')
        parser.add_argument('-a','--address',help='multiple addresses separated by commas')
        parser.add_argument('-P','--port',help='multiple ports separated by commas')
        parser.add_argument('-r','--rate',help='multiple rates separated by commas')
        parser.add_argument('-s','--sshport',help='multiple ports separated by commas')

        options=parser.parse_args()
        if options.use_cmdline:
            #cmdline args for config
            userLen=len(options.user.split(','))
            for i in range(userLen):
                client['user']=options.user
                if client['user']:
                    client['user']=client['user'].split(',')[i]
                else:
                    exit(ALLOPT+": user")

                client['password']=options.password
                if client['password']:
                    if len(client['password'].split(',')) != userLen:
                        exit(MUSTEQ+': password')
                    client['password']=client['password'].split(',')[i]
                else:
                    exit(ALLOPT+": password")

                client['address']=options.address
                if client['address']:
                    if len(client['address'].split(',')) != userLen:
                        exit(MUSTEQ+': address')
                    client['address']=client['address'].split(',')[i]
                else:
                    exit(ALLOPT+": address")

                client['port']=options.port
                if client['port']:
                    if len(client['port'].split(',')) != userLen:
                        exit(MUSTEQ+': port')
                    client['port']=client['port'].split(',')[i]
                else:
                    exit(ALLOPT+": port")

                client['sshport']=options.sshport
                if client['sshport']:
                    if len(client['sshport'].split(',')) != userLen:
                        exit(MUSTEQ+': sshport')
                    client['sshport']=client['sshport'].split(',')[i]
                else:
                    exit(ALLOPT+": sshport")
                #need to keep in mind that classified dicts need to be re-initialized after each use
                self.addNewClients(client)
                client={}

    def addNewClients(self,clientDict):
        self.clientlist.append(clientDict)

    def display(self,client,altword=None):
        for key in client.keys():
            if key not in self.forbiddenkeys:
                if altword == None:
                    print('{0}: {1}'.format(key,client[key]))
                else:
                    print('{0}: {1} {2}'.format(key,client[key],altword))

    def main(self):
        #handle ctrl-c
        signal.signal(signal.SIGINT,self.cleanup)
        #handle kill <pid>
        signal.signal(signal.SIGTERM,self.cleanup)
        for client in self.clientlist:
            Client=paramiko.SSHClient()
            Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            Client.connect(client['address'],client['sshport'],username=client['user'],key_filename=self.keyfname,password=client['password'])
            #server process
            self.display(client)
            
            process=sp.Popen('ffmpeg -f alsa -i pulse -ac 2 -acodec libmp3lame -ar 48000 -ab {0} -f flv -f rtp rtp://{1}:{2} &> /dev/null &'.format
            (self.rate,client['address'],client['port']),shell=True,stdout=sp.PIPE)
            
            stdout,stderr=process.communicate()
            #client process
            stdin,stdout,stderr=Client.exec_command('export display=:0 ; nohup ffplay rtp://{0}:{1} -nodisp &> /dev/null &'.format
            (client['address'],client['port']))
            
            self.openClients.append(Client)
        #need to hold connection open until user quits, with either userin or ctl-c/ctrl-d
        quit=' '
        while quit != 'y\n':
            #the new line '\n' is necessary so that a enter key press does not exit early
            #an explicit 'y' must be given
            #ctrl-d is a eof, this deals with a user pressing ctrl-d
            if quit:
                sys.stdout.write('quit: ')
                sys.stdout.flush()
                quit=sys.stdin.readline()
            else:
                self.cleanup()
        self.cleanup()

    def cleanup(self,signum=None,frame=None):
        print('beginning cleanup!')
        for num,client in enumerate(self.openClients):
            self.display(self.clientlist[num],altword='[done]')
            process=sp.Popen('killall -15 ffmpeg',shell=True,stdout=sp.PIPE)
            stdout,stderr=process.communicate()
            stdin,stdout,stderr=client.exec_command('killall -9 ffplay')
            for line in stdout:
                print(line.rstrip('\n'))
            client.close()
        exit()

net=netspeaker()
net.cmdline()
#print(net.clientlist)
net.main()

#! /usr/bin/env python3
#NoGuiLinux

import xml.etree.ElementTree as ET
import os

class xmlcnf:
    clients=[]
    file='netspeaker_cfg.xml'
    def getcfg(self):
        comp=0
        if os.path.exists(self.file) and os.path.isfile(self.file):
            tree=ET.parse(self.file)
            root=tree.getroot()
            for client in root:
                Client={}
                if client.tag == 'client':
                    for component in client:
                        if component.tag == 'user':
                            Client['user']=component.text
                            comp+=1
                        if component.tag == 'port':
                            Client['port']=component.text
                            comp+=1
                        if component.tag == 'address':
                            Client['address']=component.text
                            comp+=1
                        if component.tag == 'sshport':
                            Client['sshport']=component.text
                            comp+=1
                        if component.tag == 'password':
                            Client['password']=component.text
                            comp+=1
                    if not (comp < 5):
                        self.clients.append(Client)
                    else:
                        exit("xml '{}': invalid".format(self.file))
        return self.clients
#need to add checking to ensure that the proper comp
                

#! /usr/bin/env python3
#NoGuiLinux

import xml.etree.ElementTree as ET
import os

class xmlcnf:
    clients=[]
    file='netspeaker_cfg.xml'
    def getcfg(self):
        if os.path.exists(self.file) and os.path.isfile(self.file):
            tree=ET.parse(self.file)
            root=tree.getroot()
            for client in root:
                Client={}
                if client.tag == 'client':
                    for component in client:
                        if component.tag == 'user':
                            Client['user']=component.text
                        if component.tag == 'port':
                            Client['port']=component.text
                        if component.tag == 'address':
                            Client['address']=component.text
                        if component.tag == 'sshport':
                            Client['sshport']=component.text
                        if component.tag == 'password':
                            Client['password']=component.text
                    self.clients.append(Client)
        return self.clients

                

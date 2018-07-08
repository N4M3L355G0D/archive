#! /usr/bin/env python3
#NoGuiLinux

import urllib.request,urllib.error
from bs4 import BeautifulSoup as bs
import json

class container:
    master=None
    class web:
        types=['search','info']
        rpcUrl='https://aur.archlinux.org/rpc/?v=5&type={}&arg={}'
        master=None
        def connect(self,t='info',pkg=''):
            try:
                conn=urllib.request.urlopen(self.rpcUrl.format(t,pkg))
                return conn
            except urllib.error.HTTPError as err:
                exit(str(err))
            except urllib.error.URLError as err:
                exit(str(err))

        
        def jsonParseNames(self,J=b''):
            load=json.load(J)
            return [i['Name'] for i in load['results']]

        def jsonParsePkgs(self,J=b''):
            load=json.load(J)
            result=load['results'][0]
            
            pkgs={
                    'name':result['Name'],
                    'depends':result['Depends'],
                    'makeDepends':result['MakeDepends'],
                    'optDepends':result['OptDepends'],
                    'conflicts':result['Conflicts'],
                    'replaces':result['Replaces']
            }
            return pkgs

    class HiLvl:
        master=None
        def depends(self,pk):
            result=self.master.web.connect(pkg=pk)
            pkgs=self.master.web.jsonParsePkgs(result)
            return pkgs
        
        def similarPkgs(self,pk):
            result=self.master.web.connect(pkg=pk,t='search')
            pkgs=self.master.web.jsonParseNames(result)
            return pkgs

    class display:
        master=None
        def displayXML(self,data):
            pass

        def displayPlain(self,data):
            for i in data:
                formString=':'.join(['{}' for i in range(len(i))]).format(*i)
                print(formString)

        def displayProcess(self,data,mode):
            result=[]
            if type(data) == type(list()):
                for pkg in data:
                    result.append([mode,pkg])
            elif type(data) == type(dict()):
                for lisT in data.keys():
                    if lisT != 'name':
                        for pkg in data[lisT]:
                            result.append([mode,data['name'],lisT,pkg])
            else:
                result.append(data)
            #at this point decide if to print xml data or plain ascii
            ##right now assume plain
            self.displayPlain(result)    
    class cmdline:
        master=None

    class void:
        master=None

    def run(self,wa):
        wa.display.displayProcess(wa.HiLvl.depends('vlc-nox'),'info')
        wa.display.displayProcess(wa.HiLvl.similarPkgs('vlc'),'search')

    def assemble(self):
        wa=self.void()
        wa.master=self

        wa.cmdline=self.cmdline()
        wa.cmdline.master=wa

        wa.web=self.web()
        wa.web.master=wa
        
        wa.HiLvl=self.HiLvl()
        wa.HiLvl.master=wa

        wa.display=self.display()
        wa.display.master=wa
        
        self.run(wa)

run=container()
run.assemble()

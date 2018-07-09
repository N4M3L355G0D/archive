#! /usr/bin/env python3
#NoGuiLinux

import urllib.request,urllib.error
import json, argparse
from xml.etree.ElementTree import Element as element,SubElement as subElement, tostring as ts

class container:
    master=None
    class web:
        types=['search','info']
        rpcUrl='https://aur.archlinux.org/rpc/?v=5&type={}&arg={}'
        master=None
        def connect(self,t='info',pkg=''):
            try:
                conn=urllib.request.urlopen(self.rpcUrl.format(t,pkg))
                return [conn,pkg]
            except urllib.error.HTTPError as err:
                exit(str(err))
            except urllib.error.URLError as err:
                exit(str(err))

        
        def jsonParseNames(self,J=b''):
            load=json.load(J[0])
            return [i['Name'] for i in load['results']],J[1]

        def jsonParsePkgs(self,J=b''):
            load=json.load(J[0])
            result=load['results']
            if result != []:
                result=result[0]
                pkgs={}
                for pk in ['Name','Depends','OptDepends','Conflicts','Replaces']:
                    try:
                        pkgs[pk.lower()]=result[pk]
                    except:
                        pass
                
                return pkgs
            else:
                result=load['resultcount']
                return {
                        'name':self.master.cmdline.options.package,
                        'error':['RESULT_{}'.format(result)],
                        }

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

        #def displayXml(self,data,mode):

        def displayProcess(self,data,mode):
            result=[]
            if type(data) == type(list()) or type(data) == type(tuple()):
                for pkg in data[0]:
                    result.append([data[1],mode,pkg])
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
        cmdArgs={
                    'package':['-p','--package','package to look for','yes'],
                    'search':['-s','--search','mode search','store_true'],
                    'info':['-i','--info','mode info','store_true']
                }
        options=None
        def args(self):
            parser=argparse.ArgumentParser(description='',epilog='')
            for arg in self.cmdArgs.keys():
                if arg == 'package':
                    parser.add_argument(
                            self.cmdArgs[arg][0],
                            self.cmdArgs[arg][1],
                            help=self.cmdArgs[arg][2],
                            required=self.cmdArgs[arg][3]
                            )
                elif arg in ['search','info']:
                    parser.add_argument(
                            self.cmdArgs[arg][0],
                            self.cmdArgs[arg][1],
                            help=self.cmdArgs[arg][2],
                            action=self.cmdArgs[arg][3]
                            )
            self.options=parser.parse_args()


    class void:
        master=None

    def run(self,wa):
        wa.cmdline.args()
        if wa.cmdline.options.info:
            wa.display.displayProcess(wa.HiLvl.depends(wa.cmdline.options.package),'info')
        elif wa.cmdline.options.search:
            wa.display.displayProcess(wa.HiLvl.similarPkgs(wa.cmdline.options.package),'search')
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

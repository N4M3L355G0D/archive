#! /usr/bin/env python3
#NoGuiLinux

import urllib.request,urllib.error
import json, argparse
from xml.etree.ElementTree import Element as element,SubElement as subElement, tostring as ts

class container:
    master=None
    class web:
        types=['search','info']
        rpc='/rpc/?v=5&type={}&arg={}'
        url='https://aur.archlinux.org'
        rpcUrl=url+rpc
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
            result=load['results']
            come=[]
            if result != []:
                pkgs={}
                for item in result:
                    for pk in ['Name','Description']:
                        try:
                            if pk == 'Description':
                                item[pk]=item[pk]
                            pkgs[pk.lower()]=item[pk]
                        except:
                            pass
                    come.append(pkgs)
                    pkgs={}
                return come,J[1]
            else:
                result=load['resultcount']
                return [{
                        'name':self.master.cmdline.options.package,
                        'description':'ERROR_NO_RESULTS',
                        }],J[1]


            

        def jsonParsePkgs(self,J=b''):
            load=json.load(J[0])
            result=load['results']
            if result != []:
                result=result[0]
                pkgs={}
                for pk in ['Name','Depends','OptDepends','Conflicts','Replaces','URLPath','Description']:
                    try:
                        if pk == 'URLPath':
                            result[pk]=[self.url+result[pk]]
                        if pk == 'Description':
                            result[pk]=[result[pk]]
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
                formString='|'.join(['{}' for i in range(len(i))]).format(*i)
                print(formString)

        def cleanStream(self,data):
            for char in ['<','>','<=','>=','=']:
                if char in data:
                    data=data.split(char)[0]
            return data

        def displayXml(self,data):
            top=element(data[0][0],pkgname=self.cleanStream(data[0][1]))
            num=0
            diff=''
            if data[0][0] == 'info':
                for i in data:
                    if i[2] != diff:
                        num=0
                        diff=i[2]
                    else:
                        num+=1 
                    opt=subElement(top,i[2],num=str(num))
                    opt.text=self.cleanStream(i[3])
            elif data[0][0] == 'search':
                count=0
                for i in data:
                    opt=subElement(top,i[2],num=str(count))
                    subopt=subElement(opt,'pname')
                    subopt.text=i[3]
                    subopt=subElement(opt,i[4])
                    subopt.text=i[5]
                    count+=1

            print(ts(top).decode())

        def displayProcess(self,data,mode):
            result=[]
            node='error'
            if type(data) == type(list()) or type(data) == type(tuple()):
                for pkg in data[0]: 
                    result.append([
                                mode,
                                data[1],
                                'result',
                                pkg['name'],
                                'description',
                                pkg['description']
                                ])
            elif type(data) == type(dict()):
                for lisT in data.keys():
                    if lisT != 'name':
                        for pkg in data[lisT]:
                            result.append([mode,data['name'],lisT,pkg])
            else:
                result.append(data)
            #at this point decide if to print xml data or plain ascii
            ##right now assume plain
            if self.master.cmdline.options.print_plain:
                self.displayPlain(result)    
            elif self.master.cmdline.options.print_xml:
                self.displayXml(result)
            else:
                self.displayPlain(result)

    class cmdline:
        master=None
        cmdArgs={
                    'package':[
                        '-p',
                        '--package',
                        'package to look for',
                        'yes'
                        ],
                    'search':[
                        '-s',
                        '--search',
                        'mode search',
                        'store_true'
                        ],
                    'info':[
                        '-i',
                        '--info',
                        'mode info',
                        'store_true'
                        ],
                    'xml':[
                        '-x',
                        '--print-xml',
                        'print results in xml',
                        'store_true'
                        ],
                    'plain':[
                        '-a','--print-plain',
                        'print results plain',
                        'store_true'
                        ]
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
                elif arg in ['search','info','plain','xml']:
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

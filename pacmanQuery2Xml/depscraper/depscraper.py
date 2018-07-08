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

        def jsonParsePkgs(self,J=b''):
            load=json.load(J)
            result=load['results'][0]
            
            pkgs={
                    'depends':result['Depends'],
                    'makeDepends':result['MakeDepends'],
                    'optDepends':result['OptDepends'],
                    'conflicts':result['Conflicts'],
                    'replaces':result['Replaces']
            }
            return pkgs

    class void:
        master=None

    def run(self,wa):
        result=wa.web.connect(pkg='vlc-nox')
        res=wa.web.jsonParsePkgs(result)
        print(res)

    def assemble(self):
        wa=self.void()
        wa.master=self

        wa.web=self.web()
        wa.web.master=wa

        self.run(wa)

run=container()
run.assemble()

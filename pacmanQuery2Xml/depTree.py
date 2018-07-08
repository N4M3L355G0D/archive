#! /usr/bin/env python3
#NoGuiLinux
#this script is to replace the optDepTree.py script as this relies on an
#iterable based system rather than the massive reliance on recursion
#that is seen in optDepTree.py

import pyalpm,argparse
#loop through a list of pkgs, if the current pkg has deps add to list of pkgs, until for loop reaches end of list

#getDeps() will get the dependency list of the current package and return the list() if there is one, otherwise return None

class container:
    master=None
    class modes:
        OPT_DEPS=1
        REQ_DEPS=2
        BOTH_DEPS=3

    class application:
        master=None
        pkgs=['mplayer']

        def setHandle(self):
            h=pyalpm.Handle('/','/var/lib/pacman')
            return h

        def setRemote(self,handle):
            dbs=['extra','community','core']
            db={}
            for d in dbs:
                db[d]=handle.register_syncdb(d,pyalpm.SIG_DATABASE_OPTIONAL)
            sync=handle.get_syncdbs()
            return db

        def setLocal(self,handle):
            return handle.get_localdb()

        def getDeps(self,pkg,db,mode=2):
            deps=None
            for repo in db.keys():
                pk=db[repo].get_pkg(pkg)
                if pk != None:
                    if mode == self.master.modes.REQ_DEPS:
                        deps=pk.depends
                    elif mode == self.master.modes.OPT_DEPS:
                        deps=[i.split(':')[0] for i in pk.optdepends]
                    elif mode == self.master.modes.BOTH_DEPS:
                        deps=pk.depends
                        deps.extend([i.split(':')[0] for i in pk.optdepends])
                    break
            return deps

        def resolve(self,pkgs=[],mode=2,statusInstalled=False):
            opk=len(pkgs)
            oPk=pkgs
            if pkgs != []:
                handle=self.setHandle()
                lDb=self.setLocal(handle)
                rDb=self.setRemote(handle)
        
                for pkg in pkgs:
                    deps=self.getDeps(pkg,rDb,mode=mode)
                    if deps:
                        for pkg_sub in deps:
                            #ensure we are not adding duplicate pkg names to the list
                            if pkg_sub not in pkgs: 
                                if statusInstalled == False:
                                    installed=lDb.get_pkg(pkg_sub)
                                    if installed == None:
                                        pkgs.append(pkg_sub)
                                elif statusInstalled == True:
                                    pkgs.append(pkg_sub)
                    del(deps)
                if len(pkgs) > opk:
                    return pkgs[opk:]
                else:
                    return []
            else:
                return 'return empty pkgs list'

    class cmdline:
        master=None
        opts={
                'pkg':['-p','--package','package, or comma delimited list of packages to get dependencies for','yes'],
                'mode':['-m','--mode','one of [req=2||opt=1||both=3] for dependency types i.e. -m 2','yes'],
                'installed':['-i','--include-installed','include installed packages in list','store_true']
                }
        options=None

        def description(self):
            desc='''
            utilize the alpm library to gather depency 
            information on a pkg, and only display the 
            dependencies not installed.
            '''.replace('\t','')
            return desc

        def args(self):
            parser=argparse.ArgumentParser(description=self.description())
            for opt in self.opts.keys():
                if opt == 'installed':
                    parser.add_argument(self.opts[opt][0],self.opts[opt][1],help=self.opts[opt][2],action=self.opts[opt][3])
                else:
                    parser.add_argument(self.opts[opt][0],self.opts[opt][1],help=self.opts[opt][2],required=self.opts[opt][3])
               
            self.options=parser.parse_args()
        def parseModes(self):
            if self.options.mode != None:
                try:
                    mode=int(self.options.mode)
                except:
                    exit('that is not a valid mode!')
                if 0 < mode < 4:
                    return mode
                else:
                    exit('mode must be one of the range 1-3')
                

    class display:
        master=None
        def display(self,dataSet):
            if type(dataSet) == type(list()):
                for element in dataSet:
                    print(element)
            else:
                print(element)
    class void:
        master=None

    def run(self,workArea):
        workArea.cmdline.args()
        mode=workArea.cmdline.parseModes()
        installed=workArea.cmdline.options.include_installed
        workArea.application.pkgs=workArea.cmdline.options.package.split(',')
        deps=workArea.application.resolve(workArea.application.pkgs,mode=mode,statusInstalled=installed)
        workArea.display.display(deps)

    def assemble(self):
        workArea=self.void()
        workArea.master=self
       
        workArea.modes=self.modes()

        workArea.cmdline=self.cmdline()
        workArea.cmdline.master=workArea

        workArea.application=self.application()
        workArea.application.master=workArea
        
        workArea.display=self.display()
        workArea.display.master=workArea

        self.run(workArea)

app=container()
app.assemble()

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

        def getDeps(self,pkg,db):
            deps=None
            for repo in db.keys():
                pk=db[repo].get_pkg(pkg)
                if pk != None:
                    deps=pk.depends
                    break
            return deps

        def resolve(self,pkgs=[]):
            opk=len(pkgs)
            oPk=pkgs
            if pkgs != []:
                handle=self.setHandle()
                lDb=self.setLocal(handle)
                rDb=self.setRemote(handle)
        
                for pkg in pkgs:
                    deps=self.getDeps(pkg,rDb)
                    if deps:
                        for pkg_sub in deps:
                            #ensure we are not adding duplicate pkg names to the list
                            if pkg_sub not in pkgs:
                                installed=lDb.get_pkg(pkg_sub)
                                if installed == None:
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
        opts={'pkg':['-p','--package','package, or comma delimited list of packages to get dependencies for','yes']}
        options=None
        def args(self):
            parser=argparse.ArgumentParser()
            for opt in self.opts.keys():
                parser.add_argument(self.opts[opt][0],self.opts[opt][1],help=self.opts[opt][2],required=self.opts[opt][3])
            self.options=parser.parse_args()
            
            

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
        workArea.application.pkgs=workArea.cmdline.options.package.split(',')
        deps=workArea.application.resolve(workArea.application.pkgs)
        workArea.display.display(deps)

    def assemble(self):
        workArea=self.void()
        workArea.master=self
        
        workArea.cmdline=self.cmdline()
        workArea.cmdline.master=workArea

        workArea.application=self.application()
        workArea.application.master=workArea
        
        workArea.display=self.display()
        workArea.display.master=workArea

        self.run(workArea)

app=container()
app.assemble()

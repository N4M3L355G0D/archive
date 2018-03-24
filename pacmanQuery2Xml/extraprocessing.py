#! /usr/bin/env python3
#NoGuiLinux
import os, argparse

class extraProcessing:
    conflictsFile=''
    pkgFile=''
    outFile=''
    WARNED=False
    def checks(self):
        NOEXIST='\033[1;5;31;40mCritical file missing:\033[0m {}'
        TOOLATE='''\033[1;33;40m
        If you are seeing this you are not too late,\033[0m
        
        \033[1;5;31;40moutFile '{}' exists!\033[0m 
        
        \033[1;33;40mIf you see the next prompt in\033[0m \033[1;4;31;40mRED\033[0m\033[1;33;40m,
        you are too late!\033[0m
        '''
        if not os.path.exists(self.conflictsFile):
            exit(NOEXIST.format(self.conflictsFile))
        if not os.path.exists(self.pkgFile):
            exit(NOEXIST.format(self.pkgFile))
        if os.path.exists(self.outFile):
            self.WARNED=True
            print(TOOLATE.format(self.outFile))
    def loading(self,msg):
        print('\033[1;32;40m{}\033[0m'.format(msg))

    def proc(self):
        #load conflicts into memory
        conflicts=[]
        finality=[]
        self.loading('loading conflicts into memory...')
        with open(self.conflictsFile,"rb") as conflictData:
            for line in conflictData:
                conflicts.append(line.rstrip(b'\n'))
        self.loading('looking for conflicts...')
        with open(self.pkgFile,"rb") as pkgData:
            for line in pkgData:
                line=line.rstrip(b'\n')
                if line not in conflicts:
                    finality.append(line)
        with open(self.outFile,"wb") as oData:
            if self.WARNED == True:
                print('\033[1;31;40mWell, I warned you...\033[0m')
            self.loading('writing results to file : "{}"'.format(self.outFile))
            for line in finality:
                line=line+b'\n'
                oData.write(line)

class clean:
    def cleanup(self):
        os.remove(process.pkgFile)
        os.remove(process.conflictsFile)


class cmdline:
    def cmd(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-c','--conflicts',required='yes')
        parser.add_argument('-p','--packages',required='yes')
        parser.add_argument('-o','--output',required='yes')
        options,unkown=parser.parse_known_args()
        return options

args=cmdline()
opts=args.cmd()
process=extraProcessing()
process.conflictsFile=opts.conflicts
process.pkgFile=opts.packages
process.outFile=opts.output
process.checks()
process.proc()
cln=clean()
cln.clean()


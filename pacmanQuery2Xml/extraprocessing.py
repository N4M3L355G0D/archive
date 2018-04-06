#! /usr/bin/env python3
#NoGuiLinux
import os, argparse

class extraProcessing:
    pkgFile=''
    outFile=''
    def checks(self):
        NOEXIST='\033[1;5;31;40mCritical file missing:\033[0m {}' 
        if not os.path.exists(self.pkgFile):
            exit(NOEXIST.format(self.pkgFile))

    def loading(self,msg):
        print('\033[1;32;40m{}\033[0m'.format(msg))

    def dedupe(self):
        packages=[]
        self.loading('beginning de-duping process...') 
        with open(self.pkgFile,'rb') as iData:
            for line in iData:
                line=line.rstrip(b'\n')
                if line not in packages:
                    packages.append(line)
        with open(self.outFile,'wb') as oData:
                for line in packages:
                    line=line+b'\n'
                    oData.write(line)

class cmdline:
    def cmd(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-p','--packages',required='yes')
        parser.add_argument('-o','--output',required='yes')
        options,unkown=parser.parse_known_args()
        return options

args=cmdline()
opts=args.cmd()
process=extraProcessing()
process.pkgFile=opts.packages
process.outFile=opts.output
process.checks()
process.dedupe()


#! /usr/bin/env python3
#NoGuiLinux
#convert a text file to line by line base64 then followed by gzip compression
#call this prog carbonite.py
import base64, gzip, os, argparse

class color:
    startBoldBlinkRed='\033[1;5;31;40m'
    reset='\033[0m'
    startBoldYellow='\033[1;33;40m'
    startBoldGreen='\033[1;32;40m'
    startBoldRed='\033[1;31;40m'
    startBoldULine='\033[1;4m'
    startBold='\033[1m'
colors=color()

class conform:
    #need a verbose option
    #need a cmdline argument class
    ofile=''
    file='biglist.txt'
    ext='.b64.gz'
    gzMul=10

    def cmdline(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-i','--infile',required='yes')
        parser.add_argument('-c','--chunkSize',help="{}multiples{} of {}1024 Bytes{} to compress in chunks {}GZIP [Default:{}]{}".format(colors.startBoldGreen,colors.reset,colors.startBoldYellow,colors.reset,colors.startBoldRed,self.gzMul,colors.reset))
        #more options will be added later
        options,unknown=parser.parse_known_args()
        if options.infile:
            self.file=options.infile
        if options.chunkSize:
            try:
                self.gzMul=int(options.chunkSize)
            except:
                exit("{}chunkSize is not a useable as TYPE INT{}".format(colors.startBoldRed,colors.reset))

    def setOFile(self):
        self.ofile=os.path.splitext(self.file)[0]+self.ext

    def checkFileExists(self):
        #check for IN-file
        #do not care about ofile or its bastard parent *.tmp as it new data would be better
        #backups need to taken care of by the user
        if not os.path.exists(self.file):
            exit("{} '{}' : Does not Exist {}".format(colors.startBoldYellow,self.file,colors.reset))
        if not os.path.isfile(self.file):
            exit("{} '{}' : Not a File {}".format(colors.startBoldYellow,self.file,colors.reset))
        #if ofile exists but is not a regular file, then we must care a little; like the difference between alemony and an abortion
        if os.path.exists(self.ofile) and not os.path.isfile(self.ofile):
            exit("{} '{}' : Exists, but is not a {}{}'Regular File'{}".format(colors.startBoldYellow,self.ofile,colors.reset,colors.startBold,colors.reset))

    def base64(self):
        print('{}base64 - stage begin{}'.format(colors.startBoldBlinkRed,colors.reset))
        with open(self.file,'rb') as data, open(self.ofile,'wb') as odata:
            for line in data:
               odata.write(base64.b64encode(line)+b'\n')
        print('{}base64 - stage done{}'.format(colors.startBoldYellow,colors.reset))

    def gzArchive(self):
        print('{}gzip - stage begin{}'.format(colors.startBoldBlinkRed,colors.reset))
        mul=self.gzMul
        with open(self.ofile,'rb') as data, open(self.file+'.tmp','wb') as odata:
            while True:
                d=data.read(1024*mul)
                if not d:
                    break
                odata.write(gzip.compress(d))
        print('{}gzip - stage done{}'.format(colors.startBoldYellow,colors.reset))

    def cleanup(self):  
        print('{}Finishing up!{}'.format(colors.startBoldBlinkRed,colors.reset))
        os.remove(self.ofile)
        os.rename(self.file+'.tmp',self.ofile)
        print('{}Done{}{}!{}'.format(colors.startBoldGreen,colors.reset,colors.startBoldBlinkRed,colors.reset))

    def conformist(self):
        self.cmdline()
        self.setOFile()
        self.checkFileExists()
        self.base64()
        self.gzArchive()
        self.cleanup()

a=conform()
a.conformist()

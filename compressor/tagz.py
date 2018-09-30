#! /usr/bin/python3

#a simple archiver+compressor with currently no error checking
#hackit/noguilinux
#5.27.2017

import tarfile, argparse, gzip, time

import os,sys

class tagz():
    def dotdot(self,tarinfo):
        member_notes=str()
        if ".." in tarinfo.name:
            tarinfo.name=tarinfo.name.replace("../","")
            member_notes=tarinfo.name+"had '../', so removed"
            print(member_notes)
        return tarinfo

    #set ofile to another string to set path || or name of final compressed archive
    ofile="defaults"
    ext=".tar"
    idf=None

    def __init__(self):
        #self.archComp()
        pass

    def transform(self,inval):
        if int(inval) < 10:
            inval="0"+str(inval)
        else:
            inval=str(inval)
        return inval

    def localtime(self):
        #desired format mmddyyyy-hhmmss
        #becomes major-minor
        local=time.localtime()
        #create major sections
        month=self.transform(local.tm_mon)
        day=self.transform(local.tm_mday)
        year=self.transform(local.tm_year)
        #lets make the major
        major=month+day+year
        #create minor sections
        hour=self.transform(local.tm_hour)
        minute=self.transform(local.tm_min)
        second=self.transform(local.tm_sec)
        #lets make the minor
        minor=hour+minute+second
        #complete final format
        final=major+"-"+minor
        return final
    
    def archComp(self):
        ofile_tar=self.ofile+self.ext        
        ofile_gz=ofile_tar+".gz"
        #idf ; input directory or file
        idf=self.idf
        mode="w"
        if os.path.exists(ofile_gz):
            ofile_gz=self.ofile+"."+str(self.localtime())+self.ext+".gz"

        #archive section
        try:
            tar=tarfile.TarFile(ofile_tar,mode)
            tar.add(idf,filter=self.dotdot)
            tar.close()
        except (RuntimeError,NameError,TypeError) as err:
            for i in err:
                for x in i:
                    print(x)
        try:
            #compression section
            gz=gzip.GzipFile(ofile_gz,mode)
            #need to read tarball in binary mode so as to use the gz.write method
            if os.path.exists(ofile_tar):
                file=open(ofile_tar,"rb")
                for i in file:
                    gz.write(i)
                gz.close()
                os.remove(ofile_tar)
            else:
                print("somthing must happened in the tar section [tarball does not exist]")
        except (RuntimeError,NameError,TypeError) as err:
            for i in err:
                for x in i:
                    print(x)

class readArch():
    def __init__(self):
        pass

    infile=""
    operation="list"
    member=list()
    def read(self,member=False):
        mode="r:gz"
        if os.path.exists(self.infile):
            tarball=tarfile.open(self.infile,mode)
            if self.operation == "list":
                tarball.list()
            elif self.operation == "extract-all":
                tarball.extractall()
            elif self.operation == "extract-member":
                for i in self.member:
                    if i in tarball.getnames():
                        tarball.extract(i)


#archcomp=tagz()

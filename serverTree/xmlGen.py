#! /usr/bin/env python3

from xml.etree.ElementTree import Element as element, SubElement as subElement, Comment as comment, tostring
import os, hashlib
import pwd,grp

class docGen:
    manifest="manifest.xml"
    verbose=False
    def integrity(self,fname):
        obj=hashlib.sha512()
        with open(fname,"rb") as file:
            while True:
                data=file.read(1024)
                if not data:
                    break
                obj.update(data)
        return obj.hexdigest()

    def fsize(self,fname):
        return str(os.stat(fname).st_size)

    def getUserGroup(self,fname):
        gid=os.stat(fname).st_gid
        uid=os.stat(fname).st_uid
        group=grp.getgrgid(gid)[0]
        user=pwd.getpwuid(uid)[0]
        return (str(user),str(uid),str(group),str(gid))

    def getPermissions(self,fname):
        return str(oct(os.stat(fname)[0]))[4:]

    def getFileType(self,fname):
        num=str(oct(os.stat(fname)[0]))[2:4]
        types={"01":"FIFO","02":"character device","40":"Directory","60":"block device","10":"Regular file","12":"symbolic link","14":"socket","17":"bit mask for the file type bitfields"}
        keys=[key for key in types.keys()]
        if num in keys:
            return types[num]
        else:
            return num
    
    def genXml(self,dir='.'):
        path=os.path.realpath(dir)
        dirStrip=os.path.dirname(path)
        top = element("Directory",path=os.path.basename(path))
        counter=0
        dircounter=0
        for root,dirname,fnames in os.walk(path):
            dirs=subElement(top,'dir',num=str(dircounter),dpath=root.strip(dirStrip))
            counter=0
            dircounter+=1
            names=subElement(dirs,'dirname')
            names.text=root.strip(dirStrip)
            for fname in fnames:
                fpath=os.path.join(root,fname)
                if os.path.exists(fpath):
                    if self.verbose == True:
                        print(fpath)
                    names=subElement(dirs,'file',num=str(counter))
                    subNames=subElement(names,'fname')
                    subNames.text=fname
                    nameStat=subElement(names,'fsize')
                    nameStat.text=self.fsize(fpath)
                    integ=subElement(names,'integ')
                    integ.text=self.integrity(fpath)
                    uid=subElement(names,"uid")
                    uid.text=self.getUserGroup(fpath)[1]
                    user=subElement(names,"user")
                    user.text=self.getUserGroup(fpath)[0]
                    gid=subElement(names,"gid")
                    gid.text=self.getUserGroup(fpath)[3]
                    group=subElement(names,"group")
                    group.text=self.getUserGroup(fpath)[2]
                    permissions=subElement(names,"permissions")
                    permissions.text=self.getPermissions(fpath)
                    ftype=subElement(names,"ftype")
                    ftype.text=self.getFileType(fpath)
                    #do file integreity check and record
                    counter+=1    
                else:
                    print('path {} is a broken symlink'.format(fpath))
        file=open(self.manifest,"wb")
        file.write(tostring(top))

gen=docGen()
gen.verbose=True
gen.genXml("/home/carl/Documents")

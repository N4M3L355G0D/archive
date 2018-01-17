#! /usr/bin/env python3
#NoGuiLinux
#pihole-hosts.txt stripper

import os
class stripper:
    WARN_INVALID_PATH="That path does not exist! using PWD!\n File will be saved as : "
    ERR_INVALID_CHAR="Invalid characters were detected in FPATH"
    ERR_PATH_FILE_BLANK="Path/and/Filename cannot be blank"
    ERR_FILE_EXISTS="There is something already there by that name!"
    ERR_HAS_PATH_NO_FNAME="A path was given, but no filename"
    ERR_BAD_FNAME="Filename cannot be :"
    ERR_NO_SAVE="Nothing will be Saved!"

    user=os.environ['USER']
    answers=['yes','no']
    invalid=["",'\n','\t',' ','\r','\\']
    hosts=b''
    rootSave="/etc/hosts"
    writeModes=["a","w"]


    #file to be stripped, from pihole-master.zip
    file="hosts.txt"
    
    
    def write2File(self,location='',Hosts=b''):
        mode=''
        W2File=''
        W2File=str(input("write to "+str(location)+"? : "))
        while W2File not in self.answers:
            W2File=str(input("write "+str(location)+"? ['yes','no'] : "))
        if W2File == 'yes':
            if self.user == "root":
                while mode not in self.writeModes:
                    mode=str(input("what write mode do you want to use ['a' for 'append', or 'w' for 'overwrite']: ")).rstrip("\n")
            else:
                mode='w'
            ofile=open(str(location),mode+"b")
            ofile.write(Hosts)
            ofile.close()
        else:
            print(self.ERR_NO_SAVE)
    
    
    def main(self):
        with open(self.file,"rb") as data:
            for line in data:
                if len(line) > 1:
                    if line[0] != ord("\n"):
                        if line[0] != ord('#'):
                            print(line)
                            self.hosts+=line
        if self.user == "root":
            self.write2File(location=self.rootSave,Hosts=self.hosts)
        elif self.user != "root":
            index=0
            userland=str(input("Where to write data? : "))
            if (os.path.split(userland)[0] == "") and len(os.path.split(userland)) > 1:
                index=1
        
            if os.path.exists(os.path.split(userland)[index]):
                if os.path.split(userland)[1] != "":
                    if userland not in self.invalid:
                        if index > 0:
                            print(self.ERR_BAD_FNAME+' {}'.format(os.path.split(userland)[index]))
                        elif not os.path.exists(userland):
                            self.write2File(location=userland,Hosts=self.hosts)
                        else:
                            if os.path.isdir(userland):
                                print(self.ERR_HAS_PATH_NO_FNAME)
                            else:
                                print(self.ERR_FILE_EXISTS)
                    else:
                        print(self.ERR_INVALID_CHAR)
                else:
                    print(self.ERR_PATH_FILE_BLANK)
            else:
                if userland not in self.invalid:
                    userland="./"+str(userland.replace('/','0x'+str(ord('/'))))
                    print(self.WARN_INVALID_PATH+' {}'.format(userland))
                    self.write2File(location=userland,Hosts=self.hosts)
                else:
                    print(self.ERR_INVALID_CHAR)
a=stripper()
a.main()

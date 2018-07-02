class smbRead:
    smbfile='/etc/samba/smb.conf'
    
    shareDec='''
[storage]
 comment= remote block device storage
 browseable = yes
 writable = yes
 path = /srv/samba/storage
 create mask = 0777
 directory mask = 0777
 force user = root'''
    shareName=[]
    share=False
    shareL=[]
    start=0
    end=0
    def sharename(self,data,counter):
        if data == b'[':
            self.share=True
            self.end=counter-1
        elif data == b']':
            self.share=False
            self.shareName.append(data)
            self.start=counter+1
        if self.share == True:
            self.shareName.append(data)
        else:
            if b''.join(self.shareName) != b'':
                share=b''.join(self.shareName).decode()
                self.shareL.append({'share':share,'start':self.start,'end':self.end})
            self.shareName=[]

def display(name,data):
    return '{}\n{}'.format(name,data)

def countLines(string):
    l=string[1].split('\n')
    counter=0
    lcount=len(l)
    for i in l:
        if i != '':
            if i[0] in [';','#']:
                counter+=1
        else:
            counter+=1
    if counter == lcount:
        return ';'+string[0]
    else:
        return string[0]

def getshares():
    storage=[]
    counter=1
    with open(s.smbfile,'rb') as ifile:
        while True:
            data=ifile.read(1)
            if not data:
                break
            s.sharename(data,counter)
            counter+=1
    
    points=[]
    for num,i in enumerate(s.shareL):
        if num < len(s.shareL)-1:
            points.append([s.shareL[num]['start'],s.shareL[num+1]['end']-s.shareL[num]['start']])

    counter=1
    with open(s.smbfile,'rb') as ifile:
        for num,i in enumerate(points):
            ifile.seek(i[0])
            idata=ifile.read(i[1])
            stringy=s.shareL[num]['share'],idata.decode()
            storage.append(display(countLines(stringy),stringy[1]))
        ifile.seek(s.shareL[-1]['start'])
        while True:
            idata=ifile.read(1)
            if not idata:
                break
            counter+=1
    
    with open(s.smbfile,'rb') as ifile:
        ifile.seek(s.shareL[-1]['start'])
        idata=ifile.read(counter)
        stringy=s.shareL[-1]['share'],idata.decode()
        storage.append(display(countLines(stringy),stringy[1]))
    return storage

def compare():
    storage=getshares()
    found=False
    for share in storage:
        if s.shareDec.replace('\n','') in share.replace('\n',''):
            print(s.shareDec)
            found=True
            break
    if found == True:
        return 0
    if found == False:
        return 1

def writer(result):
    if result == 1:
        try:
            with open(s.smbfile,'ab') as ofile:
                ofile.write(s.shareDec.encode())
            return 0
        except OSError as err:
            return str(err)
    else:
        print('\n\nthe share already exists!')
        return 0

s=smbRead()
result=compare()
exit(writer(result))

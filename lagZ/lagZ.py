#! /usr/bin/env python3

import gzip,sys,argparse,lzma, os

try:
    from PyCryptodome.Cipher import AES
except:
    from Cryptodome.Cipher import AES


class app:
    master=None
    class algos:
        master=None
        
        def fixkey(self,password=b''):
            if type(password) != type(bytes()):
                password=password.encode()
            return password+b' '*(32-len(password))

        def createCipher(self,iv=None):
            if iv == None:
                iv=os.urandom(16)
            password=self.fixkey(self.master.names.password)
            cipher=AES.new(password,mode=AES.MODE_EAX,nonce=iv)
            return cipher

    class names:
        master=None
        ifname=None
        password=None
        ofname=None
        decryptName=None
        mode=None
        def __init__(self):
            dot=''
            if len(sys.argv) >= 4:
                self.ifname=sys.argv[1]
                self.password=sys.argv[2]
                self.ofname=self.ifname+".lagZ"
                self.mode=sys.argv[3]
                if self.mode not in ['enc','dec']:
                    exit('incorrect mode. needs to be one of <enc|dec>!')

                file=os.path.splitext(self.ifname)
                if file[1] != '':
                    dot='.'
                self.decryptName=file[0]+'-dec'+dot+file[1]
            else:
                exit("missing possitional args $cmd <FILE> <PASS> <enc|dec>")
        
        lzmaChunkSize=1024

    class encrypt:
        master=None

        def encryptChunk(self,chunk):
            cipher=self.master.algos.createCipher()
            encDat,tag=cipher.encrypt_and_digest(chunk)
            encDat=tag+cipher.nonce+encDat
            return encDat

        def encryptFile(self):
            with open(self.master.names.ifname,'rb') as ifile, open(self.master.names.ofname,'wb') as ofile:
                while True:
                    idata=ifile.read(self.master.names.lzmaChunkSize)
                    if not idata:
                        break
                    gzDat=gzip.compress(idata,compresslevel=9)
        
                    encDat=self.encryptChunk(gzDat)
                    
                    lzmaDat=lzma.compress(encDat,preset=lzma.PRESET_EXTREME)
                    size='0'*(len(str(self.master.names.lzmaChunkSize))-len(str(len(lzmaDat))))+str(len(lzmaDat))
                    ofile.write(size.encode()+lzmaDat)
            print(self.master.mesg.done.format(self.master.colors.green,self.master.colors.end,self.master.names.ofname,self.master.names.mode,'Done'))

    class mesg:
        master=None
        done='{0}MODE:{3} STATUS:{4}! OFNAME:"{2}"{1}'

    class decrypt:
        master=None
        authentic=0
        invalid=0
        def decrypt(self,edata):
            tag=edata[:16]
            nonce=edata[16:32] 
            ciphertext=edata[32:]
            decipher=self.master.algos.createCipher(iv=nonce)
            gzdata=decipher.decrypt(ciphertext)
            
            self.verify(tag,decipher)

            return gzdata

        def verify(self,tag,decipher):
            try:
                decipher.verify(tag)
                self.authentic+=1
            except:
                self.invalid+=1

        def decryptFile(self):
            with open(self.master.names.ofname,'rb') as ifile, open(self.master.names.decryptName,'wb') as ofile:
                while True:
                    chunk=ifile.read(4)
                    if not chunk:
                        break
                    idata=ifile.read(int(chunk))
                    if not idata:
                        break

                    edata=lzma.decompress(idata)

                    gzdata=self.decrypt(edata)
                   
                    
                    rawdata=gzip.decompress(gzdata)
                    ofile.write(rawdata)
            print(self.master.mesg.done.format(self.master.colors.green,self.master.colors.end,self.master.names.decryptName,self.master.names.mode,'Done'))

        def displayAuth(self):
            print('{0}failed{1} authenticity in {0}{2}{1} locations'.format(
                self.master.colors.red,
                self.master.colors.end,
                self.invalid
                ))
            print('{0}valid{1} authenticity in {0}{2}{1} locations'.format(
                self.master.colors.green,
                self.master.colors.end,
                self.authentic
                ))

    class colors:
        green='\033[1;32;40m'
        red='\033[1;31;40m'
        end='\033[0;m'

    class workarea:
        master=None

    def run(self,wa):
        if wa.names.mode == 'enc':
            wa.encrypt.encryptFile()
        elif wa.names.mode == 'dec':
            wa.decrypt.decryptFile()
            wa.decrypt.displayAuth()
        else:
            exit('incorrect mode')

    def assemble(self):
        wa=self.workarea()
        wa.master=self
        
        wa.mesg=self.mesg()
        wa.mesg.master=wa

        wa.colors=self.colors()
        wa.colors.master=wa

        wa.names=self.names()
        wa.names.master=wa

        wa.algos=self.algos()
        wa.algos.master=wa

        wa.encrypt=self.encrypt()
        wa.encrypt.master=wa

        wa.decrypt=self.decrypt()
        wa.decrypt.master=wa

        self.run(wa)

app=app()
app.assemble()

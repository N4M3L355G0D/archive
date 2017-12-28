#! /usr/bin/python3

import keygen_nextgen, argparse
from crypt import eCrypt
import os

def cmdline():
    parser=argparse.ArgumentParser()
    parser.add_argument("-k","--keyfile",required="yes")
    parser.add_argument("-d","--destination-data-file")
    parser.add_argument("-e","--encrypt",action="store_true")
    parser.add_argument("-D","--decrypt",action="store_true")
    parser.add_argument("-s","--source-data-file")
    options=parser.parse_args()
    return options

def main():
    noexist=" does not exist!"
    key=keygen_nextgen.keygen()
    key.noDelim=True
    
    cmd=cmdline()

    
    d=eCrypt()
    d.demo=False
    d.printVal['encrypt']=False
    d.printVal['decrypt']=False
    d.keyfile=cmd.keyfile
    d.message=cmd.destination_data_file
    d.key=key.nonceTotal()
    if cmd.encrypt == True:
        if not cmd.source_data_file:
            print("please add --source-data-file argument")
            exit
        elif not cmd.destination_data_file:
            print("please add --destination-data-file argument")
            exit
        elif os.path.exists(cmd.source_data_file):
            file=open(d.keyfile,"wb")
            file.write(d.key)
            file.close()
            hfile=cmd.source_data_file
            bash_history=open(hfile,"r")
            for i in bash_history.read():
                d.text+=i
            d.encrypt()
        else:
            print(cmd.source_data_file+noexist)
    elif cmd.decrypt == True:
        if not cmd.destination_data_file:
            print("please add --destination-data-file argument")
            exit

        elif os.path.exists(d.message):
            if os.path.exists(d.keyfile):
                try:
                    a=d.decrypt().decode()
                    print(a)
                except:
                    print("could not decode data!")
            else:
                print(d.keyfile+noexist)
        else:
            print(d.message+noexist)
    else:
        print("please specify either -e, or -D")

main()

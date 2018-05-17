#! /usr/bin/env python3

import os,sys
import curses as nc
import string
import subprocess as sp

def printHelp():
    chars=[]
    counter=0
    for i in string.printable:
        chars.append(ord(i))
    chars=sorted(chars)
    for i in chars:
        if ( counter % 12 ) != 0:
            print("{}->{} ".format(i,chr(i).encode()),end='')
        else:
            print("")
            print("{}->{} ".format(i,chr(i).encode()),end='')

        counter+=1
    print('')

def printCmd():
    cmds=['help','CMD','run','quit','editor']
    cmds=['#{}#'.format(i) for i in cmds]
    cmds0x=['.'.join([str(ord(x)) for x in i]) for i in cmds]
    for num,i in enumerate(cmds):
        print(i,cmds0x[num])

def getCmd(promptView=None):
    if promptView == None:
        pre=''
    else:
        pre=promptView
    char=input("{}hex string: ".format(pre))
    if char == '-9999+':
        printHelp()
    elif char == '-9998+':
        printCmd()
    else:
        chunk_size=2
        hexString=char.split('.')
        shellAcc=''
        for unit in hexString:
            try:
                stringChar=chr(int(unit))
                shellAcc+=stringChar
            except ValueError as err:
                print(str(err))
        print(shellAcc)
        return shellAcc

def answer(msg):
    return input("[{}]{}->{} or {}->{}: ".format(msg,ord('y'),'y',ord('n'),'n'))


def main():
    while True:
        try:
            shellAcc=getCmd()
            if shellAcc == '#help#':
                printHelp()
            if shellAcc == '#CMD#':
                printCmd() 
            if shellAcc == '#quit#':
                print('user quits: {}'.format(shellAcc))
                break
            if shellAcc == '#editor#':
                #the below code is purely supplementary -- an actual buffering editor will be added later
                text=getCmd('[editor]')
                print(text)
                while True:
                    user=answer('write')
                    if user == str(ord('y')):
                        user=input("filename in 0x: ")
                        acc=''
                        user=''.join([str(chr(int(i))) for i in user.split('.')]).encode()
                        file=open(user,'wb')
                        file.write(text.encode())
                        file.close()
                        break
                    else:
                        print('did not write data!')
                        break
            if shellAcc == '#run#':
                shellCmd=getCmd('[run]')
                print("execute cmd: '{}'".format(shellCmd))
                while True:
                    user=answer('execute')
                    print(user.encode())
                    if user == str(ord('y')):
                        cmd=sp.Popen(shellCmd,shell=True,stdout=sp.PIPE)
                        result,err=cmd.communicate()
                        try:
                            print(result.decode())
                        except:
                            print(result)
                        if err:
                            print(error)
                        break
                    else:
                        print("cmd '{}' : not executed".format(shellCmd))
                        break
        except EOFError as err:
            print('{} : user press EOF SEQUENCE'.format(str(err)))
            break
        except OSError as error:
            print('{} : Error'.format(str(error)))

if __name__ == "__main__":
    main()

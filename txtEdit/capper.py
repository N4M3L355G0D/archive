#! /usr/bin/env python3

import string as st
import subprocess as sp

string="this is a list comprehension: [i for i in 'string' if ord(i) in [x for x in range(30,127)]]"

def wordCap(string=''):
    acc=''
    for num,char in enumerate(string.split(" ")):
        if len(char) < 2:
            acc+=char.upper()
        else:
            if char[0] in st.ascii_letters:
                acc+=char[0].upper()+char[1:].lower()
        if num < len(string.split())-1:
            acc+=" "
    return acc

def inverseWordCap(string=''):
    acc=''
    for num,char in enumerate(string.split(" ")):
        if len(char) < 2:
            acc+=char.lower()
        else:
            if char[0] in st.ascii_letters:
                acc+=char[0].lower()+char[1:].upper()
        if num < len(string.split(" "))-1:
            acc+=" "
    return acc

def spellCheck(string=''):
    string=string.lower()
    cmd="echo \""+string+"\" | aspell -a"
    cmdSp=sp.Popen(cmd,shell=True,stdout=sp.PIPE)
    res,err = cmdSp.communicate()
    return (res,err)
def rightWrong(string=''):
    correction=dict()
    skip="@(#) International Ispell Version"
    for line in string.split("\n"):
        if skip not in line:
            if len(line) > 0:
                if line[0] == "&":
                    line=line[2:]
                    incorrect=line.split(":")[0].split(" ")
                    suggestions=line.split(":")[1].split(",")
                    correction[incorrect[0]]={'incorrect':incorrect,'suggestions':suggestions}
    return correction
    #aspell nuances to be aware of
    ##wrong first char starts with &
    ##right first char starts with *

## function testing
string=input(": ")

a=spellCheck(string)
corrections=rightWrong(a[0].decode())
if len(corrections) > 0:
    print(corrections)

alteredString=wordCap(string)
print(alteredString)
alteredString=inverseWordCap(string)
print(alteredString)

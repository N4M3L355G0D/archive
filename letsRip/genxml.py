#! /usr/bin/env python3
import os,sys
from xml.etree.ElementTree import Element,SubElement,tostring
import xml.etree.ElementTree as ET
import subprocess as sp
import shutil
if len(sys.argv) < 2:
    exit("please give fname")

def genXml(fname=''):
    infile="vol.txt"
    read=open(infile,"r")
    top=Element("splitter",fname=fname)
    counter=0
    for i in read:
        counter+=1
        line=i.split(":")
        num=int(line[0])
        if num % 2 == 1:
            chunk=SubElement(top,"chunk",val=str(counter))
        if num % 2 == 1:
            if line[1] == "silence_end":
                chunkS=SubElement(chunk,"end")
                chunkS.text=line[2].rstrip("\n")
        if num % 2 == 0:
            if line[1] == "silence_start":
                chunkE=SubElement(chunk,"start")
                chunkE.text=line[2].rstrip("\n")
    return tostring(top).decode()

def writeXml(xml,xmlfile):
    file=open(xmlfile,"wb")
    file.write(xml)
    file.close()

def parseXml():
    songDir="songs"
    songDir=os.path.realpath(os.path.expanduser(songDir))
    if not os.path.exists(songDir):
        os.mkdir(songDir)
    if os.path.exists(songDir):
        fname=sys.argv[1]
        xmlfile="vol.xml"
        xml=genXml(fname=fname)
        writeXml(xml.encode(),xmlfile)
    
        end=0
        start=0
    
        tree=ET.parse(xmlfile)
        root=tree.getroot()
        for chunk in root:
            print(chunk.tag,chunk.attrib)
            for children in chunk:
                if children.tag == "end":
                    end=float(children.text)-0.50
                    #print(end,"end")
                if children.tag == "start":
                    start=(float(children.text)-end)+0.50
                    #print(start,"start")
            fnameSplit=os.path.splitext(fname)
            ext=fnameSplit[1]
            oname=chunk.attrib['val']+ext
            cmd="printf '%s\n' y | ffmpeg -ss {} -t {} -i {} {}".format(end,start,fname,os.path.join(songDir,oname))
            proc=sp.Popen(cmd,shell=True,stdout=sp.PIPE)
            stdout,err=proc.communicate()
            print(stdout)
    else:
        exit("songdir does not exist: {}".format(songDir))




parseXml()

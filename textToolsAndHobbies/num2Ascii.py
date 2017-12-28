#! /usr/bin/python3

nl="\n"

def test(lo,hi):
 acc=""
 endCap="#ENDCAP#"
 for i in range(lo,hi+1):
  acc=acc+chr(i)
 print(endCap,acc,endCap,sep="")
 return acc

def specialCharFmt():
    oDict=dict()
    special="~!@#$%^&*()_+`-={}|[]\\;':\",./<>? "
    for i in special:
     oText=i.rstrip(nl)
     oList=[ord(oText),oText]
     oString="_"+"S"+str(oList[0])
     oDict[oString]=oList
    for i in oDict.keys():
     print(i,oDict[i])
     
specialCharFmt()

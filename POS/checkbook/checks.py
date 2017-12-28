#! /usr/bin/python3
import time, re
#check to ensure values are what they should be
ft=float()
st=str()
it=int()

def floatCheck(value):
    if type(value) == type(ft):
        return [True,value,{"shouldBe":type(ft)}]
    else:
        if type(value) == type(it):
            return [True,float(value),{"shouldBe":type(ft)}]
        else:
         return [False,type(value),{"shouldBe":type(ft)}]

def stringCheck(value):
    if type(value) == type(st):
        return [True,value,{"shouldBe":type(st)}]
    else:
        return [False,type(value),{"shouldBe":type(st)}]

def entryDate():
    Date=time.ctime()
    if type(Date) == type(st):
        return [True,Date,{"shouldBe":type(st)}]
    else:
        return [False,type(value),{"shouldBe":type(st)}]

   
def date(value):
    dot="."
    dash="-"
    returnData=False
    acc=str()
    if type(value) == type(str()):
        returnData=re.split(r',|\s|\.|-',value)
        if len(returnData) < 3:
            returnData=[False,"too_short"]
        elif len(returnData) > 3:
            returnData=[False,"too_long"]
        else:
            for j,i in enumerate(returnData):
                if j < 2:
                    acc=acc+i+"-"
                else:
                    acc=acc+i
            returnData=[True,acc,{"shouldBe":type(st)}]
    else:
        returnData=[False,"inval_not_string",{"shouldBe":type(st)}]
    return returnData


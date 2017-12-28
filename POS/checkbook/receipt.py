#! /usr/bin/python3

import sys,argparse,os,hashlib, time, pymysql, random

#local import
import checks

#fields
#subtotal tax totalsale date entrydate store user
#need to add sql server entry duplicates check

nl="\n"
hostname=""
uzer=""
database=""
password=""
table=""

CFG="./checkbook.cfg"
if os.path.exists(CFG) and os.path.isfile(CFG):
 with open(CFG,"r") as cfg:
  for i in cfg:
   if len(i.split("=")) > 1:
    varName=i.split("=")[0]
    varVal=i.split("=")[1]
    if varName == "hostname":
     hostname=varVal.rstrip(nl)
    if varName == "uzer":
     uzer=varVal.rstrip(nl)
    if varName == "database":
     database=varVal.rstrip(nl)
    if varName == "password":
     password=varVal.rstrip(nl)
    if varName == "table":
     table=varVal.rstrip(nl)
else:
    print("configuration file does not exist! quitting!")
    exit()


def checkRun(subtotal,tax,totalsale,date,store,user,notes):
    acc=""
    entrydate_l=time.localtime()
    for i in entrydate_l:
        acc=acc+str(i)
    entrydate=time.ctime()+str(random.randint(0,int(acc)))
    Floats={"subtotal":subtotal,"tax":tax,"totalsale":totalsale}
    Strings={"store":store,"date":date,"user":user,'notes':notes}
    dataF=dict()
    results=dict()
    dataFString=str()
    for i in Floats.keys():
        test=checks.floatCheck(Floats[i])
        if test[0] == False:
            results[i]=test
    for i in Strings.keys():
        test=checks.stringCheck(Strings[i])
        if test[0] == False:
            results[i]=test
    ## check for errors, if any display them, else display and return data
    for i in results.keys():
        if results[i][0] == False:
            print(results)
            return results
    else:
        for j in Floats.keys():
            dataF[j]=Floats[j]
        for j in Strings.keys():
            dataF[j]=Strings[j]
        dataF["entrydate"]=entrydate
        for j in dataF.keys():
            dataFString=dataFString+" "+j+":"+"'"+str(dataF[j])+"'"
        print(dataFString)
        dbEntry(str(dataF['subtotal']),str(dataF['tax']),str(dataF['totalsale']),dataF['date'],dataF['entrydate'],dataF['store'],dataF['user'],dataF['notes'])
        return dataF

def dbEntry(subtotal,tax,totalsale,date,entrydate,store,user,notes):
    db = pymysql.connect(hostname,uzer,password,database)
    sql="INSERT INTO "+table+" (SUBTOTAL, TAX, TOTALSALE, DATE, ENTRYDATE, STORE,USER,NOTES) VALUES ("+"'"+subtotal+"','"+tax+"','"+totalsale+"','"+date+"','"+entrydate+"','"+store+"','"+user+"','"+notes+"')"
    print(sql)
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


#add cmd args
def cmdline():
    parser=argparse.ArgumentParser()
    parser.add_argument("-s","--subtotal",help="add subtotal entry",required="yes")
    parser.add_argument("-t","--tax",help="add tax entry",required="yes")
    parser.add_argument("-S","--totalsale",help="add totalsale entry",required="yes")
    parser.add_argument("-d","--date",help="date on receipt",required="yes")
    parser.add_argument("-e","--store",help="where the expense was spent at",required="yes")
    parser.add_argument("-u","--user",help="who spent the money",required="yes")
    parser.add_argument("-n","--notes",help="receipt notes",required="yes")
    options=parser.parse_args()
    checkRun(float(options.subtotal),float(options.tax),float(options.totalsale),options.date,options.store,options.user,options.notes)
#add sql client support
##insertion support added
##need read support

# add pygtk gui
#checkRun(111,12.0,1111.0,"1","carls","cal") 
#cmdline()

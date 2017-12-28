import pymysql,os

nl="\n"
hostname=""
database=""
uzer=""
password=""

CFG="./pinbreak.cfg"
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
    if varName == "password":
     password=varVal.rstrip(nl)
    if varName == "database":
     database=varVal.rstrip(nl)
else:
    print("configuration file does not exist! quitting!")
    exit()



def getVersion(hostname,user,password,database):
 #open database connection
 db = pymysql.connect(hostname,user,password,database)
 ##prepare a cursor object  using cursor() method
 cursor = db.cursor()
 # execute sql query using execute() method
 cursor.execute("SELECT VERSION()") 
 #fetch single row using fetchone() method
 data = cursor.fetchone()
 print("Database Version : %s" % data)
 #disconnect from server
 db.close()


getVersion(hostname,uzer,password,database)

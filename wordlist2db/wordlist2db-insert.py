#! /usr/bin/python3

import pymysql,sys, binascii, os, time, signal

try:
    import readconf
    conf=readconf.confread()
    address=conf[0]
    user=conf[1]
    password=conf[2]
    database=conf[3]
    
except:
    address="127.0.0.1"
    user="test"
    password="avalon"
    database="wordlist"

if os.path.exists("KILL"):
    sys.exit("KILL-FILE found! for processing of "+sys.argv[1])


db = pymysql.connect("127.0.0.1","test","avalon","wordlist")
cursor=db.cursor()

#keep record of data wordlist worked on
completed="completed/"
if not os.path.exists(completed):
    os.mkdir(completed)

done=open(completed+os.path.basename(sys.argv[1]),"a")
done.write("<S========================================S>\n")
done.write(sys.argv[1]+" <+> "+time.ctime()+"[START]\n")

linecount=0
with open(sys.argv[1],"rb") as file:
    for i in file:
        linecount+=1

sql="create table if not exists tracking ( list longtext, date longtext );"
cursor.execute(sql)

sql="select list from tracking where list='"+sys.argv[1]+"';"
cursor.execute(sql)
if cursor.fetchone() != None:
    print(time.ctime(),"=>",sys.argv[1])
    sys.exit("table already done!")

def sign_handler(signal, frame):
    print("ctrl-c was issued")
    done.write(sys.argv[1]+" <+> "+time.ctime()+"[END]\n")
    done.write("Ctrl-C was issued: table creation most likely incomplete\n")
    done.write("<E========================================E>\n")
    done.close()
    kill=open("KILL","w")
    kill.write("")
    kill.close()
    sys.exit("ctrl-c was issued!")


signal.signal(signal.SIGINT,sign_handler)

#create table base off of filename [Dynamic]
#table=os.path.basename(sys.argv[1].replace(".","_")).replace(" ","").replace("-","_")
#static table name
table="wordlist"

print("table name: "+table)
sql="create table if not exists "+table+" ( word longtext, ID int(20) );"
cursor.execute(sql)
count=0
acc=''

try:
    sql="select ID from wordlist order by ID desc limit 1;"
    cursor.execute(sql)
    ID=cursor.fetchone()[0]+1
    print(ID,"noif")
    if ID == None:
        ID=0
        print(ID,"tryif_due_NONE")
except:
    ID=0
    print(ID,"except")

with open(sys.argv[1],"rb") as addfile:
    for i in addfile:
        word=binascii.hexlify(i).decode()
        count+=1
        '''
        if ( count % 1000 ) == 0 and ( count == 0 ):
            sql="BEGIN;"
            cursor.execute(sql)
        else:
            sql="END;"
            cursor.execute(sql)
            sql="BEGIN;"
            cursor.execute(sql)
        '''
        try:
            sql="INSERT INTO "+table+"(WORD,ID) select '"+word+"',"+str(ID)+" where not exists(select word from "+table+" where word='"+word+"');"
            cursor.execute(sql)
            if cursor.rowcount != 0:
                print(ID,word.rstrip("\n"),"[added]")
                ID+=1
            else:
                if ( count % 100 ) == 0:
                    print(acc,"...",word.rstrip("\n"),"[already present]")
            if ( count % 100 ) == 0:        
                acc=word.rstrip("\n")

            db.commit()
            if count == linecount:
                sql="insert into tracking (list,date) select '"+sys.argv[1]+"','"+time.ctime()+"' where not exists(select list from tracking where list='"+sys.argv[1]+"');"
                cursor.execute(sql)
                db.commit()
        except:
            db.rollback()

db.close()
#write the table completed end time
done.write(sys.argv[1]+" <+> "+time.ctime()+"[END]\n")
done.write("<E========================================E>\n")
done.close()

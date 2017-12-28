#! /usr/bin/python3
import os,hashlib, pymysql, time

import subprocess
import statusgen

db=pymysql.connect("127.0.0.1","carl","avalon","clips")
cursor=db.cursor()

statusgen.gen("running")

sql="create table if not exists clipart ( urlThumbNail text, urlVector text, keyword text, clipID varchar(34), PRIMARY KEY (clipID));"
cursor.execute(sql)

counter=0
for i,j,k in os.walk("resources"):
    for subK in k:
        counter+=1
        url=os.path.join(i,subK)
        keyword=url.replace("/"," ").replace("_"," ").replace("."," ")
        fileID=hashlib.md5()
        file=open(url,"rb")
        print("md5sum - start")
        while True:
            data=file.read(128)
            if not data:
                break
            fileID.update(data)
        ID=fileID.hexdigest()
        print("m5sum - end")
        ext=os.path.splitext(url)
        urlThumbNail=url
        if ext[1] == ".tif" or ext[1] == ".wmf":
            path=url
            print("convert prep - start")
            """cmd="convert \""+path+"\" \""+ext[0]+".png\""
            doit=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            output,err = doit.communicate()
            print("convert info\n",output,err)"""
            urlThumbNail=ext[0]+".png"
            print("convert prep - end")
        else:
            urlThumbNail=url
        urlVector=url
        print("insert - start")
        try:
            #print(urlThumbNail,urlVector,keyword,ID)
            #sql="insert into clipart (urlThumbNail,urlVector,keyword,clipId) values (\""+urlThumbNail+"\",\""+urlVector+"\",\""+keyword+"\",\""+ID+"\");"
            #sql="insert into clipart (urlThumbNail,urlVector,keyword,clipId) select \""+urlThumbNail+"\",\""+urlVector+"\",\""+keyword+"\",\""+ID+"\" where not exists(select urlThumbNail,urlVector,keyword,clipId from clipart where urlThumbNail='"+urlThumbNail+"',urlVector='"+urlVector+"',keyword='"+keyword+"',clipID='"+ID+"');"
            sql="insert into clipart (urlThumbNail,urlVector,keyword,clipId) select \""+urlThumbNail+"\",\""+urlVector+"\",\""+keyword+"\",\""+ID+"\" where not exists(select urlThumbNail,urlVector,keyword,clipId from clipart where clipID='"+ID+"');"

            cursor.execute(sql)
            if cursor.rowcount != 0:
                print(urlThumbNail,urlVector)
                if ext[1] == ".tif" or ext[1] == ".wmf":               
                    print("convert - start")
                    cmd="convert \""+path+"\" \""+ext[0]+".png\""
                    doit=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
                    output,err = doit.communicate()
                    print("convert info\n",output,err)
                    print(err)
            else:
                print(url,"[not added]")
            
        except OSError as err:
            print(err)
            db.rollback()
        #print(urlThumbNail,urlVector,keyword,ID)
        if ( counter % 10000 ) == 0:
            db.commit()
        print("insert - end")
db.commit()
db.close()
statusgen.gen("done")

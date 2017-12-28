#! /usr/bin/env python3

import sqlite3,os,random
import time, subprocess, sys, argparse

def musicDir():
 rplaycnf="rpn.cnf"
 music_dir=''
 if os.path.exists(rplaycnf):
  with open(rplaycnf,"r") as cfg:
   for i in cfg:
    if i.split("=")[0] == "music_dir":
     music_dir=i.split('=')[1]
 else:
  music_dir="~/Music"
 return music_dir.rstrip("\n")

def playit(playlist='',nodisp="",music_db=''):
    db=sqlite3.connect(music_db)
    cursor=db.cursor()
    sql="select path from "+playlist+" order by id asc;"
    cursor.execute(sql)
    play=cursor.fetchall()
    for i in play:
        print(i) #need to print song
        cmd=subprocess.Popen('mpv --vid=no '+nodisp+' "'+i[0]+'"',shell=True,stdout=subprocess.PIPE)
        res,err=cmd.communicate()
        print(res.decode(),err)
    db.close()

def db_gen(verbose=False,music_db=''):
 music_dir=musicDir()
 print("scanning "+music_dir+" - generating db")
 db=sqlite3.connect(music_db)
 cursor=db.cursor()
 
 sql="create table if not exists music (path text, id real);"
 cursor.execute(sql)
 
 exclude_ext=[]
 ignorefile="ignore.cnf"
 if os.path.exists(ignorefile):
  with open("ignore.cnf","r") as config:
      for i in config:
          exclude_ext.append(i.rstrip("\n"))
 else:
  exit("missing "+ignorefile)
 sql="select id from music order by id desc limit 1;"
 cursor.execute(sql)
 if cursor.rowcount != 0:
  counter=1
 else:
  counter=cursor.fetchone()[0]

 for root,dirs,fnames in os.walk(music_dir,topdown=True):
  for fname in fnames:
   if os.path.splitext(fname)[1].replace(".","") in exclude_ext:
    path=os.path.join(root,fname)
    sql='insert into music select "'+path+'",'+str(counter)+' where not exists(select path from music where path="'+path+'");'
    cursor.execute(sql)
    if cursor.rowcount != 0:
     counter+=1
    else:
     if verbose== True:
      print("added")
    if verbose == True:
     print(path,counter)
    if (( counter % 500 ) == 0):
     db.commit()
 db.commit()
 db.close()

def datecode():
 acc=str()
 for num, val in enumerate(time.localtime()):
  if num < 7:
   acc+=str(val)
 return acc

def loggen(playString='',music_db=''):
 print("[start] creating log")
 log=open("playlist.log","w")
 dblog=sqlite3.connect(music_db)
 dbcursor=dblog.cursor()
 sql="select path from "+playString+";"
 dbcursor.execute(sql)
 if dbcursor.rowcount != 0:
     listed=dbcursor.fetchall()
     for i in listed:
         log.write(i[0]+"\n")
 print("[end] creating log")

def randgen(music_db=''):
 namecode=datecode()
 print('generating playlist: playlist'+namecode)
 db=sqlite3.connect(music_db)
 cursor=db.cursor()
 sql="select id from music order by id desc limit 1;"
 cursor.execute(sql)
 if cursor.rowcount == 0:
  exit("no music id's")
 else:
  counter_0=cursor.fetchone()
  if counter_0 != None:
   counter=counter_0[0]
  else:
   counter=0
 for i in range(1,int(counter)+1):
  randSong=random.randint(1,int(counter)+1)
  sql = "create table if not exists playlist"+namecode+"(path text,id real);"
  cursor.execute(sql)
  db.commit()
  sql='select path from music where id="'+str(int(randSong))+'"'
  cursor.execute(sql)
  song_0=cursor.fetchone()
  if song_0 != None:
   song=song_0[0]
  else:
   while song == None:
    cursor.execute(sql)
    song_0=cursor.fetchone()
    if song_0 != None:
     song=song_0[0]
  sql="select path from playlist"+namecode+' where path="'+song+'";'
  cursor.execute(sql)
  state=cursor.fetchone()
  if state == None:
   sql='insert into playlist'+namecode+'(path,id) values("'+song+'",'+str(int(i))+');'
   cursor.execute(sql)
   db.commit()
   # need to create aloop until a new song number is selected
  else:
   Fail=True
   while Fail == True:
    randSong=random.randint(1,int(counter)+1)
    sql='select path from music where id="'+str(int(randSong))+'"'
    cursor.execute(sql)
    if cursor.rowcount != 0:
     song_1=cursor.fetchone()
     if song_1 != None:
      song=song_1[0]
      sql="select path from playlist"+namecode+' where path="'+song+'";'
      cursor.execute(sql)
      state=cursor.fetchone()
      if state == None:
       sql='insert into playlist'+namecode+'(path,id) values("'+song+'",'+str(int(i))+');'
       cursor.execute(sql)
       db.commit()
       Fail=False
  if (( i % 100 ) == 0 ):
   db.commit()
 db.commit()
 db.close()
 loggen("playlist"+namecode,music_db)
 return "playlist"+namecode

def findExt(music_db=''):
    music_dir=musicDir()
    db=sqlite3.connect(music_db)
    cursor=db.cursor()
    sql="create table if not exists ext(id real, extension text);"
    cursor.execute(sql)
    sql="select id from ext order by id limit 1;"
    cursor.execute(sql)
    count=cursor.fetchone()
    if count == None:
        counter=0
    else:
        counter=count[0]
    music_dir_content=len(os.listdir(music_dir))
    if music_dir_content == 0:
        exit("no music found")
    for root,dirs,fnames in os.walk(music_dir,topdown=True):
        for fname in fnames:
            ext=os.path.splitext(fname)[1].replace(".","")
            sql="select extension from ext where extension='"+ext+"';"
            cursor.execute(sql)
            fetch=cursor.fetchone()
            if fetch == None:
             sql="insert into ext (id,extension) values("+str(counter)+",'"+ext+"');"
             cursor.execute(sql)
             db.commit()
             if cursor.rowcount != 0:
                 counter+=1
    db.commit()
    sql="select extension from ext order by id;"
    cursor.execute(sql)
    extent=cursor.fetchall()
    print("extensions in your music directory:")
    for i in extent:
        print("\t"+i[0])
    db.commit()
    db.close()


def checktable(playList='',music_db=''):
    sql='select name from sqlite_master where type="table" and name="'+playList+'"'
    db=sqlite3.connect(music_db)
    cursor=db.cursor()
    cursor.execute(sql)
    playlist=cursor.fetchone()
    if playlist == None:
        print("no playlist by that name: {}".format(playList))
        sql='select name from sqlite_master where type="table" and name like "playlist%";'
        cursor.execute(sql)
        playlists=cursor.fetchall()
        print("available playlists are: ")
        for playlist in playlists:
            print("\t{}".format(playlist[0]))
        exit(1)
    else:
        print(playlist)
        return playlist

def main():
    music="music.db"
    findExt(music)
    
    #exit("test zone exit")
    
    db_gen(verbose=False,music_db=music)
    
    parser=argparse.ArgumentParser()
    parser.add_argument("-m","--mpv-options")
    parser.add_argument("-p","--play-list")
    options=parser.parse_args()
    
    if options.play_list:
        playString=options.play_list
        checktable(playString,music_db=music)
    else:
        playString=randgen(music_db=music)
    
    
    #def loggen(playString=''):
    # print("[start] creating log")
    # log=open("playlist.log","w")
    # dblog=sqlite3.connect("music.db")
    # dbcursor=dblog.cursor()
    # sql="select path from "+playString+";"
    # dbcursor.execute(sql)
    # if dbcursor.rowcount != 0:
    #     listed=dbcursor.fetchfall()
    #     for i in listed:
    #         log.write(i[0]+"\n")
    ## print("[end] creating log")
    if options.mpv_options:
        playit(playString,options.mpv_options,music_db=music)
    else:
        playit(playString,music_db=music)

main()

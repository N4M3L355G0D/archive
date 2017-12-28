#! /usr/bin/env python3

import os, random

#need to install python-pydub
try:
 from pydub import AudioSegment
 from pydub.playback import play
except:
 print("pydub is not available on this platform at this time!")

import subprocess as sp

class player():
 nodisp=False
 file="./playlist.tmp.txt"
#directory where music is/'will be stored'
 dirpath=os.path.expanduser("~")+"/Music"
 #you might find files in your music dir that are not music, use this list to blacklist them
 non_music_ext=[".aup",".gz",".zip",".tar",".xz",".au",".txt",".jpg",".nfo",".png",".pdf",".part",".VOB",".NFO",".log",".cue",".torrent",".ini",".jpeg",".sfv"]
 count=0
 fileList=list()
 playList=list()
 noplay=False
 system=True
 def init(self):
  #if directory does not exist, exit early with message
  if not os.path.exists(self.dirpath):
   print("Directory does not exist! Please provide a valid dirpath= as dirpath=%s, preferebly in ~/Music" % self.dirpath)
   return [False,"path does not exist!"]
  elif os.path.exists(self.dirpath):
   return [True,"path exists!"]

 def deckgen(self):
  counter=0
  print("Generating Music Deck")
  #generate file system list
  #walk the filesystem
  #append files to list
  for i,j,k in os.walk(self.dirpath):
   for x in k:
    path=os.path.join(i,x)
    #print(path)
    #if ext is in blacklist do not include in playlist stage1
    if os.path.splitext(path)[1] not in self.non_music_ext:
        #print(path)
        self.fileList.append(path)
        self.count+=1
    #check to see if dir is empty
  if len(self.fileList) == 0:
   #if dir is empty, len == 0,
   #exit early
   print("Directory is Empty")
   exit()
   #begin randomizing the resulting playlist
  fileList_len=len(self.fileList)-1
  if fileList_len > 1:
   while counter != fileList_len:
    file=random.randint(0,fileList_len)
    if self.fileList[file] not in self.playList:
     #mod here
     print(self.fileList[file])
     #not necessary, but here to kill anyy stragglers, remove non-music files
     #and audcity projects
     if os.path.splitext(self.fileList[file])[1] not in self.non_music_ext:
      self.playList.append(self.fileList[file])
      counter+=1
  else:
   self.playList.append(self.fileList[0])
 def play(self):
  songnum=0
  #for variable conditions
  #create the length of fileList        
  print("Playing Random Music Deck")
  for i in self.playList:
   #check if file actually exists, though unnecessary due to list generation
   if os.path.exists(i):
   #place the player function here
   #before playing, check file extension,
   #print(i)
    if os.path.splitext(i)[1] not in self.non_music_ext:
     #print filename
     #print(i)
     #player function
     #for now i will use an ugly os.system call
     # scratch that some side effects when using os.system, such as not being able to kill player without killing bash, ffplay $file does not see eof
     #realized that i was missing -autoexit from ffplay command
     try:
      if self.noplay == False:
       print("[PID: "+str(os.getpid())+"]-[ Playing: "+i+" ]-[ Song_Number: "+str(songnum)+" ]-[ Out_of: "+str(len(self.playList))+" ]"+" kill with `bash randkill.sh $PID`")
       if self.system == False:
        song=AudioSegment.from_file(i)
        play(song)
       else:
        if self.nodisp == False:
         cmd="bash ffplay.sh "+"'"+str(i)+"'"
        if self.nodisp == True:
         cmd="bash ffplay.sh nd "+"'"+str(i)+"'"
        os.system(cmd)
        #remove played file from fileList, as I do not want to hear the same song twice in a random play
      else:
       print("song_num : "+str(songnum)+" | basename : "+str(os.path.basename(i))+" | path : "+i)
       #print("Song_Number: "+str(songnum)+" | Song_path: "+str(i)+" | Total_songs: "+str(len(self.playlist)))
     except:
      print("could not play song")
     songnum+=1
  
 def playlist_dump(self,delete=False,preserve=False):
  import hashlib
  playlistHash=hashlib.sha512()
  playlistTmp=str()
  for i in self.playList:
      playlistTmp+=i+"\n"
      #print(i)
  playlistHash.update(playlistTmp.encode())
  #print(playlistHash.hexdigest())
  if delete == False:
   if os.path.exists(self.file):
    if preserve == False:
     #if file exists, delete it
     os.remove(self.file)
     file=open(self.file,"w")
    elif preserve == True:
     file=open(self.file,"a")
   else:
    file=open(self.file,"w")
   for i in self.playList:
    oData=i+" <#> "+playlistHash.hexdigest()+"\n"
    file.write(oData)
   file.close()
  if delete == True:
   if os.path.exists(self.file):
    os.remove(self.file)

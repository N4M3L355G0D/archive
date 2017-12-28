#! /usr/bin/python3


import randplay
import argparse, time

parser=argparse.ArgumentParser()
parser.add_argument("-d,","--dir",help="music directory")
parser.add_argument("-l","--list",help="list songs in random order",action="store_true")
parser.add_argument("-s","--system",help="use os.system",action="store_true")
parser.add_argument("-p","--pydub",help="use pydub",action="store_true")
parser.add_argument("-n","--nodisp",help="use with os.system on system that does not use xorg server",action="store_true")
parser.add_argument("-i","--play-inf",help="after new playlist completes, create new playlist and play again, infinitely",action="store_true")
parser.add_argument("-b","--blacklist-extensions",help="comma delimited extension blacklist")
parser.add_argument("-L","--list-song-order",help="list the current playlist order",action="store_true")
parser.add_argument("-P","--preserve-list",help="preserve played playlists",action="store_true")
options=parser.parse_args()

def main(opts=[]):
    player=randplay.player()
    if options.blacklist_extensions:
     exts=options.blacklist_extensions.split(",")
     for i in exts:
      player.non_music_ext.append(i)
    if options.dir:
     player.dirpath=options.dir
    else:
     #use default defined in randplay.py
     pass
    exist=player.init()[0]
    if exist == True:
        player.deckgen()
        #create playlist listing file
        if options.list_song_order == True:
         if options.preserve_list == False:
          player.playlist_dump(delete=False,preserve=False)
         elif options.preserve_list == True:
          player.playlist_dump(delete=False,preserve=True)
        #set to False to use pydub, set to true to use os.system+ffplay
        #setting True allows for arrow control of the songs, to skip, but not go backwards
        if options.system:
         player.system=True
         if options.nodisp:
          player.nodisp=True
        if options.pydub:
         player.system=False
        else:
         player.system=True
        #set to True to just dump a song list
        if options.list:
         player.noplay=True
        else:
         player.noplay=False
        player.play()
        #delete playlist file
        #if options.list_song_order == True:
         #player.playlist_dump(delete=True)
#determine if player should repeat
def repeat():
    while options.play_inf == True:
        print("inf play")
        time.sleep(2)
        main()
    else:
        print("play list once")
        time.sleep(2)
        main()
repeat()

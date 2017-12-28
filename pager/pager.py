#! /usr/bin/python3
# a curses pager like less, with less features, just a pager
# no gui linux


from curses import wrapper
import curses
from time import ctime
import os,sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-f",help="file input")
parser.add_argument("-p",help="pipe input",action="store_true")
options=parser.parse_args()

def resize(stdscr,lines,cols):
    resize = curses.is_term_resized(lines+1,cols+1)
    if resize == True:
        lines,cols = stdscr.getmaxyx()
        lines=lines-1
        cols=cols-1
        stdscr.clear()
        curses.resizeterm(lines,cols)
        stdscr.refresh()

def pager(stdscr):
    key=0
    curses.halfdelay(5)
    stdscr.clear()
    stdscr.refresh()
    lines=curses.LINES-1
    cols=curses.COLS-1
    topline=0
    intacc=0
    file=sys.argv
    longline=0
    colsMove=0
    stdinacc=''
    if options.p:
     for i in sys.stdin:
      stdinacc+=i
    #using sys.stdin interferes with curses input functions
    #so to work around this problem, this will reopen the terminal
    #since there is no more input through the stdin
    #for reference see the following url
    #https://stackoverflow.com/questions/3999114/linux-pipe-into-python-ncurses-script-stdin-and-termios
    f=open("/dev/tty")
    os.dup2(f.fileno(),0)
    if options.f or options.p:
     if options.f:
      file=options.f
     elif options.p:
      file='-'
     if options.p or options.f:
         if options.f:
          infile=open(file,"r")
         else:
          infile=stdinacc.split("\n")
         keystr=[]
         for i in infile:
             keystr.append(i)
         # determine the longest line in keystr
         for i in keystr:
             if len(i) > longline:
                 longline=len(i)
         # make each line the same length
         for num,i in enumerate(keystr):
             if len(i) < longline:
                 tmp=""
                 iterations=longline-len(i)
                 for i in range(0,iterations):
                     tmp+=" "
                 keystr[num]+=tmp
         #due to a bug where the longest line would be displayed from stdinput, and paging right, would result in seeing duplicate characters as the
         #last character of the line, like the example below
         #if this was the last lineeeeeee
         #add a space to the end of the already processed lines
         for num,i in enumerate(keystr):
             keystr[num]+=" "
         #press the 'q' key to quit the pager
         # still have an issue where ptty size change causes curses to exit with an exception 
         while key != ord('q'):
          if intacc != len(keystr)-1:   
           if key == curses.KEY_DOWN:
               if topline <= len(keystr)-1:
                topline+=1
          if key == curses.KEY_UP:
           if topline > 0:
              topline-=1
          if key == curses.KEY_LEFT:
            if colsMove > 0:
             colsMove-=1
          if ((cols-5)+colsMove) != longline:
            if key == curses.KEY_RIGHT:
             colsMove+=1
          # key detection for left and right to view document left and right
          # if keystr[line] shorter than longest line in document, add spaces to line until equal len of longest line
          # if left key is pressed, move document by slicing left
          # if right key is pressed, move document by slicing right
          # in the event that the terminal is resized, get the right dimensions
          resize = curses.is_term_resized(lines+1,cols+1)
          if resize == True:
               lines,cols = stdscr.getmaxyx()
               lines=lines
               cols=cols
               stdscr.clear()
               curses.resizeterm(lines,cols)
               stdscr.refresh()
               cols=cols-1
               lines=lines-1
               colsMove=0
          for i in range(0,lines): 
              intacc=i+topline
              # in the event of terminal resize, the code will drop to an except so that a terminal redraw can be performed
              try:
               if intacc <= len(keystr)-1:
                stdscr.addstr(i,0,keystr[i+topline][colsMove:int(cols-5)+colsMove])
               #stdscr.addstr(i,0,str(topline)+":"+str(key))
              except:
               break
          #stdscr.addstr(0,0,str(lines))
          stdscr.addstr(lines,0,file,curses.A_BOLD)
          stdscr.refresh()
          key=stdscr.getch()
    else:
     return "please see -h/--help"
err=wrapper(pager)
if err != None:
 print(err)

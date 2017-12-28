#! /usr/bin/python3

from curses import wrapper
import curses
from time import ctime
def writefile(stringList=[]):
    file="tmp.txt"
    ofile=open(file,"w")
    for i in stringList:
        ofile.write(i+"\n")
    ofile.close()

def main(stdscr):
    key=0
    keystr=['',]
    #makes getch() time out after 5/10 of a second and continue the loop
    curses.halfdelay(5)
    #32 is the ascii code for the space bar
    #27 is the ascii code for the escape key; 27 is the exit code
    line=0
    while key != 27:
     #make sure key does have an undesired value
     if key != -1:
      if key != '':
       #if key is enter '10' add a line by incrementing line and appending an empty string to keystr list
       # if the len of the list keystr is greater than curses.LINE-10, or terminal height, ignore text input, except for backspace, and the escape key
       if len(keystr) < curses.LINES-10:
        if key == 10:
         line+=1
         keystr.append('')
        #if key falls within visual keycodes add them to the current line
        elif 32 <= int(key) <= 126:
         keystr[line]+=chr(key)
        #if the backspace key is used, remove 1 character from the current line
       if int(key) == 127:
        #if the current line is empty, then decrement line and pop last line from keystr list, but only if the first line is not empty
        if len(keystr[line]) == 0:
            if (len(keystr[0]) != 0) and (len(keystr) > 1):
             keystr.pop(line)
             line-=1
            elif ( keystr[line] == '' ) and ( line != 0 ):
             keystr.pop(line)
             line-=1
        # if the first line is not empty allow the backspace, otherwise ignore the back space
        if len(keystr[0]) != 0:
         keystr[line]=keystr[line][:len(keystr[line])-1]
     #clear the screen
     stdscr.clear()
     #get max screen dimensions
     win=[curses.LINES-1,curses.COLS-1]
     winStr=("lines: ","columns: ")
     count=0
     for num,i in enumerate(win):
         #uses the form addstr(y,x,string,attribute)
         stdscr.addstr(0+count,0,winStr[num]+str(i)+"\n",curses.A_BOLD)
         count+=1
     stdscr.addstr(0+count,0,"Date: {}".format(ctime()+"\n"),curses.A_UNDERLINE)
     count+=1
     stdscr.addstr(0+count,0,"keycode pressed: {}".format(str(key)),curses.A_BLINK)
     count+=1
     stdscr.addstr(0+count,0,"Warning: SPACEBAR == '32'; pressing SPACEBAR will exit this program",curses.A_BOLD)
     count+=1
     #read through keystr to print lines to the screen
     for num,i in enumerate(keystr):
      stdscr.addstr(0+count+num,0,i)
     #refresh the screen for drawing
     stdscr.refresh()
     #get the keyboard input
     key=stdscr.getch()
    return keystr

#wrapper returns the terminal to normal if an exception is raised
data=wrapper(main)
writefile(data)

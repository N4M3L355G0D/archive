#! /usr/bin/env python3

import string

comet='''
     -
    >.
-  >.
. >.|#
. ..|I#Am#Osiris#Kohmet,
<. .|The#Silent#Traveller,
<. .|Crossing#the#Deep#Void,
 <..|Observer,#Prophet,#and#Scroll#Keeper,
  <.|I#Am#Here,#and#Then#I#am#There,
   .|Observed,#Yet#Untouched,
   .|Seeking#rest#in#a#Land#without#Fire,
   .|That#I#Once#Again#May#Be#Reborn,
   -
'''
exp=5
class color:
    yellow='\033[1;33;40m'
    green='\033[1;32;40m'
    red='\033[1;31;40m'
    end='\033[0;m'
    blue='\033[1;34;40m'
    purple='\033[1;35;40m'
colors=color()

class display:
    master=None
    def display(self):
        for i in comet:
            if i in [' ','.','>','<','-']:
                if i == '>':
                    print(i.replace('>',colors.blue+'='+colors.end)*exp,end='')
                elif i == '<':
                    print(i.replace('<',colors.purple+'\\'+colors.end)*exp,end='')
                elif i == '-':
                    print(i.replace('-',colors.green+'-'+colors.end)*exp,end='')
                else:
                    print(i.replace('.',colors.yellow+'*'+colors.end)*exp,end='')
            else:
                if i == '#':
                    print(i.replace('#',' '),end='')
                elif i == '|':
                    print(i.replace('|',colors.green+'|'+colors.end),end='')
                else:
                    print('{}{}{}'.format(colors.red,i,colors.end),end='')
a=display()
a.display()

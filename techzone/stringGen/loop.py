#! /usr/bin/python3


import string, itertools

chars_complete=string.printable

char_space=63
counter=1
space_lvl=1

while space_lvl <= char_space:
 for i in itertools.product(chars_complete.replace('\n','').replace('\t','').replace('\r','').replace('\v','').replace('\f',''),repeat=space_lvl): 
     print("count |:| ",counter," |:|" ,'"'+str(''.join(i))+'"')
     counter=counter+1
 space_lvl=space_lvl+1


## chars printed
a=chars_complete.replace('\n','').replace('\t','').replace('\r','').replace('\v','').replace('\f','')

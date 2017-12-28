#! /usr/bin/python3


import string, itertools, time, signal,sys

#emergency only
chars_complete=string.printable
stripped=chars_complete.replace('\n','').replace('\t','').replace('\r','').replace('\v','').replace('\f','')


#primary char list
stripped="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;\"'<>,.?/ "
char_space=63
counter=1
space_lvl=1

start_time=(str(time.localtime().tm_hour),":",str(time.localtime().tm_min),":",str(time.localtime().tm_sec),"@",str(time.localtime().tm_mday),"\\",str(time.localtime().tm_mon),"\\",str(time.localtime().tm_year))

ofile=open("lock-start","w")
ofile.write(''.join(start_time)+'\n')
ofile.close()

def ender(signal, frame):
    print('\n',''.join(start_time))
    sys.exit(0)
signal.signal(signal.SIGINT,ender)

while space_lvl <= char_space:
 for i in itertools.product(stripped,repeat=space_lvl): 

## print the data
  data=("count |:| ",str(counter)," |:| " ,'"'+str(''.join(i))+'"'," |:| ",''.join((str(time.localtime().tm_hour),":",str(time.localtime().tm_min),":",str(time.localtime().tm_sec),"@",str(time.localtime().tm_mday),"\\",str(time.localtime().tm_mon),"\\",str(time.localtime().tm_year))))
  print(''.join(data))

  ofile=open("lock-end","w")
  ofile.write(''.join(data))
  counter=counter+1
 space_lvl=space_lvl+1


## chars printed
a=chars_complete.replace('\n','').replace('\t','').replace('\r','').replace('\v','').replace('\f','')

ofile.close()

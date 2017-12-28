#! /usr/bin/python3

import psutil, math, os, time

class rammed():
    #please not that running this in a stored object will result in never reaching the mem_limit defined
    acc=str()
    expo=2
    limit=4096
    #create string to append to memory filling string, acc
    acc_str=list()
    str_len=int()
    str_len=int(math.pow(limit,expo))
    def init(self):
        for i in range(0,self.str_len):
            self.acc_str.append(str(i))
    
    mem_limit=50
    
    mem_p=psutil.virtual_memory().percent
    #since this is a spammer, we do not want it quit after it reaches the 
    #mem_limit, but rather continue looping, without any addition
    def RAM(self):
        self.init()
        x=1
        while x == 1:
            self.mem_p=psutil.virtual_memory().percent
            print(self.mem_p)

            if float(self.mem_p) < float(self.mem_limit):
                self.acc+=''.join(self.acc_str)
            else:
                time.sleep(90)

#! /usr/bin/env python3

import numpy,pandas as pd,math,string


class container:
    class data:
        master=None
        def maxStorage(self):
            number='0'*10
            bytesPerLine=10
            phoneNumberLen=len(number)
            phoneNumberDigits=len(string.digits)
            maxPhoneNumbers=math.pow(phoneNumberLen,phoneNumberDigits)
            maxStorage=maxPhoneNumbers*bytesPerLine
            return maxStorage

    class processing:
        master=None
        def engineering(self,num):
            if 1000 > num > 0:
                #b
                return str(num)+"b".upper()
            elif 1000**2 > num > 1000**1: 
                #k
                return str(num/(1000**1))+"kb".upper()
            elif 1000**3 > num > 1000**2:
                #m
                return str(num/(1000**2))+"mb".upper()
            elif 1000**4 > num > 1000**3:
                #g
                return str(num/(1000**3))+"gb".upper()
            elif 1000**5 > num > 1000**4:
                #t
                return str(num/(1000**4))+"tb".upper()
            elif 1000**6 > num > 1000**5:
                #p
                return str(num/(1000**5))+"pb".upper()
    class tasks:
        #this is where the work should be done
        #so as to not pollute the assembler
        master=None
        def run(self):
            maxStorage=self.master.data.maxStorage()
            result=self.master.processing.engineering(maxStorage)
            print(result)

    class void:
        master=None

    def assembler(self):
        #this is just to put all objects in the work area wa
        wa=self.void()
        wa.master=wa

        wa.data=self.data()
        wa.data.master=wa

        wa.processing=self.processing()
        wa.processing.master=wa

        wa.tasks=self.tasks()
        wa.tasks.master=wa
        wa.tasks.run()

cont=container()
cont.assembler()

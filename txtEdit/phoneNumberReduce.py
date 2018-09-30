#! /usr/bin/env python3
#noguilinux
#reduce various phone number formats to a single format
import sys

class num:
    digits='0123456789'
    number=''
    area=''
    
    def numberStrip(self,number=''):
        numAcc=''
        for char in number:
            if char in self.digits:
                numAcc+=char
        return numAcc
    def unify(self,number=''):
        area=self.area
        local=''
        last4=''
        if len(number) == 10:
            area=number[0:3]
            local=number[3:6]
            last4=number[6:10]
        elif len(number) == 7:
            local=number[0:3]
            last4=number[3:7]
        else:
            return "BAD_NUM"
        form=[area,local,last4]
        acc=''
        for num,i in enumerate(form):
            if i != "":
                if num < len(form)-1:
                    acc+=i+"-"
                else:
                    acc+=i
        return acc

    def badNumHelp(self):
        message="phone number should either be 7 'OR' 10 numbers in long [8048574054 == 804-857-4054]"
        print(message)

    def begin(self):
        final=list()
        if len(sys.argv) < 2:
            number=sys.stdin
            for lines in number:
                lineList=lines.split(" ")
                for line in lineList:
                    reduced=self.numberStrip(line)
                    final.append(self.unify(reduced))
        else:
            if len(sys.argv) == 2:
                numbers=sys.argv
                number=numbers[1].split(" ")
                for num in number:
                    reduced=self.numberStrip(num)
                    final.append(self.unify(reduced))
            elif len(sys.argv) > 2:
                #numbersLen=len(sys.argv)-1
                for Num,num in enumerate(sys.argv):
                    if Num > 0:
                        reduced=self.numberStrip(num)
                        final.append(self.unify(reduced))
        for number in final:
            yield number
    
    def check(self):
        BAD_ANUM="BAD_AREA_NUMBER"
        if len(self.area) == 3:
            for i in self.area:
                if i not in self.digits:
                    return BAD_ANUM
            return 0
        else:
            return BAD_ANUM

    def main(self):
        val=0
        if type(self.area) == type(str()):
            if self.area != '':
                val=self.check()
        elif type(self.area) == type(int()):
            self.area=str(self.area)
            val=self.check()
        elif type(self.area) == type(float()):
            self.area=str(int(self.area))
            val=self.check()
        else:
            val="AREA_NUM_BLANK"

        if val != 0:
            exit(val)
        else:
            result=self.begin()
        return result


parse=num()
#num.area can of types str,int,float, or you not even specify its existance
parse.area='804'
#if all goes well main will return a generator
cleanNum=parse.main()
for i in cleanNum:
    print(i)

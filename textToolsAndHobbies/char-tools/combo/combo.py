#! /usr/bin/python3
import math

class wordy():
    bypass=bool()
    default=bool()
    #in the event of changes that might cause a break
    lower="abcdefghijklmnopqrstuvwxyz"
    upper=lower.upper()
    number="1234567890"
    special="~!@#$%^&*()_+-=`[]\{}|;':\",./<>? "

    string=str()
    stringGenStr=str()
    StringOther=str()
    iString=str()
    
    def __init__(self):
        pass

    def init(self):
        if self.bypass == False:
            self.asciiGen()
        elif self.bypass == True:
            self.string=self.lower+self.upper+self.number+self.special

        if self.default == True:
            self.iString=self.string
        elif self.default == False:
            self.iString=self.StringOther

    def asciiGen(self):
        for i in range(32,127):
            self.stringGenStr+=chr(i)
        self.string=self.stringGenStr

    def message_word(self,data=str(),unique=int()):
        print("Input String: ",data)
        print("Input String Length: ",len(data))
        print("Combinations at "+str(unique)+"^"+str(len(data))+": "+str(math.pow(unique,len(data))))

    def message_dict(self,data=dict()):
        print("\nCharacter Statistics:\n")
        for i in data.keys():
            print("\t",i,data[i])

    def message_str(self,data=str()):
        print("unique chars: ",data)
    
    def wordStat(self,text):
     text_size=len(text)
     text_dict=dict()
     for i in  text:
         if i in text_dict.keys():
          text_dict[i]+=1
         else:
          text_dict[i]=1
     chars=len(text_dict)
     self.message_word(text,len(text_dict))
     self.message_str(chars)
     self.message_dict(text_dict)
    
# declare the class object
a=wordy()
# set values
a.default=True
a.bypass=True
a.StringOther="one more time"
# run init(), not __init__()
a.init()
# run the master function,wordStat
a.wordStat(a.iString)


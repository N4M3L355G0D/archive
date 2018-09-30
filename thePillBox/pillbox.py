#! /usr/bin/env python3

#pillbox chart creation tool using config
#follow the rules, and you'll be fine

import time, os

report=time.ctime()
user=os.environ['USER']
machine=''
day="day"
dEnd=str()
pills=dict()
days=["sun","mon","tue","wed","thu","fri","sat"]

for num,data in enumerate(os.uname()):
    if num < len(os.uname())-1:
        machine+=data+","
    else:
        machine+=data

print("report created on host: ".upper()+machine+"\n")
print("report generation date: ".upper()+report+"\n")
print("report create by user: ".upper()+user+"\n")

with open("config","r") as config:
    for i in config:
        what1=i.split("=")
        if what1[0] == "pills":
            for j in what1[1].split(","):
                what2=j.rstrip("\n").split("#")
                pills[what2[1]]=what2[0]
        if what1[0] in days:
            if what1[0] == "tue":
                dEnd="s"+day
            elif what1[0] == "wed":
                dEnd="nes"+day
            elif what1[0] == "thu":
                dEnd="rs"+day
            elif what1[0] == "sat":
                dEnd="ur"+day
            else:
                dEnd=day
            fieldDay=what1[0]+dEnd
            date=" Day: "+fieldDay.upper()
            print(date)
            for j in what1[1].split(","):
                what2=j.rstrip("\n").split("#")
                print("\tPill: "+pills[what2[0]]+"\n\t\tQuantity: "+what2[1])

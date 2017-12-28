import os,time

def expo():
 userdir=os.environ['HOME']
 expodir="/Pinbreak_reports"
  
 if not os.path.exists(userdir+expodir):
  os.mkdir(userdir+expodir)
 oFILE="/pinbreak_data_expo_repeats_"+str(time.ctime())+".html"
 OUT=userdir+expodir+oFILE
 return OUT

OUT=expo()

def dump1():
 file=open(OUT,"w")
 cellhead=list()

 elstart="\t<td>"
 elend="\t</td>"
 phonenumberS="PHONE_NUMBER"
 planS="PLAN"
 repeatS="Renewals Count"
 cellhead.append('<table style="width:100%>"')
 cellhead.append("<tr>")
 cellhead.append(elstart+phonenumberS+elend)
 cellhead.append(elstart+planS+elend)
 cellhead.append(elstart+repeatS+elend)
 cellhead.append("</tr>")
 for i in cellhead:
  file.write(i)
 file.close()
def dumper(phonenumber,plan,repeat):
 cell=list()

 elstart="\t<td>"
 elend="\t</td>"

 cell.append("<tr>")
 cell.append(elstart+phonenumber+elend)
 cell.append(elstart+plan+elend)
 cell.append(elstart+repeat+elend)
 cell.append("</tr>")

 file=open(OUT,"a")
 
 for i in cell:
  file.write(i)
 file.close()


def twofield(col1,col2):
 cell=list()
 elstart="\t<td>"
 elend="\t</td>"
 cell.append("<tr>")
 cell.append(elstart+col1+elend)
 cell.append(elstart+col2+elend)
 cell.append("\t</tr>")
 
 file=open(OUT,"a")
 for i in cell:
  file.write(i)
 file.close()

"""phonenumber="PHONE_NUMBER"
ordernumber="ORDER_NUMBER"
plan="PLAN"
user="USER"
pin="PIN"
date="DATE"
bill_date="BILL_DATE"
activation="ACTIVATION"

dumper(phonenumber,ordernumber,plan,user,pin,date,bill_date,activation) """

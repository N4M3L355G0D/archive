#! /usr/bin/python3

from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from textwrap import wrap

import subprocess, time,os,sys, platform

class system():
    if len(sys.argv) < 2:
        path="./"
    else:
        path=sys.argv[1]
        if not os.path.exists(path):
            path="./"
    #report generation date
    date=time.ctime()
    #get hostname
    hostname=platform.uname().node
    title="System Info. - "+date
    subtitle=hostname+" - Page "
    fname="report"
    def dateCode(path,fname):
        local=time.localtime()
        month=str(local.tm_mon)
        day=str(local.tm_mday)
        year=str(local.tm_year)
        hour=str(local.tm_hour)
        minute=str(local.tm_min)
        sec=str(local.tm_sec)
        datecode="h"+hour+"m"+minute+"s"+sec+"mm"+month+"dd"+day+"yy"+year
        print(path+"/"+fname+"."+datecode+".pdf")
        return datecode 
    Date=dateCode(path,fname)
    #get system data
    ##cmd for report gathering
    cmd="echo '--- hostname ---' ; hostname ; echo '--- lspci ---' ; lspci ; echo '--- lscpu ---' ; lscpu ; echo '--- ip addr ---' ; ip addr ; echo '--- lsusb ---' ; lsusb ; echo '--- lsblk ---' ; lsblk ; for i in `ls -1 /dev/sd[a-z]` ; do echo --- $i --- ; smartctl -a $i ; done "
    data=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    text,err=data.communicate()
    text=text.decode()
    text_t=text.split("\n")
    
    #set reportlab output
    width,height=letter
    font="Liberation Mono Regular"
    pdfmetrics.registerFont(TTFont(font,"LiberationMono-Regular.ttf"))
    font_size=7
    
    document = canvas.Canvas(path+"/"+fname+'.'+Date+'.pdf',pagesize=letter)
    document.setFont(font,font_size+10)
    document.drawCentredString(width/2,height-78,title)
    f=0
    count=0
    page=1
    document.setFont(font,font_size)
    document.drawCentredString(width/2,height-(78+font_size+10),subtitle+str(page))
    #how far from the top of the page the report starts
    #does not include page or title
    pagetop=108
    def date(self):
        local=time.localtime()
        month=str(local.tm_mon)
        day=str(local.tm_mday)
        year=str(local.tm_year)
        hour=str(local.tm_hour)
        minute=str(local.tm_min)
        sec=str(local.tm_sec)
        datecode="h"+hour+"m"+minute+"s"+sec+"mm"+month+"dd"+day+"yy"+year
        print("system-report."+datecode+".pdf")
        return datecode 

    def reset(self):
        #if ( f % int(self.height/self.font_size) != 0):
        self.document.showPage()
        self.page+=1
        self.document.setFont(self.font,self.font_size+10)
        self.document.drawCentredString(self.width/2,self.height-78,self.title)
        self.document.setFont(self.font,self.font_size)
        self.document.drawCentredString(self.width/2,self.height-(78+self.font_size+10),self.subtitle+str(self.page))
        self.f=0

    def main(self):
        if os.environ['USER'] == "root":
            #generate document
            for i in self.text_t:
                textp1=wrap(i,70)
                for num,j in enumerate(textp1):
                    self.document.setFont(self.font,self.font_size)
                    self.document.drawString(36,self.height-(self.pagetop+self.f),j)
                    if num == len(textp1)-1:
                        if (self.height-(self.pagetop*2)) < self.f:
                            self.reset()
                        self.document.drawString(36,self.height-(self.pagetop+self.f)," ")
                        self.f+=self.font_size
                    self.f+=self.font_size
                    self.count+=1
                print("points from page top",self.f,"for",self.page)
            self.document.save()
        else:
            sys.exit("user is not root!")

d=system()
d.main()

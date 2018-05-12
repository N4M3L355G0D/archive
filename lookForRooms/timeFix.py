
import time
#tString='2018-4-30 5:20pm'
def fixTime(self,tString)
    dString=tString
    date=dString.split(' ')[0]

    dTime=dString.split(' ')[1]
    if dTime[-2] == 'a':
        dTime=dTime[:-2]
    else:
        dTime=dTime.split(':')
        dTime=str(int(dTime[0])+12)+":"+dTime[1][:-2]
    
    dString=date+" "+dTime
    dString=time.strptime(dString,'%Y-%m-%d %H:%M')
    dString=time.strftime('%d-%m-%Y %H:%M',dConverted)
    return dString

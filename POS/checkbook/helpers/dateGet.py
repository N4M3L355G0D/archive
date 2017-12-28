#! /usr/bin/python3
import subprocess as sp
import argparse, time

def cmdline():
    parser=argparse.ArgumentParser()
    parser.add_argument("-a","--year-start",required="yes")
    parser.add_argument("-b","--year-end",required="yes")
    parser.add_argument("-c","--month-start",required="yes")
    parser.add_argument("-d","--month-end",required="yes")
    parser.add_argument("-e","--day-start",required="yes")
    parser.add_argument("-f","--day-end",required="yes")
    options=parser.parse_args()

    args=list()
    if options.year_start:
        args.append(options.year_start)
    else:
        args.append(int(time.localtime().tm_year))

    if options.year_end:
        args.append(options.year_end)
    else:
        args.append(int(options.year_start)+1)
    
    if options.month_start:
        args.append(int(options.month_start))
    else:
        args.append(1)
    
    if options.month_end:
        args.append(int(options.month_end))
    else:
        args.append(13)

    if options.day_start:
        args.append(int(options.day_start))
    else:
        args.append(1)

    if options.day_end:
        args.append(int(options.day_end)+1)
    else:
        args.append(32)
    return args

def search():
 chronoT="list,range,range"
 
 args=cmdline()

 if chronoT == "list,range,range":
  year=[int(args[0]),int(args[1])]
  day=[int(args[4]),int(args[5])]
  month=[int(args[2]),int(args[3])]
  for i in range(month[0],month[1]):
      for j in range(day[0],day[1]):
          for k in range(year[0],year[1]):
              shell="python readEntry.py -f BILL_DATE -v "+str(i)+"-"+str(j)+"-"+str(k)
              sp.Popen(shell,shell=True)
              #print(shell)

##should do a year range
##should use cmdline args for year,date,month
search()

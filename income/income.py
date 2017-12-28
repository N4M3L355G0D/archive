#! /usr/bin/python3
import argparse

def month(month_m="january",leap_year="no",hourly_rate=7.25,offset=4,day_len=8):
 month_m=str(month_m).lower()
 day31=("january","march","may","july","august","october","december")
 day30=("april","june","september","november")
 if month_m == "february" and leap_year == "no":
  income_crunch(28,hourly_rate,offset,day_len)
 elif month_m == "february" and leap_year == "yes":
  income_crunch(29,hourly_rate,offset,day_len)
 elif month_m in day31:
  income_crunch(31,hourly_rate,offset,day_len)
 elif month_m in day30:
  income_crunch(30,hourly_rate,offset,day_len)

def income_crunch(day=31,hourly=7.25,offset=4,day_len=8):
 hours_m=(day-offset)*day_len
 monthly_in=hourly*hours_m
 print(monthly_in)

def month_cmd():
 offset=4
 day_len=8
 parser=argparse.ArgumentParser()
 parser.add_argument("-m","--month",help="month for which income is calculated, with a -4 day offset",required="yes")
 parser.add_argument("-l","--leap-year",help="for february's functionality",required="yes")
 parser.add_argument("-r","--hourly-rate",help="hourly pay rate",required="yes")
 parser.add_argument("-o","--offset-day",help="days not counted to monthly income")
 parser.add_argument("-d","--day-len",help="day length in hours") 

 options=parser.parse_args()
 if options.offset_day:
  offset=float(options.offset_day)
 if options.day_len:
  day_len=float(options.day_len)
 
 month(options.month,options.leap_year,float(options.hourly_rate),offset,day_len)

month_cmd()

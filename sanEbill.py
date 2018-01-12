import datetime, time

year=time.localtime().tm_year
days=(datetime.date(year,3,1)-datetime.date(year,2,1)).days
leapyear=False

if days == 28:
    leapyear=False
elif days == 29:
    leapyear=True

#power consumption of san
kW=''
while type(kW) != type(float()):
    try:
        kW=float(input("how many kilowatt hours of power do you use? [enter a number] : "))
    except:
        print("you need to enter a number")

#power cost
try:
    kWhCost=float(input("what is your fuel rate in cents? [if blank, default will be used] : "))
except:
    kWhCost=10.83

#time run
hours=24

day30M=(30,4)
day31M=(31,7)
day28M=(28,1)
day29M=(29,1)

costHour=round(((kW*(1*1))*(kWhCost/1))/100,2)
costHour6=round(((kW*(1*6))*(kWhCost/1))/100,2)
costHour12=round(((kW*(1*12))*(kWhCost/1))/100,2)
costHour18=round(((kW*(1*18))*(kWhCost/1))/100,2)

costDay=round(((kW*(1*hours))*(kWhCost/1))/100,2)
costMonth30=round(((kW*(day30M[0]*hours))*(kWhCost/1))/100,2)
costMonth31=round(((kW*(day31M[0]*hours))*(kWhCost/1))/100,2)
costMonth28=round(((kW*(day28M[0]*hours))*(kWhCost/1))/100,2)
costMonth29=round(((kW*(day29M[0]*hours))*(kWhCost/1))/100,2)

if leapyear == False:
    costYear=round(((costMonth30*day30M[1])+(costMonth31*day31M[1])+(costMonth28*day28M[1])),2)
if leapyear == True:
    costYear=round(((costMonth30*day30M[1])+(costMonth31*day31M[1])+(costMonth29*day29M[1])),2)


anualkWh=((((kW*1000)*(day30M[0]*hours))*day30M[1])+(((kW*1000)*(day31M[0]*hours))*day31M[1])+(((kW*1000)*(day28M[0]*hours))*day28M[1]))*(10**-3)

report=[("----Fuel Rate----"),("Fuel Rate per kWh in cents:",kWhCost),("----Year Type----"),("leap-year:",leapyear),("----Costs in Dollars----"),("per-month-30day:",costMonth30),("per-month-31day:",costMonth31),("per-month-28day:",costMonth28),("per-month-29day:",costMonth29),("per-hour:",costHour),("per-hour6:",costHour6),("per-hour12:",costHour12),("per-hour18:",costHour18),("per-day:",costDay),("per-year:",costYear),("----Consumption----"),("kWh:",kW),("anual-kWh-consumption:",anualkWh)]

for i in report:
    if type(i) == type(tuple()):
        print(i[0],i[1])
    else:
        print(i)


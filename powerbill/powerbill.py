#! /usr/bin/python3

import math
'''
original_formula=(((128.97/2)-(232.15/4))*2)+51.59
'''
landlord_shares=2

def floatCheck(number):
    period_counter=0
    '''number must be a str()'''
    numbers="1234567890."
    if len(number) > 0:
        for i in number:
            if i not in numbers:
                return {"fail":True,"reason":"invalid chars"}
            if i == ".":
                period_counter+=1
                if period_counter > 1:
                    return {"fail":True,"reason":"too many decimal points/periods/dots"} 
        return {"fail":False,"reason":float(number)}
    else:
        return {"fail":True,"reason":"value too short"}


#error report dictionary
userIn_err={"userIn_landlord":{"state":False,"reason":"none"},"userIn_total_bill":{"state":False,"reason":"none"},"userIn_per_share_bill":{"state":False,"reason":"none"}}
master_fail=False

# take user input and run float check for valid float values
#checks for more than one decimal points
userIn_landlord=floatCheck(input("landlord bill total : "))
userIn_total_bill=floatCheck(input("total bill : "))
userIn_per_share_bill=floatCheck(input("per share bill for tenants : "))

#do error checking, if errors found create report
if userIn_landlord["fail"] == True:
    userIn_err["userIn_landlord"]["state"]=True
    userIn_err["userIn_landlord"]["reason"]=userIn_landlord["reason"]
if userIn_total_bill["fail"] == True:
    userIn_err["userIn_total_bill"]["state"]=True
    userIn_err["userIn_total_bill"]["reason"]=userIn_total_bill["reason"]
if userIn_per_share_bill["fail"] == True:
    userIn_err["userIn_per_share_bill"]["state"]=True
    userIn_err["userIn_per_share_bill"]["reason"]=userIn_per_share_bill["reason"]

#run through error report
# if any errors, set master_fail to True
for i in userIn_err.keys():
    if userIn_err[i]["state"] == True:
        master_fail=True
        break
#if master_ fail is True, then print the error report and exit
if master_fail == True:
    print("[ERROR] : READ THE FOLLOWING REPORT CODE\n",userIn_err)
else:
    #if no errors, being formula run
    
    landlord_share_bill=userIn_landlord["reason"]/landlord_shares
    total_shares=4
    
    total_bill=userIn_total_bill["reason"]
    
    per_share_bill=userIn_per_share_bill["reason"]
    
    per_share_cost=total_bill/total_shares
    landlord_offset_single=landlord_share_bill-per_share_cost
    landlord_offset_double=landlord_offset_single*2
    
    amount_to_be_paid=landlord_offset_double+per_share_bill
    print("[what I will pay]",amount_to_be_paid)
    #when paying a bill, it is better to round up
    print("[Rounded up]",math.ceil(amount_to_be_paid))

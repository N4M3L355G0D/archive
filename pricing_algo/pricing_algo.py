#! /usr/bin/python3

import argparse

def cmdline():
 parser=argparse.ArgumentParser()
 parser.add_argument("-oh","--on-hand",help="on hand parts cost")
 parser.add_argument("-b","--bought",help="bought parts cost")
 parser.add_argument("-t","--travel_distance",help="distance travelled in miles")
 parser.add_argument("-g","--average_gas_t",help="the average gas price for the distance travelled")
 parser.add_argument("-hr","--hourly_r",help="hourly rate for the job")
 parser.add_argument("-wh","--worked-hours",help="hours worked")
 options=parser.parse_args()
 return options
def repair(): 
 if cmdline().worked_hours == None:
   hours=0
 else:
  hours=cmdline().worked_hours
 ## need minute flexibility
 if cmdline().hourly_r == None:
  hourly_r=10
 else:
  hourly_r=cmdline().hourly_r
 ## b for bought
 if cmdline().bought == None:
  b_parts_cost=0
 else:
  b_parts_cost=cmdline().bought
 ## oh for on-hand
 if cmdline().on_hand == None:
  oh_parts_cost=0
 else:
  oh_parts_cost=cmdline().on_hand
 ## travel cost is if i have to go to the customer to do an operation
 ## free software is free, but costs data to download. if the software is on hand, still apply the fee for free software download.
 free_software_download_fee=5
 if cmdline().average_gas_t == None or cmdline().travel_distance == None:
  travel_cost=0
 else:
  travel_cost=float(cmdline().average_gas_t)*float(cmdline().travel_distance)
 
 total=int(hourly_r)*int(hours)+int(b_parts_cost)+int(travel_cost)+int(oh_parts_cost)
 return total
data=repair()
print(data)

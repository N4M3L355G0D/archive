#! /usr/bin/python3


import argparse

try:
    parser=argparse.ArgumentParser()
    parser.add_argument("-b","--business-card",action="store_true")
    parser.add_argument("-s","--summary-of-skills",action="store_true")
    parser.add_argument("-c","--certifications",action="store_true")
    parser.add_argument("-w","--work-xp",action="store_true")
    parser.add_argument("-e","--education",action="store_true")
    parser.add_argument("-r","--resume",action="store_true")
    options=parser.parse_args()

    resString=[]
    if options.business_card:
        resString.append("#bc")
    
    if options.summary_of_skills:
        resString.append("#sok")
    
    if options.certifications:
        resString.append("#c")
    
    if options.work_xp:
        resString.append("#wxp")
    
    if options.education:
        resString.append("#e")
    
    if options.resume:
        resString=["#resume"]
    
    if len(resString) == 0:
        print("please look at --help/-h")
    else:
        print(''.join(resString))
except:
    print('err')

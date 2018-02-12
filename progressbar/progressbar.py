#! /usr/bin/env python3

import os, time,sys

def barGen(percent,header):
    rows=os.get_terminal_size().columns-10
    percentAsDec=percent/100
    barForPercent=int(round(percentAsDec*rows))*'='
    return barForPercent

def main(state,MAX):
    header='[{}/{}] '.format(state,MAX)
    bar=barGen(state,header)
    string=header+bar
    if state == 0:
        sys.stdout.write(string)
    else:
        sys.stdout.write((len(string)-1)*'\b'+string)
    sys.stdout.flush()

for i in range(100):
    main(i,100)
    time.sleep(0.1)
print('')

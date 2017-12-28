#! /usr/bin/python3
import os, sys

length=8
acc=""
user=sys.argv[1]
for i in enumerate(user):
    if i[0] <= length:
       acc=acc+''.join(i[1]).rstrip('\n')
print(acc)

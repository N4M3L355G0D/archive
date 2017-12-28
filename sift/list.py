import sys


rem=sys.argv[1]
remlist=list()
for i in rem.split(","):
 remlist.append(i)
print(remlist)

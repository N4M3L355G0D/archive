total=open("pk2.txt","r") 
delete=open("remove.txt","r")
l1=dict()
l2=dict()
ps=dict()
for i in total:
 pk=i.rstrip("\n")
 l1[pk]=" "
for x in delete:
 pkr=x.rstrip("\n")
 l2[pkr]=" "


for x in l2.keys():
  del l1[x]
for i in l1.keys():
  print(i)

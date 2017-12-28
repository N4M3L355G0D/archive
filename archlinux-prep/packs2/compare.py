list1=list()
list2=list()
common=dict()
unique=dict()
file1="./packages-arch.txt"
file2="./packages-manjaro.txt"
stream1=open(file1,"r")
stream2=open(file2,"r")

for i in stream1:
    list1.append(i.rstrip("\n"))

for i in stream2:
    list2.append(i.rstrip("\n"))

for i in list1:
    if i not in list2:
        unique[i]=i
for i in list2:
    if i not in list1:
        unique[i]=i

for i in unique.keys():
    print(i)

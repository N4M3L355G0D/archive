import os
accL=list()
location="/home/"
for i in os.listdir(location):
 path=location+i+"/.bash_history"
 if os.path.exists(path):
  accL.append(path)
print(accL)

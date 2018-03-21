import netifaces

#get the addresses of the interfaces that are up and have an assigned address

#the readable form
a=[[netifaces.ifaddresses(i)[x][0] for num,x in enumerate(netifaces.ifaddresses(i).keys()) if num == 1][0] for i in netifaces.interfaces() if len(netifaces.ifaddresses(i)) >= 3]
b=[i for i in netifaces.interfaces() if len(netifaces.ifaddresses(i)) >= 3]
final={t[0]:t[1] for t in zip(b,a)}

#the more difficult to read form
final_oneliner={u[0]:u[1] for u in zip([i for i in netifaces.interfaces() if len(netifaces.ifaddresses(i)) >= 3],[[netifaces.ifaddresses(i)[x][0] for num,x in enumerate(netifaces.ifaddresses(i).keys()) if num == 1][0] for i in netifaces.interfaces() if len(netifaces.ifaddresses(i)) >= 3])}


#the three liner
print(final)
#the one liner
print(final_oneliner)

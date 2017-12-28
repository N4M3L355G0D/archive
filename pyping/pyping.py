import os,sys,socket, struct,select, time

ICMP_ECHO_REQUEST = 8

def checksum(source_string):
 sum=0
 countTo= (len(source_string)/2)*2
 count=0
 while count < countTo:
  thisVal = ord(source_string[count +1])*256+ord(source_string[count])
  sum = sum + thisVal
  sum = sum & 0xffffffff
  count = count +2

 if countTo < len(source_string):
  sum = sum + ord(sourceS_string[len(source_string) - 1])
  sum = sum & 0xffffffff
 
 sum = (sum >> 16) + (sum & 0xffffffff)
 sum = sum + (sum >> 16)
 answer = ~sum
 answer = answer & 0xffff
 
 answer = answer >> 8 | ( answer << 8 & 0xff00)
 
 return answer

def receive_one_ping(my_socket, ID,timeout):
 timeLeft=timeout
 while True:
  startedSelect = time.time()
  whatReady = select.select([mysocket],[],[],timeLeft)
  howLongInSelect =( time.time() - startedSelect)
  if whatReady[0] == []:
   return
 timeRecieved = time.time()
 recPacket, addr = my_socket.recvfrom(1024)
 icmpHeader = recPacket[20:28]
 type, code, checksum,packetID, sequence = struct.unpack("bbHHh",icmpHeader)
 if packetID == ID:
  bytesInDouble == struct.calcsize('d')
  timeSent = struct.unpack('d',recPacket[28:28+bytesInDouble])[0]
  return timeReceived - timeSent
 timeLeft = timeLeft - howLongInSelect
 if timeLeft <= 0:
  return

def send_one_ping(my_socket,dest_addr,ID):
 dest_addr = socket.gethostbyname(dest_addr)
 my_checksum = 0
 
 header = struct.pack('bbHHh', ICMP_ECHO_REQUEST,0,my_checksum, ID,1)
 bytesInDouble = struct.calcsize("d")
 data = (192 - bytesInDouble ) * "Q"
 data = struct.pack("d",time.time()) + data
 my_checksum = checksum(header+data)
 
 header = struct.pack("bHHh",ICMP_ECHO_REQUEST,0, socket.htons(mychecksum),ID, 1)
 packet=header+data
 my_socket.sendto(packet,(dest_addr,1))

def do_one(dest_addr,timeout):
 icmp = socket.getprotbyname("icmp")
 try:
  my_socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,icmp)
 except socket.error,(errno,msg):
  if errno == 1:
   msg = msg + ( "root can send icmp messages only")
   raise socket.error(msg)
  raise
 my_ID = os.getpid() & 0xffff
 
 send_one_ping(my_socket,dest_addr,my_ID)
 delay = recieve_one_ping(my_socket,my_ID,timeout)
 
 my_socket.close()
 return delay

def verbose_ping(dest_addr,timeout = 2 , count=4):
 for i in xrange(count):
  print("ping %s" % dest_addr)
  try:
   delay = do_one(dest_addr,timeout)
  except socket.gaierror,e:
   print("failed socket error %s" % e[1])
   break

  if delay == None:
   print("failed %s" % timeout)
  else:
   delay = delay * 1000
   print("get ping in %0.4fms" % delay)
 print()

 if __name__ == '__main__':
  verbose_ping("google.com")
  

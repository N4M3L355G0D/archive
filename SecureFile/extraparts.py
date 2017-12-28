import netifaces as ni
import platform, time


NICS=ni.interfaces()
pairs=dict()
xclass_iface=list()

def interface_ip():
 xclass_iface_addr=""
 for interface in NICS:
  xclass_iface=list()
  if len(ni.ifaddresses(interface)) > 1:
   ip=ni.ifaddresses(interface)[2][0]['addr']
   xclass_iface.append("\t<interface="+str(interface)+">")
   xclass_iface.append("</interface>\n")
   xclass_iface_addr=xclass_iface_addr+xclass_iface[0]+str(ip)+xclass_iface[1] 
 return xclass_iface_addr

def hostname():
 xclass_host=list()
 xclass_host.append("\t<host>")
 xclass_host.append("</host>\n")
 hostname=platform.uname().node
 host=xclass_host[0]+hostname+xclass_host[1]
 return host

def macaddress():
 xclass_mac=list()
 xclass_mac_str=""
 ifaces=ni.interfaces()
 for i in ifaces:
  mac=ni.ifaddresses(i)[ni.AF_LINK][0]['addr']
  xclass_mac.append("\t<MAC interface="+str(i)+">"+str(mac)+"</MAC>\n")
 for i in xclass_mac:
  xclass_mac_str=xclass_mac_str+i
 return xclass_mac_str

def date_extended():
 datedata=time.localtime()
 date_str="\t<date_extended>"+str(datedata.tm_mon)+"."+str(datedata.tm_mday)+"."+str(datedata.tm_year)+" @ "+str(datedata.tm_hour)+":"+str(datedata.tm_min)+":"+str(datedata.tm_sec)+"</date_extended>\n"
 return date_str

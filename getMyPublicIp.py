import urllib3
url='ip.42.pl'
pool=urllib3.HTTPConnectionPool(url,maxsize=1)
request=pool.request("GET","/raw")
ip=request.data.decode()
print(ip)


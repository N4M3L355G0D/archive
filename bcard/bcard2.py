#! /usr/bin/env python3
import sqlite3,gzip,os
import base64 as b64
dB="""H4sIAFTuZVoAA+3YT0/CMBgG8Ps+zTbBxIOHttA5GJgOOtludE0osrLF4P7w6WXiTLyY
mBi9PE/SN23f5Nf0+kqPL7abuAiDrM6tZzQjZ0IJIWJKBCM70ue9huRrpp9liHNZlPwsjLBR2hG3
39PJbUP6NWC/FmDAgAEDBgwYMGDAgAEDBgwYMGDAgAH7tstDSts84SKg9CY2qW2L1OddFixNbgUT
3oyLJOYhj6k4tNwJr41SWX7KVtTNNsaNgqxWVu50kIw0awv1xCvFhp6udGC8dH89z8XHVHTsEqcv
f/NNYMCAAQMGDBgwYMCAAQMGDBgwYMCAAfs3jBqHCFnP5DIRPu8Uo/Nwaqrcjot8T2creRgtJuL0
OJFutBbNcq1fIlu+boOiUzbpoqOucj+ulaTHfvzqKDZ+Vr5X6oe4yc9lHfnDHLa/d+ssSM5b/+4c
bUwTXR5MfVNpK++dN3CKEC88KwAA"""
dB=b64.b64decode(gzip.decompress(b64.b64decode(dB.encode())))
file=open("bc.db","wb")
file.write(dB)
file.close()
#this file is intended for a 2X3 business card, thus no checking
db=sqlite3.connect("bc.db")
cursor=db.cursor()
sql="select * from card;"
cursor.execute(sql)
for row in cursor.fetchall():
    for col in row:
        print(col)
os.remove("bc.db")

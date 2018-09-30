#! /usr/bin/env python3
#noguilinux

python3 << EOF
stringMixCap="outofmemoryerror"
acc=''
for num,i in enumerate(stringMixCap):
 if num % 2 == 0:
  acc+=i.upper()
 else:
  acc+=i.lower()
print(acc)

EOF

#! /usr/bin/python3

import itertools,string

STOP=None
a=itertools.product("abcd",repeat=2)
b=next(itertools.islice(a,1,STOP))
print(b)

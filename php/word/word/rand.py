#! /usr/bin/env python3

import os,binascii 
print(binascii.hexlify(os.urandom(128))).decode()

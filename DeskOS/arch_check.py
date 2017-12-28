#! /usr/bin/python3

import os

def arch_check():
 machine=os.uname().machine
 if machine == 'i686':
  return 32
 elif machine == 'x86_64':
  return 64

print(arch_check())

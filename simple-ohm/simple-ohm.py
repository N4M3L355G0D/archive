#! /usr/bin/python


import argparse
import sys
import os
from ohm import resistance
from volt import volt
from amp import amp

ohms=0
volts=0
amps=0
metricV=""
metricA=""
metricO=""

warning="Valid Metrics : kilo = 10^3, mega = 10^6, giga = 10^9, nano = 10^-9, micro = 10^-6, milli = 10^-3 | Please remember, the metric option is optional.\n\tBut if you do not use this option,\n\tthen you must adjust your values accordingly to\n\tyeild correct results. | "

error="Please use -r, -v, -a, according to the operation you are performing.\nFor more information, use -h/--help."

option = argparse.ArgumentParser(epilog=warning)
option.add_argument("-v",help="Required : Gets voltage from <Amp> * <Ohm>")
option.add_argument("-r",help="Required : Gets Resistance from <Volt> / <Amp>")
option.add_argument("-a",help="Required : Gets Current from <Volt> / <Ohm>")
option.add_argument("-metricO",help="engineering format for <Ohm>")
option.add_argument("-metricA",help="engineering format for <Amp>")
option.add_argument("-metricV",help="engineering format for <Volt>")


options=option.parse_args()
if options.r == None:
	if options.v == None:
		print(error)
		exit()
	elif options.a == None:
		print(error)
		exit()
elif options.v == None:
	if options.a == None:
		print(error)
		exit()
	elif options.r == None:
		print(error)
		exit()
elif options.a == None:
	if options.v == None:
		print(error)
		exit()
	elif options.r == None:
		exit()


if options.v:
	volts=float(options.v)
	metricV=options.metricV
	if options.r:
		ohms=float(options.r)
		metricO=options.metricO
		result=amp(volts,ohms,metricV,metricO)
		print(result)
	elif options.a:
		amps=float(options.a)
		metricA=options.metricA
		result=resistance(volts,amps,metricV,metricA)
		print(result)
elif options.a:
	amps=float(options.a)
	metricA=options.metricA
	if options.v:
		volts=float(options.v)
		metricV=options.metricV
		result=resistance(volts,amps,metricV,metricA)
		print(result)
	elif options.r:
		ohms=float(options.r)
		metricO=options.metricO
		result=volt(ohms,amps,metricO,metricA)
		print(result)
elif options.r:
	ohms=float(options.r)
	metricO=options.metricO
	if options.v:
		volts=float(options.v)
		metricV=options.metricV
		result=amps(volts,ohms,metricV,metricO)
		print(result)
	elif options.a:
		amps=float(options.a)
		metricA=options.metricA
		result=volt(ohms,amps,metricO,metricA)
		print(result)

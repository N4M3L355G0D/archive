#! /usr/bin/python

import math

def amp(volt,ohm,metricV,metricO):
	if metricO == None:
		pass
		#no powers
	elif metricO == "nano":
		#10^-9
		ohm = ohm * math.pow(10,-9)
	elif metricO == "micro":
		#10^-6
		ohm = ohm * math.pow(10,-6)
	elif metricO == "milli":
		#10^-3
		ohm = ohm * math.pow(10,-3)
	elif metricO == "kilo":
		#10^3
		ohm = ohm * math.pow(10,3)
	elif metricO == "mega":
		#10^6
		ohm = ohm * math.pow(10,6)
	elif metricO == "giga":
		#10^9
		ohm = ohm * math.pow(10,9)
	
	if metricV == None:
		pass
	elif metricV == "nano":
		volt = volt * math.pow(10,-9)
	elif metricV == "micro":
		volt = volt * math.pow(10,-6)
	elif metricV == "milli":
		volt = volt * math.pow(10,-3)
	elif metricV == "kilo":
		volt = volt * math.pow(10,3)
	elif metricV == "mega":
		volt = volt * math.pow(10,6)
	elif metricV == "giga":
		volt = volt * math.pow(10,9)
			
	amp = volt / ohm

	if amp < 1000:
		place = "Amp"
	elif amp < 1000000:
		place = "kilo"
	elif amp < 1000000000:
		place = "mega"
	elif amp < 1000000000000:
		place = "giga"
	elif amp < 0.000001:
		place = "nano"
	elif amp < 0.001:
		if amp > 0.0000009:
			place = "micro"
		else:
			place = "nano"
	elif amp < 1:
		if amp > 0.0009:
			place = "milli"
		else:
			if amp > 0.0000009:
				place = "micro"
			else:
				if amp > 0.0000000009:
					place = "nano"

	return amp,place



#! /usr/bin/python

import math

def resistance(volt,amp,metricV,metricA):
	if metricA == None:
		pass
		#no powers
	elif metricA == "nano":
		#10^-9
		amp = amp * math.pow(10,-9)
	elif metricA == "micro":
		#10^-6
		amp = amp * math.pow(10,-6)
	elif metricA == "milli":
		#10^-3
		amp = amp * math.pow(10,-3)
	elif metricA == "kilo":
		#10^3
		amp = amp * math.pow(10,3)
	elif metricA == "mega":
		#10^6
		amp = amp * math.pow(10,6)
	elif metricA == "giga":
		#10^9
		amp = amp * math.pow(10,9)
	
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
			
	ohm = volt / amp

	if ohm < 1000:
		place = "Ohm"
	elif ohm < 1000000:
		place = "kilo"
	elif ohm < 1000000000:
		place = "mega"
	elif ohm < 1000000000000:
		place = "giga"
	elif ohm < 0.000001:
		place = "nano"
	elif ohm < 0.001:
		if ohm > 0.0000009:
			place = "micro"
		else:
			place = "nano"
	elif ohm < 1:
		if ohm > 0.0009:
			place = "milli"
		else:
			if ohm > 0.0000009:
				place = "micro"
			else:
				if ohm > 0.0000000009:
					place = "nano"
 
	return ohm,place



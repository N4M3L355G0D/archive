#! /usr/bin/python

import math

def volt(ohm,amp,metricO,metricA):
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
	
	if metricO == None:
		pass
	elif metricO == "nano":
		ohm = ohm * math.pow(10,-9)
	elif metricO == "micro":
		ohm = ohm * math.pow(10,-6)
	elif metricO == "milli":
		ohm = ohm * math.pow(10,-3)
	elif metricO == "kilo":
		ohm = ohm * math.pow(10,3)
	elif metricO == "mega":
		ohm = ohm * math.pow(10,6)
	elif metricO == "giga":
		ohm = ohm * math.pow(10,9)
			
	voltage = ohm * amp

	if voltage < 1000:
		place = "Volt"
	elif voltage < 1000000:
		place = "kilo"
	elif voltage < 1000000000:
		place = "mega"
	elif voltage < 1000000000000:
		place = "giga"
	elif voltage < 0.000001:
		place = "nano"
	elif voltage < 0.001:
		if voltage > 0.0000009:
			place = "micro"
		else:
			place = "nano"
	elif ohm < 1:
		if voltage > 0.0009:
			place = "milli"
		else:
			if voltage > 0.0000009:
				place = "micro"
			else:
				if voltage > 0.0000000009:
					place = "nano"
 
	return voltage,place



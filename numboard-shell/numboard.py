#! /usr/bin/python3.4

import os

def lowerAlpha(string):
	if string == "01":
		return "a"
	elif string == "02":
		return "b"
	elif string == "03":
		return "c"
	elif string == "04":
		return "d"
	elif string == "05":
		return "e"
	elif string == "06":
		return "f"
	elif string == "07":
		return "g"
	elif string == "08":
		return "h"
	elif string == "09":
		return "i"
	elif string == "10":
		return "j"
	elif string == "11":
		return "k"
	elif string == "12":
		return "l"
	elif string == "13":
		return "m"
	elif string == "14":
		return "n"
	elif string == "15":
		return "o"
	elif string == "16":
		return "p"
	elif string == "17":
		return "q"
	elif string == "18":
		return "r"
	elif string == "19":
		return "s"
	elif string == "20":
		return "t"
	elif string == "21":
		return "u"
	elif string == "22":
		return "v"
	elif string == "23":
		return "w"
	elif string == "24":
		return "x"
	elif string == "25":
		return "y"
	elif string == "26":
		return "z"
	elif string == "27":
		return "~"
	elif string == "28":
		return "`"
	elif string == "29":
		return "!"
	elif string == "30":
		return "@"
	elif string == "31":
		return "#"
	elif string == "32":
		return "$"
	elif string == "33":
		return "%"
	elif string == "34":
		return "^"
	elif string == "35":
		return "&"
	elif string == "36":
		return "*"
	elif string == "37":
		return "("
	elif string == "38":
		return ")"
	elif string == "39":
		return "-"
	elif string == "40":
		return "_"
	elif string == "41":
		return "="
	elif string == "42":
		return "+"
	elif string == "43":
		return "["
	elif string == "44":
		return "]"
	elif string == "45":
		return "{"
	elif string == "46":
		return "}"
	elif string == "47":
		return "|"
	elif string == "48":
		return "\\"
	elif string == "49":
		return ":"
	elif string == "50":
		return ";"
	elif string == "51":
		return "'"
	elif string == "52":
		return "\""
	elif string == "53":
		return ","
	elif string == "54":
		return "<"
	elif string == "55":
		return "."
	elif string == "56":
		return ">"
	elif string == "57":
		return "/"
	elif string == "58":
		return "?"
	elif string == "59":
		return " "
	elif string == "60":
		return "\0"
	elif string == "61":
		return "\t"
	elif string == "62":
		return "\n"
	elif string == "63":
		return "A"
	elif string == "64":
		return "B"
	elif string == "65":
		return "C"
	elif string == "66":
		return "D"
	elif string == "67":
		return "E"
	elif string == "68":
		return "F"
	elif string == "69":
		return "G"
	elif string == "70":
		return "H"
	elif string == "71":
		return "I"
	elif string == "72":
		return "J"
	elif string == "73":
		return "K"
	elif string == "74":
		return "L"
	elif string == "75":
		return "M"
	elif string == "76":
		return "N"
	elif string == "77":
		return "O"
	elif string == "78":
		return "P"
	elif string == "79":
		return "Q"
	elif string == "80":
		return "R"
	elif string == "81":
		return "S"
	elif string == "82":
		return "T"
	elif string == "83":
		return "U"
	elif string == "84":
		return "V"
	elif string == "85":
		return "W"
	elif string == "86":
		return "X"
	elif string == "87":
		return "Y"
	elif string == "89":
		return "Z"
	else:
		return "that is not a valid character!"
	
a=""
while a != "-1":
	b=input("letter : ")
	blen=len(b)
	if blen < 2:
		if b == "0":
			a=""
		elif b == "1":
			os.system(a)
	elif blen == 2:
		if b == "-0":
			exit()
		else:
			a=a+lowerAlpha(b)
	elif blen > 2:
		if ( blen % 2 ) == 0:
			accum=""
			for x in range(0,blen,2):
				accum=b[x]
				accum=accum+b[x+1]
				a=a+lowerAlpha(accum)
		elif ( blen % 2 ) == 1:
			blen = blen - 1
			accum=""
			for x in range(0,blen,2):
				accum=b[x]
				accum=accum+b[x+1]
				a=a+lowerAlpha(accum)
	print("command : %s" % a)
		

import sys,argparse

parser=argparse.ArgumentParser()
parser.add_argument("-i","--input",help="input")
options=parser.parse_args()

a=""
if options.input:
 a=options.input


al=len(a)
sep="================"
acc=0
counter=0
mdiv=0
print("divisors\n"+sep)
for i in range(1,al):
 if al % i == 0:
  if mdiv < al/i:
   mdiv=al/i
  elif al/i < acc:
   acc=al/i
  elif acc == 0:
   acc=al/i
  print(i)

print("String Ends\n"+sep)
print("minimum divisor: ",acc)
print("maximum divisor: ",mdiv)

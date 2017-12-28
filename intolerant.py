#! /usr/bin/python3

''' a drunk joke, a depressing story rotating over chance, who knows '''
import random, time, math



state=["!drunk","drunk"]
notDrunk=list()
def approach():
 if random.randint(0,30) < 18:
  print("friend approaches you!\n let's get wasted!\n")
 else:
  print("you just lost your wife, your children, the IRS is coming to take your home, and you are about to get fired at work for intoxication at work, in a yellow cake factory. You drink 8 shots of whatever heavy liquor is on hand, pickup the Desert Eagle sitting next to you on your home office desk, placing the muzzle in your mouth, and pull the trigger. everything goes black in a brief shot of pain, your brains splattered across the wall, ceiling, and floor, behind you. You will not be missed!")
  exit()

def get_drunk():
 for i in notDrunk:
  if i != "!drunk":
   if random.randint(0,1) == 1:
    print("topple over")
   else:
    print("you drank too much and died of alcohol poisoning!") 
   return False
  else:
   print("drink another")
def main():
 for i in range(0,random.randint(1,365)):
  if random.randint(0,365) > i:
   notDrunk.append(state[0])
  elif (random.randint(0,6) % time.localtime().tm_wday) == 0:
   print("you are already drunk, and the friends that approached you were drunken hallucinations!")
   if ( random.randint(0,4*math.pow(10,6)) % ( 50 )) == 0:
    print("you have no friends!")
   if random.randint(0,4) in [1,2,3]:
    print("you never make it to the bar, even though you tried!")
    if random.randint(0,2) in [0,1]:
     print("you lose your way across a highway, get hit by a semi-truck, and die, while dreaming that heaven is a skip and a hop away!")
    else:
     print("you get arrested for public indecency, and get raped in a jail cell shower")
   return False
  else:
   notDrunk.append(state[1])
 if notDrunk[len(notDrunk)-1] != "drunk":
  notDrunk.append(state[1])
 approach()
 get_drunk()

main()

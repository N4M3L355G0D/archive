#! /usr/bin/python3

import time,os,threading, argparse

bash_cmd="play -n synth &"
kill_cmd="killall -9 play"
deactivation="700"
setting=5

""" create a monitor thread to kill the signal thread when the appropriate time is right"""

def cmdline():
 parser=argparse.ArgumentParser()
 parser.add_argument("-s","--stop-time",help="time when alarm stops")
 options=parser.parse_args()
 option=options.stop_time
 if option:
  return str(option)
 else:
  exit()

def sleeper(setting):
 time.sleep(setting)

def actor_time():
 now=time.localtime()
 now_hours=now.tm_hour
 now_minutes=now.tm_min
 if now_minutes < 10:
  now_minutes="0"+str(now_minutes)
 time_mil=str(now_hours)+str(now_minutes)
 return time_mil

def actor_hour():
 hour=time.localtime().tm_hour
 return hour

def monitor(deactivation):
 now=actor_time()
 hour=actor_hour()
 negate=0
 while hour < 24:
  now=actor_time()
  print(now)
  if str(now) == deactivation:
   if negate == 1:
    exit()
   elif negate == 0:
    negate=1
    os.system(kill_cmd)

def signal(bash_cmd=bash_cmd):
 os.system(bash_cmd)

def start(end_time):
 worker=threading.Thread(target=signal())
 worker.start()
 monitor(str(end_time))

timeless=cmdline()
start(timeless)
""" oh hey, one more note, the 'when the appropriate time is right' is indicative of 'when the defined time has been reached' """

""" need to find an old usb keyboard with a good key matrix circuit to convert into a sensor.
i will need to document all keys, especially the return key, this way I can detect the flow of current in the sign. """

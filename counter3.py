#!/usr/bin/env python
#from datetime import datetime, time
import time
import datetime
import RPi.GPIO as g
import Tkinter as tk
#from PIL import Image, ImageTkimport 
from time import sleep
import os
os.environ['DISPLAY'] = ":0"


g.setmode(g.BCM)
#g.setup(20, g.OUT)
#g.output(20, 1)
g.setup(21, g.IN, pull_up_down=g.PUD_DOWN) 
f = open("elecy.cvs", "a")
#global revcount
#revcount = 0
#textinfo="starting"
#currentwatts = 0
#lasttime=0


#print(is_time_between(time(23,0), time(8,00)))
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.textinfo = "starting"
        self.revcount = 0
        self.daycount = 0
        self.nightcount = 0
        self.currentwatts = 0
        self.lastime = datetime.datetime.now()
        self.label = tk.Label(text=self.textinfo)
        self.label.config(width=200)
        self.label.config(font=("Courier", 24))
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def is_time_between(self, begin_time, end_time, check_time=None):
        # If check time is not given, default to current UTC time
        check_time = datetime.datetime.now().time()
        print check_time
        print begin_time
        print end_time
        #check_time = check_time or datetime.datetime.utcnow().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else: # crosses midnight
            return check_time >= begin_time or check_time <= end_time

    def update_clock(self):
	if g.input(21):
	    print('Input was HIGH')
	    self.revcount+=1
            datetime.time(23,0)
            if(self.is_time_between(datetime.time(23,0), datetime.time(8,00))):
               self.nightcount+=1
            else:
               self.daycount+=1
	    secondspassed = (datetime.datetime.now() - self.lasttime).total_seconds() 
	    self.currentwatts = round((3600 / secondspassed),2)
		#print(str(secondspassed))
	    print(str(datetime.datetime.now()) + " " + str(self.revcount) + "Wh " + str(self.currentwatts) + "W")
            f = open("elecy.cvs", "a")
	    f.write(str(datetime.datetime.now()) + " " + str(self.revcount) + "Wh " + str(self.currentwatts) + "W " + str(self.daycount) + "dWh "+ str(self.nightcount) + "nWh "  + "\n")
            f.close()
	    self.textinfo= "".join(str(self.revcount) + "Wh " + str(self.currentwatts) + "W")
	    self.label.configure(text=self.textinfo)
            self.label.pack()
		#app.update_clock(textinfo)
        else:
            print('Input was LOW')
	lastval = g.input(21) 
	self.lasttime = datetime.datetime.now()

	    #To wait for a button press by polling in a loop:
	    
	while g.input(21) == lastval:
	    time.sleep(0.05)  # wait 10 ms to give CPU chance to do other things
            print("waiting" + str(lastval))
        self.root.after(2,self.update_clock)


app=App()

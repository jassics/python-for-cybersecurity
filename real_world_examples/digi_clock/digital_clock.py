#!/usr/bin/python3
# tkinter is installed already with python. But in case you get module not found error. Try this
# MacOS: brew install python-tk
# Ubuntu: sudo apt-get install python3-tk
# Test tkinter: python3 -m tkinter
from tkinter import Label, Tk
import time

digi_clock = Tk()
digi_clock.title("Digital Clock")
# window size and x+y i.e. width*height+x+y
digi_clock.geometry("250x120+600+50")
# Make popup window not resizable
digi_clock.resizable(0,0)

# select font from tkinter.font.families()
clock_font = ("Optima", 40, 'bold')
date_font = ("Optima", 20, 'bold')

# choose background and foreground colors using https://www.color-hex.com/
fg_clock = "#57d658"
fg_date = "#26c2e3"
border_width = 2

# Set Label for date and time
date= Label(digi_clock, font=date_font, fg=fg_date, bd=border_width)
date.grid(row=0,column=0)

clock = Label(digi_clock, font=clock_font, fg=fg_clock, bd=border_width)
clock.grid(row=1, column=0)

def digital_clock():
    date_local = time.strftime("%a %d %b %Y")
    time_local = time.strftime("%I:%M:%S %p")
    date.config(text=date_local)
    clock.config(text=time_local)
    clock.after(1000, digital_clock)

digital_clock()
digi_clock.mainloop()

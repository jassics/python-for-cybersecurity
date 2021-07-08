#!/usr/bin/python3
# tkinter is installed already with python. But in case you get moduole not found error. Try this
# MacOS: brew install python-tk
# Ubuntu: sudo apt-get install python3-tk
from tkinter import Label, Tk
import time

clock = Tk()
clock.title("Digital Clock")
clock.geometry("550x80+600+50") # window size and x+y i.e. width*height+x+y
# Make popup window not resiazble
clock.resizable(0,0)

# select font from tkinter.font.families()
text_font= ("Optima", 40, 'bold')

# choose background and foreground colors using https://www.color-hex.com/
background = "#23272a"
foreground = "#57d658"
border_width = 10

label = Label(clock, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=0)

def digital_clock():
    time_local = time.strftime("%a %d %b %Y %I:%M:%S %p")
    label.config(text=time_local)
    label.after(1000, digital_clock)

digital_clock()
clock.mainloop()

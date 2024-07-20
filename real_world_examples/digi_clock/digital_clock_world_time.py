#!/usr/bin/python3
# tkinter is installed already with python. But in case you get module not found error. Try this
# MacOS: brew install python-tk
# Ubuntu: sudo apt-get install python3-tk
# Test tkinter: python3 -m tkinter
from tkinter import Label, Tk
import time
from datetime import datetime
import pytz # pip install pytz

# To get all supported country timezones use this
# time_zones = pytz.all_timezones

country_zones = {'Asia/Kolkata': ['India'],
                 'America/New_York': ['NewYork'],
                 'Europe/Amsterdam': ['Amsterdam'],
                 'Asia/Singapore': ['Singapore'],
                 'Australia/Sydney': ['Sydney']
                 }
country_time_zones = []

for country_zone in country_zones.keys():
    country_time_zones.append(pytz.timezone(country_zone))
    country_zones[country_zone].append(pytz.timezone(country_zone))

digi_clock = Tk()
digi_clock.title("Digital World Time")
# window size and x+y i.e. width*height+x+y
digi_clock.geometry("450x220+600+50")
# Make popup window not resizable
digi_clock.resizable(0,0)

# select font from tkinter.font.families()
clock_font = ("Optima", 22)
date_font = ("Optima", 20, 'bold')

# choose background and foreground colors using https://www.color-hex.com/
fg_clock = "#57d658"
fg_date = "#26c2e3"
border_width = 2

# Set Label for date and time
date= Label(digi_clock, font=date_font, fg=fg_date, bd=border_width)
date.grid(row=0,column=0)

# clock = Label(digi_clock, font=clock_font, fg=fg_clock, bd=border_width)
# clock.grid(row=1, column=0)

def digital_clock():
    count = 1
    date_local = time.strftime("%a %d %b %Y")
    date.config(text=date_local)
    for country_zone in country_zones.keys():
        country_time = datetime.now(country_zones[country_zone][1])
        country_time_fmt = country_time.strftime(f"{country_zones[country_zone][0]}: %I:%M %p (Timezone: %z)")
        clock = Label(digi_clock, font=clock_font, fg=fg_clock, bd=border_width)
        clock.grid(row=count, column=0)
        clock.config(text=country_time_fmt)
        count += 1

    # for country_time_zone in country_time_zones:
    #     country_time = datetime.now(country_time_zone)
    #     country_time_fmt = country_time.strftime(f"{country_zones[country_time_zone]}: %I:%M %p | Timezone: %z")
    #     clock = Label(digi_clock, font=clock_font, fg=fg_clock, bd=border_width)
    #     clock.grid(row=count, column=0)
    #     clock.config(text=country_time_fmt)
    #     count += 1
    clock.after(1000, digital_clock)

digital_clock()
digi_clock.mainloop()

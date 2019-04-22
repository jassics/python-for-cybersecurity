#!/usr/bin/python
# This is the first example from Kunal Chawla's Python Foundation course at udacity.

import time
import webbrowser

total_breaks = 3
break_count  = 0

print("This program started at "+time.ctime() )

while(break_count < total_breaks):
  time.sleep(1800)
  webbrowser.open("http://www.aliencoders.org")
  break_count = break_count + 1


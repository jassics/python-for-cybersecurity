import time
import datetime as dt

# obtain current hour, minute and second from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour

while True:
    print(f'{hr:02d}:{min:02d}:{sec:02d}', end="", flush=True)
    print("\r", end="", flush=True)

    time.sleep(1)
    sec+= 1

    if sec == 60:
        sec = 0
        min+= 1
    if min == 60:
        min = 0
        hr+= 1
    if hr == 24:
        hr = 1



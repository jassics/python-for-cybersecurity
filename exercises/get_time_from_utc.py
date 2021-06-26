#!/usr/bin/python3
# Script to get time when utc timestamp and timezone in timestamp are given

from datetime import datetime

# Thanks to stackoverflow for this snippet
def time_from_utc_with_timezone(utc):
    utc_time = datetime.utcfromtimestamp(utc)
    return utc_time.time()

utc = 1614215239
timezone = 19800

utc_with_tz = utc + timezone
print(time_from_utc_with_timezone(utc_with_tz))

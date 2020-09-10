#!/usr/bin/env python3.6

import time

from time import localtime, strftime, mktime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

# wait for user to stop timer
input("Press 'Enter' to stop timer ")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
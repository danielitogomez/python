#!/usr/bin/env python3

#import libs
import os

#Declare variables
hostname = "localhost" 
response = os.system("ping -c 1 " + hostname)
state_up = " is up"
state_down = " is down"

#and then check the response...
if response == 0:
    print( str(hostname) + str(state_up) )
else:
    print( str(hostname) + str(state_down) )

#!/usr/bin/env python3.6

with open("/home/cloud_user/xmen_file.txt") as file_in:
    
    for line in file_in:
            print(line, end="")
#!/usr/bin/env python3.8

import os
from subprocess import call

proxies = ['test1', 'test2']
USER = ('')
PASS = ('')
ORG = ('')
ENV = ('test')

for file in proxies:
    output = call(['apigeetool', 'deployproxy', '-u', USER, '-p', PASS, '-o', ORG, '-e', ENV, '-n', file, '-d', '.'])
    if output == 'o':
        print("Deploy ok")
    else:
        print("Some Error!")
        exit()

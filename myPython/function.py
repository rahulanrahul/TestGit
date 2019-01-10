'''
Created on 6 Jan 2019

@author: rahulvijayan
'''
def square(x,y):
    return x*x, y*y

t,v = square(2,5)
print(t,v) 

import platform

x = dir(platform)
print(x)

import datetime

x = datetime.datetime.now()
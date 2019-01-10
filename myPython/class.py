'''
Created on 8 Jan 2019

@author: rahulvijayan
'''

import platform
x = platform.system()
print(x)

class Person111:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.kidu = 0

p1 = Person111("John", 36)
p1.kidu = 10

print(p1.name)
print(p1.age)
print(p1.kidu)
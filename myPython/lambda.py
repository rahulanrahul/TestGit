'''
Created on 8 Jan 2019

@author: rahulvijayan
''''''
x = lambda a, b : a + b
print(x(5, 6))


sqroot = lambda a : a * a

y = sqroot(10)

print(y)'''

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
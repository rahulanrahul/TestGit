'''
Created on 2 Jan 2019

@author: rahulvijayan
'''
x = []
print("Enter your name:")
entry = input()
x.append(entry)
print("Enter your Age:")
entry = input()
x.append(entry)
print("Enter your Place:")
entry = input()
x.append(entry)
#x.pop(2)
for i in x:
    print(i+" ",end="")
'''
Created on 3 Jan 2019

@author: rahulvijayan
'''
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "Ford" in thisdict.values():
    print("Yes, 'Ford' is one of the keys in the thisdict dictionary")
a = 4
b = 3  
print("A") if a > b else print("B")

if a > b: print("A ",a," is greater") 
else: print("B ",b," is greater")
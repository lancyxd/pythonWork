#! /usr/bin/python
# -*- coding: utf-8 -*-

import math


#print(math.sqrt(4).is_integer())  #True
#print(math.sqrt(5).is_integer())  #False

def isnum():
   for num in range(10000):
        if math.sqrt((num + 100)).is_integer() and math.sqrt((num + 268)).is_integer():
            print(num)

isnum()



def isnum1():
    for num in range(10000):
        x=int(math.sqrt(num+100))
        y=int(math.sqrt(num+268))
        if (x*x==num+100)and(y*y==num+268):
            print(num)
isnum1()
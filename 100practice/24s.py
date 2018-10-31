#! /usr/bin/python
# -*- coding: utf-8 -*-

from fractions import Fraction
a=1
b=2
sum=0
for i in range(2,21):
    #c=b/a
    c=Fraction(b,a)
    sum+=c
    a,b=b,a+b
    print(c)
print(sum)
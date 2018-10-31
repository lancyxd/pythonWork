#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
完数:一个数洽好等于其因子之和，则称该数为完数
'''

import math
l = [ ]
for n in range (1,1000):
    for a in range (1,n):
        if n%a ==0:
            l.append(a)
    if sum(l)==n:
        print ('l:',l)
        print (n)
    l = []




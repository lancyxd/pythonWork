#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
101~200之间的素数
素数(质数):除了1和本身之外没有其他约数
'''

from math import sqrt
from sys import  stdout

def isprime():
    lst = []
    for i in range(100):  # 建立 101-200 的列表
        lst.append(101 + i)

    for i in range(101, 201):  # 除数为 101-200 这200个数字
        for j in range(2, i):  # 除数为从2至i本身的前一个数字
            if i % j == 0:  # 如果能除尽
                lst.remove(i)  # 则从 lst 列表剔除
                break
    return lst# 剩下的都是素数

lst=isprime()
print(lst,len(lst))




def isprime1():
    h = 0 #统计素数的数目
    leap = 1#素数标识
    for m in range(101, 201):
        k = int(sqrt(m + 1))
        for i in range(2, k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            print(m, end=' ')
            h += 1
        leap = 1
    return h

total=isprime1()
print('\n素数总数目为%d' % total)












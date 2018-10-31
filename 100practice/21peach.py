#! /usr/bin/python
# -*- coding: utf-8 -*-

# 猴子吃桃
from functools import reduce


# FOR循环
# t=1
# for i in range(9,0,-1):
#      t=(t+1)*2
#      print(i,t)
# 推导
# mli=[reduce(lambda x,y:(x+1)*2,range(1,day)) for day in range(11,1,-1)]
# print(list(enumerate(mli)))

s = 1

for i in range(1, 11):
    print(u"现在是第 %d 天，桃子的数目是：%d " % (11 - i, s))
    s = (s + 1) * 2


#! /usr/bin/python
# -*- coding: utf-8 -*-

l=[]
for i in range(3):
    inum=input("请输入一个整数：")
    l.append(int(inum))
l.sort()
print("排序后：",l)


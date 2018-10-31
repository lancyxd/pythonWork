#! /usr/bin/python
# -*- coding: utf-8 -*-

n=int(input("请输入一个数字:"))

def fab(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fab(n-1)

print(fab(n))
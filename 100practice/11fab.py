#! /usr/bin/python
# -*- coding: utf-8 -*-

def fab(n):
    if n<=2:
        num=1
    else:
        num=fab(n-1)+fab(n-2)
    return num

print(fab(4))



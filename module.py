#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys

__author__='Mily'

def test():
    args=sys.argv
    if len(args)==1:
        print("hello word  2222")
    elif len(args)==2:
        print('hello,%s' % args[1])
    else:
        print("too many args")

if __name__=='__main__':
    test()

# python module.py  test1 test2执行命令


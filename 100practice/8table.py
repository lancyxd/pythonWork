#! /usr/bin/python
# -*- coding: utf-8 -*-

print("第1种方式打印9x9:")
def table():
    for i in range(1, 10):
        for j in range(i, 10):
            r = i * j
            print('%d x %d =%-3d' % (i, j, r), end=' ')
        print('  ')

table()


print("第2种方式打印9x9:")
def table1():
    for i in range(1, 10):
        for x in range(1, i + 1):
            print('%d X %d = %2d' % (i, x, i * x), end='  ')
        print('  ')
table1()

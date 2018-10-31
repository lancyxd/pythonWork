#! /usr/bin/python
# -*- coding: utf-8 -*-

def board():
    for i in range(8):
        for j in range(8):
            if (i+j)%2!=0:
                print(chr(219)*2,end='')#因为要连续打印一行，所以不能使用默认的print函数
            else:
                print('  ',end='')
        print('')#打印完了一行之后需要换行

board()




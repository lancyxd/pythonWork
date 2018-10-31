#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
三位数中各个数字立方和等于该数
i=int(153/100)
j=int(153/10)%10
k=153%10
print("各个位上的数字:",i,j,k)
'''


def isdaffodil(num):
    bok=False
    if num<100 or num>999:
        print("请重新输一个有效的三位数")
    else:
        i=int(num/100)
        j=int((num%100)/10)
        k=num%10
        print(i,j,k)
        if i*i*i+j*j*j+k*k*k==num:
            bok=True
    return bok,num


innum=int(input("请输入一个整数:"))
bok,num=isdaffodil(innum)
if bok:
    print("%d 是水仙花数"% num)
else:
    print("%d 不是水仙花数" % num)

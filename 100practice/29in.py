#!/usr/bin/python
#-*-coding:utf-8-*-

n=int(input("请输入一个不多于五位的正整数:"))

a=int(n/10000)
b=int((n%10000)/1000)
c=int((n%1000)/100)
d=int((n%100)/10)
e=n%10

if a!=0:
    print('五位数:',a,b,c,d,e)
elif b!=0:
    print('四位数:', b, c, d, e)
elif c!=0:
    print('三位数:',  c, d, e)
elif d!=0:
    print('二位数:',  d, e)
else:
    print('一位数:',  e)
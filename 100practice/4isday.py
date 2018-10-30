#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
闰年的定义:能被400整除的，或者不能被100整除而能被4整除的年就是闰年。
1)能被100整除，且能被400整除的是闰年
2)其它情况下，能被4整除的是闰年
'''

dat = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
y = int(dat[0:4])  #获取年份
m = int(dat[5:7])  #获取月份
d = int(dat[8:])  #获取日
print(y,m,d)

ly=False
if y%100==0:
    if y%400==0:
        ly=True
    else:
        ly=False
elif y%4==0:
    ly=True
else:
    ly=False

if ly == True:  #若为闰年，则2月份有29天
    ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days=0
for i in  range(1,13):
    if i==m: #i即为所在的月份
        for j in range(1,i-1):
            days+=ms[i]
result=days+d
print('%s是该年中的第%d天。' % (dat, (days + d)))









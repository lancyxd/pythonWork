#! /usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce

count=int(input('请输入要加的数字总数:'))  #将str类型转换为int
num=int(input('请输入第一个数字:'))

'''
sum=a+aa+aaa+....+aaaaaaaa..
'''

def caculate(count,num):
    sum = 0
    for i in range(1, count + 1):
        elem = 0
        for j in range(1, i + 1):
            elem += pow(10, j - 1) * num
        print(elem)
        sum += elem
    return sum

sum=caculate(count,num)
print('求和为：%d'% sum)


print('另一种方式求和>>>>>')
def caculate1(n,a):
    Tn=0
    Sn=[]
    for i in range(n):
        Tn=Tn+a
        a=a*10
        Sn.append(Tn)
        print(Tn)
    print(Sn)
    Sn=reduce(lambda x,y:x+y,Sn)#f=lambda x,y:x+y函数等价于x与y的求和。讲数组Sn的元素相加
    print(Sn)


caculate1(count,num)




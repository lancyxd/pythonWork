#! /usr/bin/python
# -*- coding: utf-8 -*-

n = num = int(input('请输入一个数字：'))  
list = []  # 存放质因数

for j in range(int(num / 2) + 1):  # 判断次数仅需该数字的一半多1次
    for i in range(2, n):
        t = n % i  # i不能是n本身
        if t == 0:  # 若能整除
            list.append(i)  # 则表示i是质因数
            n =int(n / i)   # 除以质因数后的n重新进入判断，注意应用两个除号，使n保持整数
            break  # 找到1个质因数后马上break，防止非质数却可以整除的数字进入质因数列表

if len(list) == 0:  # 若一个质因数也没有
    print('该数字没有任何质因数。')
else:  # 若至少有一个质因数
    list.append(n)  # 此时n已被某个质因数整除过，最后一个n也是其中一个质因数
    list.sort()  # 排下序
    print('%d=%d' % (num, list[0]), end='')
    for i in range(1, len(list)):
        print('*%d' % list[i], end='')
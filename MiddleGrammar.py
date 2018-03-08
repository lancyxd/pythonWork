#! /usr/bin/python
# -*- coding:utf-8 -*-
from  collections import  Iterable
import  os
import  time

#slice
l=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
s=[]
n=len(l)
for i in range(n):
    s.append(l[i])
print(s)
print(s[0:3])
print(s[-2:])#取倒数后两个元素
print('ABCDEF'[:3])

#for
d={'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k,d[k])
for ch in 'ABC':
    print(ch)
for i,value in enumerate(['A','B','C']):
    print(i,value)
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
L=[]
for x in range(1,11):
    if x%2==0:
        L.append(x * x)
print(L)
print([d for d in os.listdir('.')])

print(isinstance('abc',Iterable))#判断str是否可迭代

#生成器
print([x*x for x in range(10)])#list
g=(x*x for x in range(10))#g为迭代器
print(g)
print(g.__next__())
for n in g:
    print('n:',n)

def fib(max):
    n,a,b=0,0,1
    while(n<max):
        print(b)
        a,b=b,a+b
        n=n+1
fib(6)


#函数式编程：允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,6,abs))

#map和reduce
m=map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(m.__next__())

def is_odd(n):
    return n%2==1
f=filter(is_odd,[1,2,3,4,5])
print(f.__next__())

#返回函数sum
def lazy_sum(*args):
    def sum():
        ax=0
        for i in args:
            ax=ax+i
        return  ax
    return  sum
f=lazy_sum(1,2,3,4,5)
print(f())

#闭包，返回函数不要引用任何循环变量，或者后续会发生变化的变量。返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return  i*i
        fs.append(f)
    return  fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


#lambda匿名函数,冒号前面的x表示函数参数
f=lambda x:x*x
print(f(5))
def build(x,y):
    return  lambda :x*x+y*y

def now():
    print('2013-12-25')
now()

#装饰器,装饰器是在函数定义时前面加@，然后跟装饰器的实现函数。
def decorator(func):
    def wrapper():
        start=time.time()
        func()
        print(time.time()-start)
    return wrapper
@decorator
def do_sth():
    for i in range(100000000):
        pass
    print('play game')

do_sth()





















#! /usr/bin/python
# -*- coding: utf-8 -*-
#hello.py
import  math


print ("hello")
print (300+300)
print(3>2)
print(not True)
print(10/3)
print(int(10/3))



#name=input("please input str:")
#print('input:',name)

#字符，\n表示换行，\t表示制表符，r''表示内部字符不需要转义，用'''...'''的格式表示多行内容
print('I\'m OK!')
print('\\\t\\')
print(r'\\\t\\')

print('''line1
line2
line3''')
print("I love 'python'")
print('I love \'python\'') #python中字符串用单引号和双引号均对，三引号主要用于输入多行文本

print(u'中文')#以Unicode表示的字符串用u'...'
print(u'ABC')

#list列表
movies=["the holy grail","the life brian","the meaning of life"]
print(movies)
print (movies[1])
print(movies[-1])
print(len(movies))
movies.append("addelem")
movies.insert(1,'jack')
movies.pop()
movies.pop(1)
movies[1]='replace'
movies[2]=['array1','array2']
print (movies)
print(movies[2][1])


#tuple元组，不可变
classmates=('Michael','Bob','Tracy')
print(classmates)
t=()#空元组
t=(1)
t=(1,)#只有1个元素的tuple定义时必须加一个逗号
print(t)#不是元组，为1这个数
m=('a','b',['x','y'])
m[2][0]='xchange'
print(m)#指向不变

#dict
d={'Michael': 95, 'Bob': 75}
print(d['Bob'])
print(d.get('Bob'))

#set 没有重复的key
s=set([5,4,6])
s.remove(4)
print(s)


#func
print(abs(-20))

def my_abs(x):
    if x>0:
        return  x
    else:
        return  -x
print(my_abs(-30))

#空函数；pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass
def nop():
    pass

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step * math.sin(angle)
    return nx,ny

#把n=2设为默认
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return  s

#可变参数
def cal(numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    return  sum
print(cal([1,2,3]))

#关键字参数
def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',**kw)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


















#! /usr/bin/python
# -*- coding:utf-8 -*-
import types

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_grade(self):
        if self.score>=90:
            return 'A'
        if self.score>=60:
            return 'B'
        else:
            return 'C'

    def print_score(self):
        print(self.name,self.score)


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


#继承和多态
class Animal(object):
    def run(self):
        print('runing')

class Dog(Animal):
    def run(self):
        print('Dog runing')
    def eat(self):
        print('Dog eating')

dog = Dog()
dog.run()
dog.eat()

#类型判断
print(isinstance(dog,Animal))
print(isinstance(123, int))
print(type(123))
print(type(123)==int)

def fn():
    pass
print('true:',type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

#对象的所有属性和方法
print(dir('ABC'))
print('ABC'.__len__())
print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        self.x*self.x

obj=MyObject()
print(obj)
print(hasattr(obj,'x'))
setattr(obj,'y',19)#设置属性
print(obj.y)



#面向对象高级编程
class Student(object):
    def get_score(self):
        return  self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
   # __slots__ = ('name','age')#限制该class实例能添加的属性

s=Student()
s.set_score(60)
print(s.get_score())
s.set_score(999)

#多重继承










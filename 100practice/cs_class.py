#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
#类定义语句的内容通常是函数定义,先执行才能生效。类对象支持两种操作：属性引用和实例化
class ClassName:
    <statement-1>
    .
    <statement-N>

#函数 isinstance() 用于检查实例类型;函数 issubclass() 用于检查类继承：
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    <statement-N>
'''


class  Myclass:
    i=12345
    def f(self):
        return 'hello world'
x=Myclass()

print(x.i)
print(x.f())



class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):
    def update(self, keys,values):
        for item in zip(keys,values):
            self.items_list.append(item)







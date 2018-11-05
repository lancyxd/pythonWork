#! /usr/bin/python
# -*- coding: utf-8 -*-

import json

#把list先序列化，写入到一个文件中
# 两步操作 1步先序列化 列表对象  2步把序列化成的字符串写入文件
list = ['Apple','Huawei','selenium','java','python']
json.dump(list, open('test.txt','w'))
r1=open('test.txt','r')
print(r1.read())

#["Apple", "Huawei", "selenium", "java", "python"]


#两步操作：1、先读取文件的字符串对象；2、然后反序列化成列表对象
res=json.load(open('test.txt','r'))
print (res)
print('数据类型:',type(res))

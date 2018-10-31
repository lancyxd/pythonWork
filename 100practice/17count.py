#! /usr/bin/python
# -*- coding: utf-8 -*-

nspace=0
ndigtal=0
nletter=0
nother=0

instr=input("请输入:")
for i in instr:
    if i.isspace():
        nspace+=1
    elif i.isdigit():
        ndigtal+=1
    elif i.isalpha():
        nletter+=1
    else:
        nother+=1

print("空格数:%d，数字数:%d，字母数:%d，其它数:%d" % (nspace,ndigtal,nletter,nother))


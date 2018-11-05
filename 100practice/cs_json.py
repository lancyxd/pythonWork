#! /usr/bin/python
# -*- coding: utf-8 -*-

import json

class file_open(object):
    f = open('chooes_course.txt', 'r+', encoding='utf-8')

    def write_f(self, info):
        self.info = info
        file_open.f.write(json.dumps(self.info,ensure_ascii=False))
        print(json.dumps(self.info,ensure_ascii=False))

    def read_f(self):
        print(file_open.f.read())

    def __del__(self):
        file_open.f.flush()
        file_open.f.close()


members = {'张三': ['zs123', '56.8'], 'lisi': ['ls123', '47.2'], 'mologa': ['mologa123', '100']}
f1 = file_open()
f1.write_f(members)

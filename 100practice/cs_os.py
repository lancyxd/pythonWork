#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import glob
import sys
import re
import math
import random
from urllib.request import urlopen #互联网模块
from datetime import date
import time
import logging


print(os.getcwd())
#print(os.chdir('E:\#Lancy电子书IT\Python\pythonWork'))
#print(os.system('mkdir today'))

print(dir(os))
#print(help(os))

shutil.copyfile('test.txt', 'test1.txt')
print(glob.glob('*.py'))

print(sys.argv)
#sys.stderr.write('Warning, log file not found starting a new one\n')

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(math.log(1024, 2))
print(random.choice(['apple', 'pear', 'banana']))

for line in urlopen('https://www.hao123.com/'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)


now=date.today() #2018-11-05
print(now.strftime("%y-%m-%d. %Y %b %d is a %A on the %d day of %B."))

t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('[%s ] Warning:config file %s not found' % (t,'server.conf') )
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
# print('[%s]'% t)
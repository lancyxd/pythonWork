#!usr/bin/python
# -*- coding:utf-8 -*-

import logging
'''有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
同理，指定level=WARNING后，debug和info就不起作用了。'''
n=2
logging.basicConfig(level=logging.INFO)
logging.info('n = %d' % n)
#try except finally
#认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print('try:')
    r = 10 / int('a')
    print(r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
finally:
    print('finally')
print('END')


#logging记录错误信息
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)

main()



#抛出错误
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')









#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

#异常处理
def deal_e():
    while True:
        try:
            x=int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again")


def deal_e1():
    try:
        f = open('test.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

#使用 else 子句比在 try 子句中附加代码要好
def deal_e2():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

def custom_e():
    class MyError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    try:
        raise MyError(2 * 2)
    except MyError as e:
        print('My exception occurred, value:', e.value)
    raise MyError('oops!')


def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")
divide(2,3)
divide(2,0)
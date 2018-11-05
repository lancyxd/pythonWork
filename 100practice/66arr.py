#! /usr/bin/python
# -*- coding: utf-8 -*-



def createArr(num):
    arr = []
    for i in range(1, num+1):
        n = int(input('请输入一个数:'))
        arr.append(n)
    return arr

def min(arr):
    min=arr[0]
    for i in range(0,len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min,i

def max(arr):
    max=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>max:
            max=arr[i]
    print(max,i)
    return max,i


if __name__=='__main__':
    num=int(input('请输入数组元素数目:'))
    arr=createArr(num)
    print('before:',arr)
    min,imin=min(arr)
    max,imax=max(arr)
    arr[0],arr[imax]=max,arr[0]
    arr[len(arr)-1],arr[imin]=min,arr[len(arr)-1]
    print('exchange after:',arr)


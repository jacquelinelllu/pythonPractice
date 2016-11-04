#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
  题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

def sortNumber(a,b,c):
    list = [a,b,c]
    list.sort()
    for i in list:
        print i

sortNumber(90,2,56)
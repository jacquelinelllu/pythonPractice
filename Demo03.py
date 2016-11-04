#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

'''
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''

for i in range(1,1000000):
     x = 100+i;
     y = 268+i;
     a = int(math.sqrt(x))
     b = int(math.sqrt(y))
     if a*a == x and b*b==y:
         print "这道题目的答案是%d"%i

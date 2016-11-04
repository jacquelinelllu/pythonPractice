#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
list = [1,2,3,4]

for i in list:
    for j in list:
       for k in list:
           if i!=j and i!=k and j!=k:
               print '%d%d%d'%(i,j,k)
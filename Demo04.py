#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
def getDayForYear(year,month,day):
    result = 0
    mounts = [31,28,31,30,31,30,31,31,30,31,30,31];
    i = 1
    while i<month:
       result+= mounts[i-1]
       i+=1
    result+=day
    if year%4==0 and month>2:
        result+=1
    return result

print getDayForYear(2016,4,1)
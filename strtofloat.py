# -*- coding: utf-8 -*-

from functools import reduce

def fn1(x, y):
    return x*10 + y

def str2float(s):
    n = s.index('.')
    l1 = list(map(int, [x for x in s[:n]]))
    l2 = list(map(int, [x for x in s[n+1:]]))
    return reduce(fn1, l1) + reduce(fn1,l2)/10**len(l2)

print ("(\'123.456\') = ", str2float('123.456'))

# -*- coding: utf-8 -*-

from functools import reduce

def cheng(a, b):
    return a*b

def prod(L):
    return reduce(cheng, L)

print("3*5*7*9 = %d" %(prod([3, 5, 7, 9])))

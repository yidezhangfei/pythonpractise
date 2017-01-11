#-*- coding: utf-8 -*-

L = ['hello', 'world', 18, 'Apple', None]

L2 = [ s.lower() for s in L if (isinstance(s, str))]

print(L2)

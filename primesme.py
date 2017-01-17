# -*- coding: utf-8 -*-

def odd_list():
    n = 1
    while True:
        n = n + 1
        yield n

def not_division(n):
    print (n)
    return True
    # return lambda x : x % n > 0

def primes():
    n = 2
    it = odd_list()
    while True:
        yield n
        n = next(it)
        filter(not_division, it)

for i in primes():
    if i < 1000:
        pass
        # print (i)
    else:
        exit()

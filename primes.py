# -*- coding: utf-8 -*-

def odd_list():
    n = 1
    while True:
        n = n + 2
        yield n

def not_division(n):
    return lambda x : x % n > 0

def primes():
    n = 2
    it = odd_list()
    while True:
        yield n
        n = next(it)
        it = filter(not_division(n), it)

for n in primes():
    if n < 1000:
        print (n)
    else:
        exit()

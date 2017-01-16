# -*- coding: utf-8 -*-

def is_palindrome(n):
    str_n = str(n)
    reverse_str_n = str_n[-1::-1]
    return str_n == reverse_str_n

output = filter(is_palindrome, range(1, 1000))
print (list(output))

# -*- coding: utf-8 -*-

from time import ctime
import functools

def log(logtype='debug'):
    def decorate(func, ascstr=logtype):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            print ('%s: call %s():' % (ascstr, func.__name__))
            print ('call start')
            ret = func(*args, **kargs)
            print ('call end')
        # return func(*args, **kargs)
        return wrapper

    if isinstance(logtype, str):
        return decorate
    elif callable(logtype):
        return decorate(logtype, 'void_call') 

def logg(func):
    def wrapper(*args, **kargs):
        return func(*args, **kargs)
    return wrapper

def logged(func):
    def wrapper(*args, **kargs):
        print ('logged')
        return func(*args, **kargs)
    return wrapper

"""@logged
@logg"""
#@log('debug')
@log
def now():
    return print(ctime())

now()

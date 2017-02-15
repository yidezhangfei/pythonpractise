# coding: utf-8

def coroutine(func):
    def wrapper(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen
    return wrapper

@coroutine
def nature():
    n = 0
    while True:
        if n > 100:
            return n
        yield n
        n += 1

nums = nature()
while True:
    print(nums.send(None))

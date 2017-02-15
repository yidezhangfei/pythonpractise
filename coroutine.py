# coding: utf-8

def consumer():
    r = ''
    while True:
        n = yield r
        if n == '':
            print("wrong param")
        else:
            print("consumer consume %s" % (n))
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("produce %d" % (n))
        r = c.send(n)
        type(r)
        print("consumer return %s" % (r))
    c.close()
    return

c = consumer()
produce(c)

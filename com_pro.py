# python3
# coding: utf-8

def comsumer():
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print ("[comsumer]: comsume %d" % n)
        r = "200 OK"

def produce(comsumer, max):
    n = 1 
    comsumer.send(None)
    while n < max:
        print ("[produce] produce %d" % n)
        r = comsumer.send(n)
        print ("[produce] comsumer return %s" % r)
        n = n + 1

if __name__ == "__main__":
    c = comsumer()
    produce(c, 8)
        
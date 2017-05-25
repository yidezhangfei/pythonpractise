# python3
# coding: utf-8

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1

if __name__ == "__main__":
    for i in fib(10):
        print (i)
# -*- coding: utf-8 -*-

def triangles():
    n = 0
    while True:
        yield list(n)
        n = n + 1
    return "done"

def list(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    elif n > 1 and isinstance(n, int):
        L = []
        for i in range(n+1):
            if i == 0:
                L.append(1)
            elif i == n:
                L.append(1)
            else:
                L.append(list(n-1)[i-1] + list(n-1)[i])
        return L

g_n = 0
for t in triangles():
    print(t)
    g_n = g_n + 1
    if g_n == 10:
        break

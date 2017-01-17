# -*- coding: utf-8 -*-

import os
import sys
import logging

g_result_files = []

def walk(path):
    for f in os.listdir(path):
        next_path = os.path.join(path, f)
        if os.path.isdir(next_path):
            print (next_path)
            walk(next_path)
        elif os.path.isfile(next_path):
            print (next_path)
            g_result_files.append(next_path)

if __name__ == '__main__':
    walk('./test')
    r = sys.argv[1]
    print (g_result_files)
    result = filter(lambda f : f.find(r) != -1, g_result_files)
    print (result)

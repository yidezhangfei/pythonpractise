# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')

print ('       size   last modified  Name')
print ('................................')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    ftime = datetime.fromtimestamp(os.path.getmtime(f))
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' %(fsize, ftime, f, flag))

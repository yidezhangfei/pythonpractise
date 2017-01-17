# -*- coding: utf-8 -*-

import os

pwd = os.path.abspath('.')

for root, dirs, filenames in os.walk(pwd):
    print ('root: %s, dirs: %s, filenames: %s' % (root, dirs, filenames))

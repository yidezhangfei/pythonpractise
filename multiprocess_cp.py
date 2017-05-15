# python3
# coding: utf-8

import os
import sys
import multiprocessing
import shutil

g_exclude_suffixs = [".git", "out"]

def should_exclude(dir):
    should = False
    for suffix in g_exclude_suffixs:
        should = True if dir.find(suffix) != 0 else False
    return should

def recursion_cp(source, target):
    if os.path.exists(target) is False:
        os.mkdir(target)
    dirs_or_files = os.listdir(source)
    for dir_or_file in dirs_or_files:
        abdir_or_file = os.path.join(source, dir_or_file)
        abdir_or_file_target = os.path.join(target, dir_or_file)
        if os.path.isdir(abdir_or_file) and should_exclude(abdir_or_file) is False:
            recursion_cp(abdir_or_file, abdir_or_file_target)
        elif os.path.isfile(abdir_or_file):
            shutil.copy(abdir_or_file, abdir_or_file_target)

def recursion_cp_mp(source, target):
    if os.path.isdir(source) is False:
        raise "not a directory" 
    if os.path.exists(target) is False:
        os.mkdir(target)
    dirs_or_files = os.listdir(source)
    pool = multiprocessing.Pool(5)
    for dir_or_file in dirs_or_files:
        abdir_or_file = os.path.join(source, dir_or_file)
        abdir_or_file_target = os.path.join(target, dir_or_file)
        if os.path.isdir(abdir_or_file) and should_exclude(abdir_or_file) is False:
            pool.apply_async(recursion_cp, (abdir_or_file, abdir_or_file_target))
        elif os.path.isfile(abdir_or_file):
            shutil.copy(abdir_or_file, abdir_or_file_target)

if __name__ == "__main__":
    current_dir = os.getcwd()
    if len(sys.argv) < 3:
        raise "path error"
    else:
        source = os.path.join(current_dir, sys.argv[1])
        target = sys.argv[2]
        recursion_cp_mp(source, target)
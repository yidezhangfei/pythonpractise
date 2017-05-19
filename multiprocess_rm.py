# python3
# coding: utf-8

import os
import sys
import multiprocessing
import stat

g_exclude_suffixs = [".svn"]

def should_exclude(dir):
    should = False 
    for suffix in g_exclude_suffixs:
        should = True if os.path.basename(dir).find(suffix) == 0 else False
        if should is True:
            break
    return should

def recursion_rm(dir):
    dirs_or_files = os.listdir(dir)
    for dir_or_file in dirs_or_files:
        abdir_or_file = os.path.join(dir, dir_or_file)
        if os.path.isdir(abdir_or_file) and should_exclude(abdir_or_file) is False:
            recursion_rm(abdir_or_file)
        elif os.path.isfile(abdir_or_file):
            try:
                if stat.S_IWRITE & os.stat(abdir_or_file).st_mode == 0:
                    print (" file cannot write")
                    os.chmod(abdir_or_file, stat.S_IWRITE)
                os.remove(abdir_or_file)
                print ("remove file: %s" % (abdir_or_file))
            except Exception as e:
                raise e
    try:
        if stat.S_IWRITE & os.stat(dir).st_mode == 0:
            print (" cannot write") 
            s.chmod(dir, stat.S_IWRIT)
        os.rmdir(dir)
        print ("remove dir: %s" % (dir))
    except IOError as e:
        raise e
    return

def recursion_rm_mp(dir):
    if os.path.isdir(dir) is False:
        raise "not a directory"
    dirs_or_files = os.listdir(dir)
    pool = multiprocessing.Pool(5)
    for dir_or_file in dirs_or_files:
        abdir_or_file = os.path.join(dir, dir_or_file)
        if os.path.isdir(abdir_or_file) and should_exclude(abdir_or_file) is False:
            pool.apply_async(recursion_rm, (), dict(dir=abdir_or_file))
        elif os.path.isfile(abdir_or_file):
            try:
                os.remove(abdir_or_file)
                print ("remove file: %s" % (abdir_or_file))
            except IOError as e:
                raise e
    pool.close()
    pool.join()
    try:
        if stat.S_IWRITE & os.stat(dir).st_mode == 0:
            os.chmod(dir, stat.S_IWRITE)
        os.rmdir(dir)
        print ("remove dir: %s" % (dir))
    except IOError as e:
        raise e
    return

if __name__ == "__main__":
    current_dir = os.getcwd()
    dir = current_dir
    if len(sys.argv) >= 2:
        dir = sys.argv[1]
    recursion_rm_mp(dir)
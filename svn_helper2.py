# python3
# coding: utf-8

import os
import sys
import subprocess
from multiprocessing import Pool

g_root = ""
g_exclude_suffix = [".zip"]
g_exclude_dir_ffix = [".git", ".svn"]
g_svn_adddepthempty = "--depth=empty"

g_commands = {"svn": "svn"}
g_op = {"add": "add", "delete": "delete", "commit": "commit", "revert": "revert"}

def walk_and_ex_files(root):
    dirs_or_files = os.listdir(root)
    child = subprocess.Popen([g_commands["svn"], g_op["add"], g_svn_adddepthempty, root], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(child.communicate())
    for dir_or_file in dirs_or_files:
        abdir_or_file = os.path.join(root, dir_or_file)
        if os.path.isdir(abdir_or_file):
            walk_and_ex_files(abdir_or_file)
        elif os.path.isfile(abdir_or_file):
            svn_add(abdir_or_file)
    return

def walk_and_do(root_in, func_in):
    if os.path.abspath(root_in) is False:
        return
    print(root_in, func_in)
    dirs_or_files = os.listdir(root_in)
    for dir_or_file in dirs_or_files:
        addir_or_file = os.path.join(root_in, dir_or_file)
        if os.path.isdir(addir_or_file):
            walk_and_do(addir_or_file, func_in)
        elif os.path.isfile(addir_or_file):
            func_in(addir_or_file)
    func_in(root_in)
    return

def test():
    print ("run here")

def walk_and_do_main(root, func, MP=False):
    if MP is False:
        walk_and_do(root, func)
    else:
        pool = Pool(5)
        dirs_or_files = os.listdir(root)
        for dir_or_file in dirs_or_files:
            addir_of_file = os.path.join(root, dir_or_file)
            if os.path.isdir(addir_of_file):
                pool.apply_async(walk_and_do, (),dict(root_in=addir_of_file, func_in=func))
                #pool.apply_async(test)
            elif os.path.isfile(addir_of_file):
                func(addir_of_file)
        pool.close()
        pool.join()
    return

def svn_add(file):
    child = subprocess.Popen([g_commands["svn"], g_op["add"], file], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(child.communicate())
    return

def svn_commit():
    commit_command = "svn commmit ."
    os.system(commit_command)
    return

def svn_revert(file):
    child = subprocess.Popen([g_commands["svn"], g_op["revert"], file], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(child.communicate())
    return

g_func_op = {"revert": svn_revert}

if __name__ == "__main__":
    current_dir = os.getcwd()
    os.chdir(current_dir)
    op = ""
    mp = False
    if len(sys.argv) >= 2:
        g_root = sys.argv[1]
    if len(sys.argv) >=3:
        op = sys.argv[2]
    if len(sys.argv) >= 4:
        mp = True if sys.argv[3]=="m" else False
    root = current_dir + '/' + g_root
    #walk_and_ex_files(root)
    walk_and_do_main(root, g_func_op[op], MP=mp)
    
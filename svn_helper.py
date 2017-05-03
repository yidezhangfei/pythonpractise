# python3
# coding: utf-8

import os
import sys
import subprocess

g_root = ""
g_exclude_suffix = [".zip"]
g_exclude_dir_ffix = [".git", ".svn"]
g_svn_adddepthempty = "--depth=empty"

g_commands = {"svn": "svn"}
g_op = {"add": "add", "delete": "delete", "commit": "commit"}

def add_sub_dir(root):
    for dirpath, subdirs, files in os.walk(root):
        for subdir in subdirs:
            will_exclude = False
            for dir_ffix in g_exclude_dir_ffix:
                if subdir.find(dir_ffix) != -1:
                    will_exclude = True
            if will_exclude is False:
                walk_and_ex_files(os.path.join(dirpath, subdir))
    return

def walk_and_ex_files(root):
    add_files = []
    for dirpath, dirnames, files in os.walk(root):
        child = subprocess.Popen([g_commands["svn"], g_op["add"], g_svn_adddepthempty, dirpath],
            shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        print(child.communicate())
        for dir in dirnames:
            walk_and_ex_files(os.path.join(dirpath, dir))
        for file in files:
            for suffix in g_exclude_suffix:
                if file.find(suffix) == -1:
                    full_filename = os.path.join(dirpath, file)
                    add_files.append(full_filename)
        svn_add(add_files)
    return

def svn_add(files):
    add_command = "svn add "
    for file in files:
        command = add_command + file;
        #os.system(command)
        child = subprocess.Popen([g_commands["svn"], g_op["add"], file], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        print(child.communicate())
    return

def svn_commit():
    commit_command = "svn commmit ."
    os.system(commit_command)
    return

if __name__ == "__main__":
    current_dir = os.getcwd()
    os.chdir(current_dir)
    if len(sys.argv) >= 2:
        g_root = sys.argv[1]
    root = current_dir + '/' + g_root
    add_sub_dir(root)
    
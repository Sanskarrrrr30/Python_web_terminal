import os
import shutil

def ls(term, *args):
    for item in os.listdir(term.cwd):
        print(item)

def cd(term, *args):
    if not args:
        print("Usage: cd <directory>")
        return
    new_path = os.path.abspath(os.path.join(term.cwd, args[0]))
    if os.path.isdir(new_path):
        term.cwd = new_path
        os.chdir(new_path)
    else:
        print(f"No such directory: {args[0]}")

def pwd(term, *args):
    print(term.cwd)

def mkdir(term, *args):
    if not args:
        print("Usage: mkdir <directory>")
        return
    path = os.path.join(term.cwd, args[0])
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"Directory already exists: {args[0]}")

def rm(term, *args):
    if not args:
        print("Usage: rm <file/folder>")
        return
    target = os.path.join(term.cwd, args[0])
    if os.path.isfile(target):
        os.remove(target)
    elif os.path.isdir(target):
        shutil.rmtree(target)
    else:
        print(f"No such file or directory: {args[0]}")

command_map = {
    "ls": ls,
    "cd": cd,
    "pwd": pwd,
    "mkdir": mkdir,
    "rm": rm,
}

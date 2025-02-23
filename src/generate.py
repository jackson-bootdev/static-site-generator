import os
import shutil
from distutils.dir_util import copy_tree

def clear_directory(path):
    shutil.rmtree(path)
    os.mkdir(path)

def copy_directory(from_path, to_path):
    dir_list = os.listdir(from_path)
    for dir in dir_list:
        fp = os.path.join(from_path, dir)
        tp = os.path.join(to_path, dir)
        if os.path.isfile(fp):
            shutil.copy(fp, tp)
        else:
            os.mkdir(tp)
            copy_directory(fp, tp)
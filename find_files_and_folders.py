import os
import glob
from glob import glob
import pkg_resources

def find_folders(path):
    folders = glob(path)
    return folders 

def find_files(path, extension):
    folders = find_folders(path)
    filesAnnot = []
    for folder in folders: 
        filesAnnot.append(__get_files(folder, extension))
    return filesAnnot

def __get_files(dir_name, extensions):
    '''Helper function to get files in a single directory'''

    # Expand out the directory
    dir_name = os.path.abspath(os.path.expanduser(dir_name))
    myfiles = set()

    for sub_ext in extensions:
        globstr = os.path.join(dir_name, '*' + os.path.extsep + sub_ext)
        myfiles |= set(glob(globstr))

    return myfiles
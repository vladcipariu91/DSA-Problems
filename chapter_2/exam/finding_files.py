"""
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it)
that end with ".c"

    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths

"""
import os
from collections import deque


def find_files(suffix, path):
    q = deque()
    q.appendleft(path)
    c_files = []

    while q:
        path = q.pop()
        print(path)
        content = os.listdir(path)
        for f in content:
            file = os.path.join(path, f)
            if os.path.isfile(file):
                if file.endswith(suffix):
                    c_files.append(file)
            else:
                q.appendleft(file)

    return c_files


print(find_files('.c', './chapter_2/exam/testdir'))

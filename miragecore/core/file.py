"""
Mirage Framework
file.py

Created by Shota Shimazu on 2018/10/21

Copyright (c) 2018-2019 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import os
import shutil
import contextlib


@contextlib.contextmanager
def InDir(path):
    current = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current)


def exists(path):
    return os.path.exists(path)


def copy(from_path, to_path, force = False):
    if os.path.exists(to_path):
        if force:
            shutil.rmtree(to_path)
        else:
            raise FileExistsError
    
    shutil.copytree(from_path, to_path)


def move(from_path, to_path, force = False):
    shutil.move(from_path, to_path)


def mkdir(path):
    os.makedirs(path)


def rm(path):
    if os.path.isdir(path): shutil.rmtree(path)
    if os.path.isfile(path): os.remove(path)


def cwd():
    return os.getcwd()


def cd(path):
    os.chdir(path)

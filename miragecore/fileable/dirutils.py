"""
MIRAGE Console
withdir.py

Created by Shota Shimazu on 2018/06/05

Copyright (c) 2018-2020 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import os
import contextlib

@contextlib.contextmanager
def withDir(path):
    current = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current)

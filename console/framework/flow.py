"""
MIRAGE Console
flow.py

Created by Shota Shimazu on 2018/11/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import os, sys
import importlib
from typing import List


def obj(class_name: callable) -> callable:
    return callable


def module(module_name: str) -> callable:

    new = importlib.import_module(module_name)

    return new.flow.flows

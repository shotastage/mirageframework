"""
MIRAGE Console
flow.py

Created by Shota Shimazu on 2018/10/25

Copyright (c) 2017-2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import sys
import inspect
from typing import List
from console.flows import flows


def collect(module: str):
    modules: List[str] = flows

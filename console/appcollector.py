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

class AppCollector():
    
    modules: List[str]

    def __init__(self):
        self.modules = self._collect_module()

    def _collect_module(self):
        return sys.modules[__name__]

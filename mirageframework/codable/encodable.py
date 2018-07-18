"""
Mirage Framework
encodable.py

Created by Shota Shimazu on 2018/07/18

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from typing import Callable, NoReturn

class Encodable(object):
    
    def __init__(self):
        self._encorder = self.encode
        self._value = None

    def encode(self):
        if self._value is None:
            raise ValueError("Encodable data is empty!")
        else:
            self._encorder()
            raise ValueError("Encode function havn't been overrided!")

    def regist_encorder(self, f: Callable) -> NoReturn:
        self._encorder = f
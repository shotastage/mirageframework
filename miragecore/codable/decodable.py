"""
Mirage Framework
decodable.py

Created by Shota Shimazu on 2018/07/18

Copyright (c) 2018-2020 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from typing import Callable, NoReturn

class Decodable(object):
    
    def __init__(self):
        self._decoder = self.decode

    def decode(self):
        self._decoder()
        raise ValueError("Decode function havn't been overrided!")

    def regist_decorder(self, f: Callable) -> NoReturn:
        self._decoder = f

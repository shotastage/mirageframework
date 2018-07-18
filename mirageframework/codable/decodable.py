"""
Mirage Framework
decodable.py

Created by Shota Shimazu on 2018/07/18

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

class Decodable(object):
    
    def __init__(self):
        self._value = None

    def decode(self):
        if self._value is None:
            raise ValueError("Decoable data is empty!")
        else:
            raise ValueError("Decode function havn't been overrided!")

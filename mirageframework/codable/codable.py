"""
Mirage Framework
codable.py

Created by Shota Shimazu on 2018/07/18

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from .encodable import Encodable
from .decodable import Decodable

class Codable(Encodable, Decodable):

    def __init__(self):
        self._value = None

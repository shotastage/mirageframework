"""
Mirage Framework
encodable.py

Created by Shota Shimazu on 2018/07/18

Copyright (c) 2018-2019 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from typing import Callable, NoReturn
from enum import Enum
from . import json_encorder_decoder


class EncodableFormats(Enum):
    json = "JSON"



class Encodable(object):
    
    def __init__(self):
        self._encorder: Callable = None


    def encode(self, format: EncodableFormats) -> any:
        
        if self._encorder is None:
            
            if format is EncodableFormats.json:
                return json_encorder_decoder.encode(self)

        else:
            self._encorder()

    def regist_encorder(self, f: Callable) -> NoReturn:
        self._encorder = f

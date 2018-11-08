"""
MIRAGE Framework
optional.py

Created by Shota Shimazu on 2018/11/09

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

class Optional():

    def __init__(self, value: any):
        self._value: any = value

    def type_name(self) -> str:
        return type(self._value).__name__

    def unwrap(self) -> any:
        
        if self._value is not None:
            return self._value
        else:
            return None

    def force(self) -> any:
        
        if self._value is not None:
            return self._value
        else:
            raise ValueError("This value contains None.\n Thus, unwrapping optional value has been failed.")


class OptionalF(Optional):

    # TODO: Implement force optional class

    def __new__(cls):
        pass

    def __init__(self, value):
        super().__init__(value)

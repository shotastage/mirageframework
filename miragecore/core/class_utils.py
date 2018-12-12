"""
MIRAGE Framework
class_utils.py

Created by Shota Shimazu on 2018/12/13

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from typing import Type, TypeVar


"""
Final Class Decorotor from https://github.com/moscow-python-beer/final-class

MIT License

Copyright (c) 2017 wemake.services

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
T = TypeVar('T', bound=Type)


def _init_subclass(cls: T, *args, **kwargs) -> None:
    raise TypeError('Subclassing final classes is restricted')


def final(cls: T) -> T:
    """Marks class as `final`, so it won't have any subclasses."""
    setattr(cls, '__init_subclass__', classmethod(_init_subclass))
    return cls



def private():
    pass

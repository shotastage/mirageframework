"""
MIRAGE Console
flow.py

Created by Shota Shimazu on 2018/10/20

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from abc import ABCMeta, abstractmethod
from miragecore.core import *


class Procedure():

    def __init__(self):
        self.procedure_will_run()
        self.procedure_running()
        self.procedure_did_run()


    def procedure_will_run(self) -> Void:
        pass    

    def procedure_running(self) -> Void:
        pass

    def procedure_did_run(self) -> Void:
        pass    

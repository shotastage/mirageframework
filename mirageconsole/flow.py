"""
MIRAGE Console
flow.py

Created by Shota Shimazu on 2018/10/20

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from abc import ABCMeta, abstractmethod
from mirageconsole.core import Void


class Workflow():

    def __init__(self):
        self.workflow_will_run()
        self.workflow_running()
        self.workflow_did_run()


    def workflow_will_run(self) -> Void:
        pass    

    def workflow_running(self) -> Void:
        pass

    def workflow_did_run(self) -> Void:
        pass    

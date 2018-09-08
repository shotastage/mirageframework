"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from abc import ABCMeta, abstractmethod
from mirageconsole.core import Void
from mirageconsole import system as mys



class Workflow():

    def __init__(self, parser) -> Void:
        self.init()

    def main(self) -> bool:
        # Main flow struct
        return True

    def run(self) -> Void:
        self.main()

        # Flow
        for flow in self.Stepflows:
            try:
                flow.run()
            except:
                raise Exception


class Action():

    def __init__(self, where) -> Void:
        
        if where:
            self.script()
    

    def script(self): pass

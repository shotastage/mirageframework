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

import platform
import tempfile, sys, traceback
from functools import lru_cache
from urllib import request
from console.proj import InDir
from console.framework import Procedure
from miragecore.core.types import *
from console.version import __version__ as ver
from console import system as mys




class SystemCheckFlow(Procedure):

    def main(self) -> Void:
        mys.log("Checking system information...")

        if self.get_os() == "Darwin":
            print("OS: macOS")
        elif self.get_os() == "Windows":
            print("OS: Windows")
        elif self.get_os() == "Linux":
            print("OS: Linux")

        print(
            "Python: ",
            self.get_python_version()[0], ".",
            self.get_python_version()[1], ".",
            self.get_python_version()[2]
        )

    def remaining_disk():
        pass

    @lru_cache(maxsize = 100)
    def get_os(self) -> str:
       return  platform.system()


    @lru_cache(maxsize = 100)
    def get_python_version(self) -> tuple:
        return platform.python_version_tuple()

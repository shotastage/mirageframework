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

import sys
import enum
import functools

from typing import List
from mirageconsole import system
from mirageconsole.core import *


class CommandActionStore(object):

    def __init__(self, cmd: str, subcmd: str, target: str, option: str, flow: callable) -> Void:
        # Default action is below.
        # mgc no-action:void test --detail [empty list]

        self._command = cmd
        self._subcommand = subcmd
        self._target_name = target
        self._command_option = option
        self._flow = flow

        # Status
        self.is_assessmented = False



class ArgumentsParser(object):

    def __init__(self) -> Void:
        self._action_stack: List[CommandActionStore] = []
        self._arguments: List[str] = []

        self._command = self._command_parser(sys.argv[1])
        self._subcommand = self._subcommand_parser(sys.argv[1])
        self._target_name = sys.argv[2]
        self._command_option = sys.argv[3]

    
    def add_argument(self, command: str, subcommand: str, target: str, detail: str, flow) -> Void:
        self._action_stack.append(
            CommandActionStore(
                cmd = command,
                subcmd = subcommand,
                target = target,
                option = detail,
                flow = flow
            )
        )


    def parse(self) -> Void:
        pass


    def _command_parser(self, cmd: str) -> str:

        if ":" in cmd:
            return cmd.split(":")[0]
        else:
            return cmd

    
    def _subcommand_parser(self, cmd: str) -> str:

        if ":" in cmd:
            return cmd.split(":")[1]
        else:
            return ""

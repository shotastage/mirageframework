"""
MIRAGE Console
mgargparse.py

Created by Shota Shimazu on 2018/09/06

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import sys
import enum
import functools

from typing import List
from miragecore.core.types import *


class CommandActionStore(object):

    def __init__(self, cmd: str, sub: str, target: str, option: str, flow: callable = None) -> Void:
        # Default action is below.
        # mgc no-action:void test --detail [empty list]
        # ex. mgc new:react proj_name --typescript

        self._command = cmd
        self._subcommand = sub
        self._target_name = target
        self._command_option = option
        self._flow = flow


class ArgumentsParser(object):

    def __init__(self) -> Void:
        self._action_stack: List[CommandActionStore] = []
        self._arguments: List[str] = []
        self._given_action = self._get_given_action()

    
    def add_argument(self, command: str, subcommand: str, target: str, detail: str, flow) -> Void:
        self._action_stack.append(
            CommandActionStore(
                cmd = command,
                sub = subcommand,
                target = target,
                option = detail,
                flow = flow
            )
        )


    def parse(self) -> Void:

        for action in self._action_stack:
            if self._given_action == action:
                action._flow()
                print("Action has been executed.")

                return
        
        print("Your command is not found.")



    def _get_given_action(self) -> CommandActionStore:

        try:
            target = sys.argv[2]
        except:
            target = None

        try:
            option = sys.argv[3]
        except:
            option = None

        return CommandActionStore(
            cmd = self._command_parser(sys.argv[1]),
            sub = self._subcommand_parser(sys.argv[1]),
            target = target,
            option = option
        )



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

    def _parse_detail_option(self, option: str) -> str:
        return ""

"""
MIRAGE Console
procedures.py

Created by Shota Shimazu on 2018/11/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from miragecore import core
from console.framework import Procedure
from console.help import description, description_long
from console import version


class UsageShowProcedure(Procedure):

    def procedure_running(self):
        super().procedure_running()



class VersionShowProcedure(Procedure):

    def procedure_running(self):
        super().procedure_running()
        print(version.__version__)

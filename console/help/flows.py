"""
MIRAGE Console
flow.py

Created by Shota Shimazu on 2018/11/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from console.framework.flow import obj
from console.help.procedures import (
    UsageShowProcedure,
    VersionShowProcedure
)

flows = (
    obj(UsageShowProcedure),
    obj(VersionShowProcedure),
)

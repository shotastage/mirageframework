"""
MIRAGE Console
logger.py

Created by Shota Shimazu on 2018/11/21

Copyright (c) 2017-2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""


import sys


def log(string,
            withError = False, errorDetail = None,
            withInput = False, withConfirm = False, default = None):


    if withError:

        print('\033[31mMIRAGE: ' + str(string) + '\033[0m')

        if not errorDetail == None:
            separator_begin = "===== Error Detail =========================================================\n"
            separator_end   = "============================================================================\n"
            print('\033[31m' + separator_begin + errorDetail + "\n" + separator_end + '\033[0m')


    elif withInput:
        string = str(input('\033[32m' + str(string) + ' >> \033[0m'))

        if string == "" and default != None:
            return default
        else:
            return string

    elif withConfirm:
        print('\033[31mMIRAGE: ' + str(string) + '\033[0m')

        while True:
            answer = input('\033[32m' + "Please respond with yes or no [Y/N/y/n]" + ' >> \033[0m').lower()

            if answer in [ "y", "Y", "yes", "Yes", "YES", "Yeah"]:
                return True
            elif answer in [ "n", "N", "no", "No", "NO", "Nope"]:
                return False

    else:
        print('\033[32mMIRAGE: \033[0m' + str(string))

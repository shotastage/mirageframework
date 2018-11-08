import os, sys

class Path():

    # Path
    path: str


    def __init__(self, path: str = None):

        if path is not None:
            self.path = os.environ['HOME']
        else:
            self.path = path

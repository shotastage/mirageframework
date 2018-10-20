import os
import contextlib


@contextlib.contextmanager
def InDir(path):
    current = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current)

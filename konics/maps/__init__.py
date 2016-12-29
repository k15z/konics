from os import path
from glob import glob

__all__ = []
for file in glob(path.dirname(path.abspath(__file__)) + "/*.py"):
    if "__init__" not in file:
        __all__.append(path.basename(file)[:-3])
MAP_IDS = __all__

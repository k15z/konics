from os import path
from glob import glob

MAP_IDS = []
for file in glob(path.dirname(path.abspath(__file__)) + "/*.py"):
    if "__init__" not in file:
        map_id = path.basename(file)[:-3]
        exec("from . import " + map_id)
        MAP_IDS.append(map_id)

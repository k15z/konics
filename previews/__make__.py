import sys
from os import path
MY_DIR = path.dirname(path.abspath(__file__))
sys.path.insert(0, path.abspath(MY_DIR + '/..'))

import konics.maps
from konics.core import *
from konics.utils import *
from scipy.misc import imsave

for map_id in konics.maps.MAP_IDS:
    print(map_id)
    exec("import konics.maps." + map_id)
    item = getattr(konics.maps, map_id)

    world = World()
    track = Track(item.x_t, item.y_t, item.e_t)
    track.add_to(world)

    drive = Drive(world)
    drive.set_pose(track.get_pose(0.0))

    imsave(MY_DIR + "/" + map_id + ".track.png", make_preview(track, world, title=map_id))
    imsave(MY_DIR + "/" + map_id + ".world.png", drive.render())

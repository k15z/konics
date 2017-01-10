import sys
from os import path
MY_DIR = path.dirname(path.abspath(__file__))
sys.path.insert(0, path.abspath(MY_DIR + '/..'))

from tqdm import tqdm
from konics.maps import *
from konics.core import *
from konics.utils import *
from scipy.misc import imsave

world, track = make_wt("kilo")
drive = Drive(world)
for t in tqdm(range(100)):
    drive.set_pose(track.get_pose(t / 100.0))
    drive.render()

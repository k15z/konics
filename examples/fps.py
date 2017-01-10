import sys
from os import path
from tqdm import tqdm
from random import choice
MY_DIR = path.dirname(path.abspath(__file__))
sys.path.insert(0, path.abspath(MY_DIR + '/..'))

from konics.maps import *
from konics.core import *
from konics.utils import *
from scipy.misc import imsave

world, track = make_wt(choice(MAP_IDS))
drive = Drive(world)
for t in tqdm(range(1000)):
    drive.set_pose(track.get_pose(t / 100.0))
    drive.render()

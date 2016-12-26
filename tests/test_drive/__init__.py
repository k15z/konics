import os
import sys
import math
import unittest
sys.path.insert(0, os.path.abspath('..'))

from konics import *
from scipy.misc import imsave

def please_check(to_check, make_sure):
    print(" ".join(["Please check", to_check, "and make sure", make_sure]))

class TestDrive(unittest.TestCase):

    def test_0(self):
        track = Track(sky=choice(SKY_TEXTURES), ground=choice(GROUND_TEXTURES))
        for i in range(3):
            track.add(Cone(-10, 20*i))
            track.add(Cone( 10, 20*i))
        track.add(Cone(-15, 40, 0.0))
        track.add(Cone( 15, 40, math.pi))

        race = Drive(track)
        imsave("_output/track_0.png", race.render())
        race.forward()
        imsave("_output/track_1.png", race.render())
        race.rotate(0.1)
        imsave("_output/track_2.png", race.render())

        please_check("_output/track_N.png", "0, 1, and 2 show the car moving forwards and turning left.")

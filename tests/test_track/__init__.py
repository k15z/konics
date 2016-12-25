import os
import sys
import math
import unittest
sys.path.insert(0, os.path.abspath('..'))

from konics import *
from scipy.misc import imsave

def please_check(to_check, make_sure):
    print(" ".join(["Please check", to_check, "and make sure", make_sure]))

class TestTrack(unittest.TestCase):

    def test_shape(self):
        track = Track(size=128)
        self.assertEqual(track.render((0,0), (0,1)).shape, (128, 128, 3))

        track = Track(size=512)
        self.assertEqual(track.render((0,0), (0,1)).shape, (512, 512, 3))

    def test_look_at(self):
        track = Track()
        track.add(Cone(0, 20))

        image = track.render((0,0), (0,1))
        imsave("_output/one_cone.png", image)
        please_check("_output/one_cone.png", "you see one cone.")

        image = track.render((0,0), (0,-1))
        imsave("_output/no_cones.png", image)
        please_check("_output/no_cones.png", "you see no cones.")

    def test_left_cone(self):
        track = Track()
        track.add(Cone(0, 20, math.pi))

        image = track.render((0,0), (0,1))
        imsave("_output/left_cone.png", image)
        please_check("_output/left_cone.png", "the cone points left.")

    def test_right_cone(self):
        track = Track()
        track.add(Cone(0, 20, 0.0))
        
        image = track.render((0,0), (0,1))
        imsave("_output/right_cone.png", image)
        please_check("_output/right_cone.png", "the cone points right.")

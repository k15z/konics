import os
import sys
import math
import unittest
sys.path.insert(0, os.path.abspath('..'))

from konics import *
from scipy.misc import imsave

def please_check(to_check, make_sure):
    print(" ".join(["Please check", to_check, "and make sure", make_sure]))

def x_t(t):
    if t > 4:
        return x_t(4) + t
    return np.sin(t)*100

def y_t(t):
    if t > 4:
        return y_t(4) + t
    return np.cos(t)*100 - 100

class TestParametrics(unittest.TestCase):

    def test_start_pos(self):
        self.assertEqual(start_pos(x_t, y_t), (0, 0, 0))

    def test_make_track(self):
        drive = Drive(make_track(x_t, y_t, 40.0))
        drive.position = (0, 0, 0)
        imsave("_output/parametrics.png", drive.render())
        please_check("_output/parametrics.png", "make sure the path curves to the right.")

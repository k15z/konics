import numpy as np
from random import random
from math import atan2, sqrt, pi

Z_HAT = np.array([0.0, 0.0, 1.0])
P_MISSING_CONE = 0.2
VEHICLE_WIDTH = 10.0 + random() * 5.0
CONE_DISTANCE = 15.0 + random() * 5.0

def D(f_t, t, eps=1e-3):
    return (f_t(t + eps) - f_t(t - eps)) / (2.0 * eps)

def M(f_t, s_t, e_t, res=10000):
    best, best_t = f_t(s_t), s_t
    for t in np.linspace(s_t, e_t, num=res):
        if f_t(t) < best:
            best_t = t
            best = f_t(t)
    return t, best

class Track:
    
    def __init__(self, x_t, y_t, e_t):
        self.x_t = x_t
        self.y_t = y_t
        self.e_t = e_t

    def get_pose(self, t):
        x, y, a, _, _ = self.get_full_pose(t)
        return x, y, a

    def get_full_pose(self, t):
        x, y = self.x_t(t), self.y_t(t)
        dx, dy = D(self.x_t, t), D(self.y_t, t)
        return x, y, atan2(dy, dx), dx, dy

    def add_to(self, world):
        left_cone = (0.0, 0.0)
        right_cone = (0.0, 0.0)
        for t in np.linspace(0.0, self.e_t, num=10000):
            x, y, a, dx, dy = self.get_full_pose(t)
            normal = np.cross(np.array([dx, dy, 0]), Z_HAT)
            dx, dy, _ = normal / np.linalg.norm(normal) * VEHICLE_WIDTH

            left = True
            if abs(x + dx - left_cone[0]) < CONE_DISTANCE:
                if abs(y + dy - left_cone[1]) < CONE_DISTANCE:
                    left = False
            if left:
                left_cone = (x + dx, y + dy)
                if random() > P_MISSING_CONE:
                    world.add_cone(x + dx, y + dy)

            right = True
            if abs(x - dx - right_cone[0]) < CONE_DISTANCE:
                if abs(y - dy - right_cone[1]) < CONE_DISTANCE:
                    right = False
            if right:
                right_cone = (x - dx, y - dy)
                if random() > P_MISSING_CONE:
                    world.add_cone(x - dx, y - dy)

    def evaluate(self, pose):
        x, y, a = pose
        def distance(t):
            return sqrt((self.x_t(t) - x) ** 2 + (self.y_t(t) - y) ** 2)
        t, d = M(distance, 0.0, self.e_t)
        _, _, aa = self.get_pose(t)
        print(a, aa)
        on_track = True if d < VEHICLE_WIDTH else False
        right_dir = True if abs(aa - a) < pi / 2.0 else False
        return on_track, right_dir

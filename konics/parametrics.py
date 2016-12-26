import math
import random
import numpy as np
from random import choice
from . import Track, Cone, SKY_TEXTURES, GROUND_TEXTURES

P_MISSING_CONE = 0.2
CONE_DISTANCE = 10.0 + random.random() * 5.0
VEHICLE_WIDTH = 20.0 + random.random() * 5.0

def d(f_t, t, eps=1e-3):
    """
    Numerical approx. of derivative.
    """
    delta = f_t(t + eps) - f_t(t - eps)
    return delta / (2.0 * eps)

def start_pos(x_t, y_t):
    return pos_at_time(x_t, y_t, 0)

def pos_at_time(x_t, y_t, t):
    """
    Get the optimal position/direction at a given "time".
    """
    x, y = x_t(t), y_t(t)
    a = math.atan2(d(y_t, t), d(x_t, t))
    return x, y, a

def make_track(x_t, y_t, end_time, random_textures=True):
    """
    Return a track which follows the given parametric equations from time 0 to 
    time `end_time`. Note that the idea of `time` used here is different from 
    the amount of time actually required to drive through the track.
    """
    track = Track(sky=choice(SKY_TEXTURES), ground=choice(GROUND_TEXTURES))
    if not random_textures:
        track = Track()

    timesteps = np.linspace(0.0, end_time, num=1000)
    x = [x_t(t) for t in timesteps]
    y = [y_t(t) for t in timesteps]

    cx = []
    cy = []
    for t in timesteps:
        dx, dy = d(x_t, t), d(y_t, t)
        normal = np.cross(np.array([dx, dy, 0]), np.array([0,0,1]))
        dx, dy, _ = normal / np.linalg.norm(normal) * (VEHICLE_WIDTH / 2.0)

        # add on left and right
        for i in [1.0, -1.0]:
            # make sure the cones are spaced out by at least CONE_DISTANCE units
            if len(cx) > 0 and abs(x_t(t) + i*dx - cx[-1]) < CONE_DISTANCE:
                if len(cy) > 0 and abs(y_t(t) + i*dy - cy[-1]) < CONE_DISTANCE:
                    continue
            if len(cx) > 1 and abs(x_t(t) + i*dx - cx[-2]) < CONE_DISTANCE:
                if len(cy) > 1 and abs(y_t(t) + i*dy - cy[-2]) < CONE_DISTANCE:
                    continue

            # randomly drop some cones
            if random.random() < P_MISSING_CONE:
                continue

            cx.append(x_t(t) + i*dx)
            cy.append(y_t(t) + i*dy)
            track.add(Cone(cx[-1], cy[-1]))

    return track

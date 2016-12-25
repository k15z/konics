import math
import random
import numpy as np
from . import Track, Cone

def d(f_t, t, eps=1e-3):
    dy = f_t(t + eps) - f_t(t - eps)
    dx = 2.0 * eps
    return dy / dx

def start_pos(x_t, y_t):
    x, y = x_t(0), y_t(0)
    a = math.atan2(d(y_t, 0), d(x_t, 0))
    return x, y, a

def make_track(x_t, y_t, end_time):
    track = Track()

    timesteps = np.linspace(0.0, end_time, num=1000)
    x = [x_t(t) for t in timesteps]
    y = [y_t(t) for t in timesteps]

    cx = []
    cy = []
    for t in timesteps:
        dx, dy = d(x_t, t), d(y_t, t)
        normal = np.cross(np.array([dx, dy, 0]), np.array([0,0,1]))
        dx, dy, _ = 10.0 * normal / np.linalg.norm(normal)

        if random.random() < 0.1:
            continue
        for i in [1.0, -1.0]:
            if len(cx) > 0 and abs(x_t(t) + i*dx - cx[-1]) < 5.0:
                if len(cy) > 0 and abs(y_t(t) + i*dy - cy[-1]) < 5.0:
                    continue
            cx.append(x_t(t) + i*dx)
            cy.append(y_t(t) + i*dy)
            track.add(Cone(cx[-1], cy[-1]))

    return track

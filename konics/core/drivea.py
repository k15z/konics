from random import choice
from math import pi, tan, cos, sin

PI = pi
TAU = 2.0 * pi
WHEEL_BASE_METERS = 1.0
FRAMES_PER_SECOND = 10.0
SECONDS_PER_FRAME = 1.0 / FRAMES_PER_SECOND

def awrap(a):
    while a < 0: a += TAU
    while a > TAU: a -= TAU
    return a

def ackerman(x, y, a, v, s):
    if s == 0:
        nx = x + cos(a)
        ny = y + sin(a)
        return nx, ny, a

    circle_angle = awrap(a + PI/2.0)
    circle_init_angle = awrap(a - PI/2.0)
    circle_radius = WHEEL_BASE_METERS / tan(s)
    circle_x = x + cos(circle_angle) * circle_radius
    circle_y = y + sin(circle_angle) * circle_radius

    travel_distance = v * SECONDS_PER_FRAME
    travel_angle = travel_distance / circle_radius
    circle_final_angle = awrap(circle_init_angle + travel_angle)

    na = a + travel_angle
    nx = circle_x + cos(circle_final_angle) * circle_radius
    ny = circle_y + sin(circle_final_angle) * circle_radius

    return nx, ny, na

class Drive:

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.a = 0.0
        self.v = 1.0
        self.s = 0.0

    def _normalize(self):
        self.a = awrap(self.a)
        self.s = awrap(self.s)

    def step(self):
        self._normalize()
        x, y, a, v, s = self.x, self.y, self.a, self.v, self.s
        self.x, self.y, self.a = ackerman(x, y, a, v, s)

    def velocity(self, dv):
        self.v += dv

    def steering(self, ds):
        self.s += ds

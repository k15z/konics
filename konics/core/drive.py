from math import pi, cos, sin

TAU = 2*pi

class Drive:
    
    SPEED = 5.0

    def __init__(self, world):
        self.world = world
        self.pose = (0.0, 0.0, 0.0)

    def _validate_pose(self):
        x, y, a = self.pose
        while a < 0.0: a += TAU
        while a > TAU: a -= TAU
        self.pose = (x, y, a)

    def render(self):
        return self.world.render(self.pose)

    def set_pose(self, pose):
        self.pose = pose
        self._validate_pose()

    def move(self, rotation=0.0):
        x, y, a = self.pose
        a += rotation
        x = x + cos(a) * Drive.SPEED
        y = y + sin(a) * Drive.SPEED
        self.pose = (x, y, a)
        self._validate_pose()

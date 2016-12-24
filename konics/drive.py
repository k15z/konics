import math

DRIVE_SPEED = 5.0

class Drive:
    def __init__(self, track):
        self.track = track
        self.position = (0.0, 0.0, math.pi/2.0)

    def render(self):
        """
        return a picture of what "you" see
        """
        x, y, a = self.position
        look_at = (x+math.cos(a), y+math.sin(a))
        return self.track.render((x, y), look_at)

    def forward(self):
        """
        move forward by DRIVE_SPEED units
        """
        x, y, a = self.position
        x = x + math.cos(a) * DRIVE_SPEED
        y = y + math.sin(a) * DRIVE_SPEED
        self.position = (x, y, a)

    def rotate(self, da=0.0):
        """
        rotate `da` radians from the current angle
        """
        x, y, a = self.position
        a += da
        self.position = (x, y, a)

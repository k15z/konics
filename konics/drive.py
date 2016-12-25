import math

class Drive:
    SPEED = 2.5

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
        move forward by Drive.SPEED units
        """
        x, y, a = self.position
        x = x + math.cos(a) * Drive.SPEED
        y = y + math.sin(a) * Drive.SPEED
        self.position = (x, y, a)

    def rotate(self, da=0.0):
        """
        rotate `da` radians from the current angle
        """
        x, y, a = self.position
        a += da
        while a < 0.0: a += math.pi*2
        while a > math.pi*2: a -= math.pi*2
        self.position = (x, y, a)

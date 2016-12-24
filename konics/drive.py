import math

class Drive:
    def __init__(self, track):
        self.speed = 5.0
        self.track = track
        self.position = (0.0, 0.0, math.pi/2.0)

    def render(self):
        x, y, a = self.position
        look_at = (x+math.cos(a), y+math.sin(a))
        return self.track.render((x, y), look_at)

    def forward(self):
        x, y, a = self.position
        x = x + math.cos(a)*self.speed
        y = y + math.sin(a)*self.speed
        self.position = (x, y, a)

    def rotate(self, da=0.0):
        x, y, a = self.position
        a += da
        self.position = (x, y, a)

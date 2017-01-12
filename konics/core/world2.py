import requests
from io import BytesIO
from scipy.misc import imread, imsave

class World:
    
    def __init__(self):
        self.cones = []
        self.cones2 = []

    def add_cone(self, x, y):
        self.cones.append((x, y, 0.0))
        self.cones2.append({"x":x,"y":y})

    def render(self, pose):
        while True:
            try:
                url = "http://localhost:3000/"
                pose = (pose[0], pose[1], pose[2])
                payload = {"cones": self.cones2, "pose": pose}
                response = requests.post(url, json=payload)
                return imread(BytesIO(response.content))
            except:
                print("Warning: rendering server offline. Retrying...")

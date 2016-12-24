import os
import math
import platform
import subprocess
from io import BytesIO
from scipy.misc import imread

BINARY = "povray"
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

if platform.system() == "Darwin":
    BINARY = "./povray_osx"

class Track:
    def __init__(self, size=128):
        self.cones = []
        self.size = size

    def add(self, cone):
        self.cones.append(cone)

    def render(self, loc, at):
        with open(DATA_DIR + "/tmp.pov", "wt") as fout:
            pov = """#include "textures.inc"
    #declare White   = rgb 1;
    #declare Orange = color red 1 green 0.5 blue 0.0;
    #declare OrangeRed = color red 1.0 green 0.25; 

    camera {
        perspective
        location <""" + str(loc[0]) + """, 8, """ + str(loc[1]) + """>
        look_at  <""" + str(at[0]) + """, 8, """ + str(at[1]) + """>
        right x
        up y
    }

    light_source {
        <0, 100, 0> color White
    }
    sphere{<0,0,0>,1 hollow
    texture{Shadow_Clouds}
     scale 10000
    }
    plane{ <0,1,0>, 0 
           texture{ pigment{color rgb<0.05,0.05,0.05>}
                    normal {bumps 0.75 scale 0.015}
                  } // end of texture
     } // end of plane
    """
            for cone in self.cones:
                pov += cone.compile()
            fout.write(pov)
        cmd = [BINARY, "tmp.pov", "+W"+str(self.size), "+H"+str(self.size), "-GA", "-o-"]
        result = subprocess.check_output(cmd, cwd=DATA_DIR, stderr=open(os.devnull, 'w'))
        return imread(BytesIO(result))

class Cone:
    def __init__(self, x, y, a=None):
        self.x, self.y, self.a = x, y, a

    def compile(self):
        x, y, a = self.x, self.y, self.a
        if a == None:
            return """cone {
                <""" + str(x) + """, 4, """ + str(y) + """>, 0.1
                <""" + str(x) + """, 0, """ + str(y) + """>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }"""
        else:
            a = 2.0 * math.pi * a / 360.0
            tip_x, tip_y = x + math.cos(a)*2, y + math.sin(a)*2
            base_x, base_y = x - math.cos(a)*2, y - math.sin(a)*2
            return """cone {
                <""" + str(tip_x) + """, 0, """ + str(tip_y) + """>, 0.1
                <""" + str(base_x) + """, 1, """ + str(base_y) + """>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }"""

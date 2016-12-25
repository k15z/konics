import os
import platform
import subprocess
from io import BytesIO
from scipy.misc import imread

SHELL = False
BINARY = "povray"
EXTRA_FLAGS = []
if platform.system() == "Darwin":
    BINARY = "./povray_osx"
if platform.system() == "Windows":
    SHELL = True
    BINARY = 'povray.exe'
    EXTRA_FLAGS = ["+FS"]

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/bin"
SKY_TEXTURES = ["Blue_Sky", "Blood_Sky", "Apocalypse", "Clouds", "FBM_Clouds", "Shadow_Clouds", "Starfield"]
GROUND_TEXTURES = ["Asphalt", "Brown_Agate", "White_Marble"]

class Track:
    def __init__(self, size=256, sky="Shadow_Clouds", ground="Asphalt"):
        self.cones = []
        self.size = size
        self.sky = sky
        self.ground = ground

    def add(self, cone):
        self.cones.append(cone)

    def render(self, loc, at):
        with open(DATA_DIR + "/track.pov", "wt") as fout:
            pov = """#include "textures.inc"

    #declare White   = rgb 1;
    #declare Orange = color red 1 green 0.5 blue 0.0;
    #declare OrangeRed = color red 1.0 green 0.25; 
    #declare Asphalt = texture{
        pigment{color rgb<0.05,0.05,0.05>}
        normal {bumps 0.75 scale 0.015}
    }

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
    texture{""" + self.sky + """}
     scale 10000
    }
    plane{ <0,1,0>, 0 
           texture{""" + self.ground + """}
     } // end of plane
    """
            for cone in self.cones:
                pov += cone.compile()
            fout.write(pov)
        cmd = [BINARY, "track.pov", "+W"+str(self.size), "+H"+str(self.size), "-GA", "-o-"] + EXTRA_FLAGS
        devnull = open(os.devnull, 'w')
        result = subprocess.check_output(cmd, cwd=DATA_DIR, stderr=devnull, shell=SHELL)
        devnull.close()
        result = BytesIO(result)
        result.seek(0)
        return imread(result)

    def set_size(self, size):
        self.size = size

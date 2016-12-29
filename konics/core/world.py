from io import BytesIO
from uuid import uuid4
from random import choice
from math import sin, cos
from platform import system
from scipy.misc import imread
from subprocess import check_output
from os import path, remove, devnull

SHELL = False
BINARY = "povray"
EXTRA_FLAGS = []
if system() == "Darwin":
    BINARY = "./povray_osx"
if system() == "Windows":
    SHELL = True
    BINARY = 'povray.exe'
    EXTRA_FLAGS = ["+FS"]

DATA_DIR = path.dirname(path.abspath(__file__)) + "/bin"
SKY_TEXTURES = ["Blue_Sky", "Apocalypse", "Clouds", "Shadow_Clouds", "Starfield"]
GROUND_TEXTURES = ["Asphalt", "White_Marble"]

class World:
    
    def __init__(self):
        self.cones = []
        self.sky = "Shadow_Clouds"
        self.ground = "Asphalt"
        if system() != "Windows":
            self.sky = choice(SKY_TEXTURES)
            self.ground = choice(GROUND_TEXTURES)

    def set_sky(self, sky):
        assert sky in SKY_TEXTURES
        self.sky = sky

    def set_ground(self, ground):
        assert ground in GROUND_TEXTURES
        self.sky = sky

    def add_cone(self, x, y, a=None):
        self.cones.append((x, y, a))

    def render(self, pose):
        x, y, a = pose
        fname = str(uuid4()) + ".pov"
        with open(DATA_DIR + "/" + fname, "wt") as fout:
            fout.write(self._compile(x, y, a))
        with open(devnull, 'w') as devout:
            cmd = [BINARY, fname, "+W256", "+H256", "-GA", "-o-"] + EXTRA_FLAGS
            result = BytesIO(check_output(cmd, cwd=DATA_DIR, stderr=devout, shell=SHELL))
            result.seek(0)
        remove(DATA_DIR + "/" + fname)
        return imread(result)

    def _compile(self, x, y, a):
        my_x, my_y = x, y
        at_x = my_x + cos(a)
        at_y = my_y + sin(a)
        pov = """
            #include "textures.inc"
            #declare White   = rgb 1;
            #declare Orange = color red 1 green 0.5 blue 0.0;
            #declare OrangeRed = color red 1.0 green 0.25; 
            #declare Asphalt = texture{
                pigment{color rgb<0.05,0.05,0.05>}
                normal {bumps 0.75 scale 0.015}
            }
            camera {
                perspective
                location <""" + str(my_x) + """, 8, """ + str(my_y) + """>
                look_at  <""" + str(at_x) + """, 8, """ + str(at_y) + """>
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
        for x, y, a in self.cones:
            pov += self._compile_cone(x, y, a)
        return pov

    def _compile_cone(self, x, y, a):
        if a == None:
            return """cone {
                <""" + str(x) + """, 4, """ + str(y) + """>, 0.1
                <""" + str(x) + """, 0, """ + str(y) + """>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }"""
        tip_x, tip_y = x + cos(a)*2, y + sin(a)*2
        base_x, base_y = x - cos(a)*2, y - sin(a)*2
        return """cone {
            <""" + str(tip_x) + """, 0, """ + str(tip_y) + """>, 0.1
            <""" + str(base_x) + """, 1, """ + str(base_y) + """>, 1.0
            texture { 
                finish { ambient Orange }
                pigment { color OrangeRed }
            }
        }"""

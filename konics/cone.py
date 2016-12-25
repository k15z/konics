import math

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

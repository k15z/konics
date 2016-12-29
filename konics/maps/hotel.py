from math import sin, cos

e_t = 0.9

def x_t(t):
    t = -t
    return sin(t*2.0*3.1415) * 200 + sin(t*2.0*3.1415*6.0)*20

def y_t(t):
    t = -t
    return cos(t*2.0*3.1415) * 200 + cos(t*2.0*3.1415*6.0)*20 + t*200

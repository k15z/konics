from math import sin, cos

e_t = 2.0
def x_t(t):
    t += 0.3
    return sin(t*2.0*3.1415) * 100 * t
def y_t(t):
    t += 0.3
    return cos(t*2.0*3.1415) * 100 * t

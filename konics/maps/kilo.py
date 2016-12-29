from math import sin, cos

e_t = 5.0

def x_t(t):
    return sin(t) * 100.0

def y_t(t):
    return cos(t) * 100.0 * t

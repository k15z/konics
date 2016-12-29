from math import cos

e_t = 5.0

def x_t(t):
    return t * 100.0

def y_t(t):
    return cos(t) * 100.0 * t + t ** 2

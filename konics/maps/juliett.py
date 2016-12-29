from math import sin

e_t = 8.0
BREAKPOINT = 6.0

def x_t(t):
    if t > BREAKPOINT:
        return x_t(BREAKPOINT) + 10.0 * (t - BREAKPOINT)
    return sin(t)*100.0

def y_t(t):
    return t * 200.0
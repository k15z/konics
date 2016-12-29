from math import sin

e_t = 6.0
BREAK_POINT = 3.0

def x_t(t):
    if t > BREAK_POINT:
        return x_t(BREAK_POINT) + (sin(t)*100.0 - sin(BREAK_POINT)*100.0)
    return t * 100.0

def y_t(t):
    return t * 200.0

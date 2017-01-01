from math import sin, cos

e_t = 60.0
BREAKPOINT_1 = 10.0
BREAKPOINT_2 = 15.0
BREAKPOINT_3 = 30.0
BREAKPOINT_4 = 35.0

def x_t(t):
    if t > BREAKPOINT_4:
        return x_t(BREAKPOINT_4) + (t - BREAKPOINT_4) * 10.0
    if t > BREAKPOINT_3:
        return x_t(BREAKPOINT_3) - sin((t - BREAKPOINT_3) / 1.5) * 30.0
    if t > BREAKPOINT_2:
        return x_t(BREAKPOINT_2) - (t - BREAKPOINT_2) * 10.0
    if t > BREAKPOINT_1:
        return x_t(BREAKPOINT_1) + sin((t - BREAKPOINT_1) / 1.5) * 30.0
    return t * 10.0

def y_t(t):
    if t > BREAKPOINT_4:
        return y_t(BREAKPOINT_4)
    if t > BREAKPOINT_3:
        return y_t(BREAKPOINT_3) + cos((t - BREAKPOINT_3) / 1.5) * 15.0 - 15.0
    if t > BREAKPOINT_2:
        return y_t(BREAKPOINT_2)
    if t > BREAKPOINT_1:
        return y_t(BREAKPOINT_1) + cos((t - BREAKPOINT_1) / 1.5) * 15.0 - 15.0
    return 0.0

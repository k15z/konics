e_t = 10.0

BREAK_POINT_1 = 2.0
BREAK_POINT_2 = 4.0
BREAK_POINT_3 = 6.0

def x_t(t):
    if t > BREAK_POINT_1:
        return x_t(BREAK_POINT_1) + 50.0 * (t - BREAK_POINT_1)
    return t * 100.0

def y_t(t):
    if t > BREAK_POINT_3:
        return y_t(BREAK_POINT_3) - 25.0 * (t - BREAK_POINT_3)
    if t > BREAK_POINT_2:
        return y_t(BREAK_POINT_2) + 0.0 * (t - BREAK_POINT_2)
    return t * 50.0

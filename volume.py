def Cube(a,b,c):
    if (type(a) == str or type(b) == str or type(c) == str):
        raise TypeError("String input invalid")
    elif a < 0 or b < 0 or c < 0:
        raise ValueError("Tried to compute volume with negative value")
    else:
        return a * b * c

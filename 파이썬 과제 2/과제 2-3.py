def circleArea(r):
    size = pi*(r**2)
    print("반지름이 5인 원의 면적: {0}".format(size))

def circleCircumference(r):
    dul = 2*pi*r
    print("반지름이 5인 원의 둘레: {0}".format(dul))

import math
pi = math.pi
circleCircumference(5)
circleArea(5)

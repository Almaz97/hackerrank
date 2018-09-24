from cmath import sqrt, acos
from math import degrees


def hypotenuse(catA, catB):
    hyp = sqrt(pow(catA, 2) + pow(catB, 2))
    return hyp.real

def findAngle():
    AB = int(input())
    AC = int(input())

    hyp = hypotenuse(AB, AC)
    AM = CM = hyp / 2
    a = acos((pow(AM, 2) + pow(AC, 2) - pow(CM, 2)) / (2*AM*AC))
    a = a.real
    deg = degrees(a)
    deg = round(deg)
    sign = '°'
    deg = str(deg)
    print(deg + sign)


if __name__ == '__main__':
    findAngle()
"""
Authors:

Linus Below Blomkvist <libl@kth.se>
 
code skeleton

Variable names:

Input variables

NUMPOINTS The number of planar data points.

POINTS Array containing the coordinates of data points.

PARAMETERS Struct holding parameters for LIC’s (see below).

LCM Logical Connector Matrix.

PUV Preliminary Unlocking Vector.

Output variables

LAUNCH Final launch / no launch decision encoded as ”YES”, ”NO” on the standard output.

In addition, the following intermediate results are computed.

CMV Conditions Met Vector.

PUM Preliminary Unlocking Matrix.

FUV Final Unlocking Vector.

"""
import math as m

def DECIDE():
    return

def CMV():
    return

def PUM():
    return

def FUV():
    return

def LIC_0(points, length1) -> bool:
    result = False
    # Handle invalid data
    if length1 < 0:
        return result
    for i in range(len(points) - 1):
        if m.dist(points[i], points[i+1]) > length1:
            result = True
            break
    return result

def LIC_1(points, radius1) -> bool:
    result = False
    # Handle invalid data
    if radius1 < 0 or len(points) < 3:
        return result
    for i in range(len(points) - 2):
        a = m.dist(points[i], points[i+1])
        b = m.dist(points[i+1], points[i+2])
        c = m.dist(points[i], points[i+2])
        abc_div_2 = (a+b+c) / 2
        if float(radius1) >= a*b*c / (4*m.sqrt(abc_div_2*(abc_div_2-a)*(abc_div_2-b)*(abc_div_2-c))):
            result = True
            break
    return result

def LIC_2():
    return

def LIC_3():
    return

def LIC_4():
    return

def LIC_5():
    return

def LIC_6():
    return

def LIC_7():
    return

def LIC_8():
    return

def LIC_9():
    return

def LIC_10():
    return

def LIC_11():
    return

def LIC_12():
    return

def LIC_13():
    return

def LIC_14():
    return

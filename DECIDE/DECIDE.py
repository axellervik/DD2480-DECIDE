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

def LIC_1():
    return

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

def LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS):
    if (LENGTH2 < 0 or NUMPOINTS < 3):
            return False
    
    finnished_length1 = False
    finnished_length2 = False

    for i in range(NUMPOINTS):
        if (finnished_length1 and finnished_length2):
            break
        
        p1 = POINTS[i]
        p2 = POINTS[(i + K_PTS)%NUMPOINTS]

        dist = m.dist(p1, p2)

        if (dist > LENGTH1):
            finnished_length1 = True
        if (dist < LENGTH2):
            finnished_length2 = True
    if (finnished_length1 and finnished_length2):
        return True
    else:
        return False

def LIC_13():
    return

def LIC_14():
    return

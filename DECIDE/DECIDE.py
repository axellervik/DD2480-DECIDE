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

def LIC_2(points, epsilon) -> bool:
    result = False
    # Handle invalid data
    if epsilon < 0:
        return result
    for i in range(len(points) - 2):
        if points[i] != points[i+1] and points[i+1] != points[i+2]:
            x = m.dist(points[i], points[i+1])
            y = m.dist(points[i+1], points[i+2])
            abs_x = abs(x)
            abs_y = abs(y)
            angle = m.acos(x*y/(abs_x*abs_y))
            if angle < m.pi - epsilon or angle > m.pi - epsilon: 
                result = True
                break
            
        return result
        
        
        
    return result

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

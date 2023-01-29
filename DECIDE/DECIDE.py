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

def LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON):
    if(NUMPOINTS < 5 or C_PTS < 1 or D_PTS < 1 or C_PTS + D_PTS > NUMPOINTS - 3):
        return False
    
    for i in range(NUMPOINTS):
        p1 = POINTS[i]
        p2 = POINTS[(i + C_PTS)%NUMPOINTS]
        p3 = POINTS[(i + C_PTS + D_PTS)%NUMPOINTS]

        if(p1 != p2 and p3 != p2):
            angle = m.atan2(p3[1]-p2[1], p3[0]-p2[0]) - m.atan2(p1[1]-p2[1], p1[0]-p2[0])
            if(angle < m.pi - EPSILON or angle > m.pi + EPSILON):
                return True

    return False

def LIC_10():
    return

def LIC_11():
    return

def LIC_12():
    return

def LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2):
    if(NUMPOINTS < 5 or RADIUS2 < 0):
        return False
    
    finished_RADIUS1 = False
    finished_RADIUS2 = False
    for i in range(NUMPOINTS):
        if(finished_RADIUS1 and finished_RADIUS2):
            break
        x1 = POINTS[i][0]
        y1 = POINTS[i][1]

        x2 = POINTS[(i + A_PTS)%NUMPOINTS][0]
        y2 = POINTS[(i + A_PTS)%NUMPOINTS][1]

        x3 = POINTS[(i + A_PTS + B_PTS)%NUMPOINTS][0]
        y3 = POINTS[(i + A_PTS + B_PTS)%NUMPOINTS][1]

        d1 = m.dist((x1,y1), (x2,y2))
        d2 = m.dist((x1,y1), (x3,y3))
        d3 = m.dist((x2,y2), (x3,y3))
        maxDistance = max(d1, d2, d3)

        if(maxDistance > RADIUS1*2):
            finished_RADIUS1 = True

        if(maxDistance <= RADIUS2*2):
            finished_RADIUS2 = True

    if(finished_RADIUS1 and finished_RADIUS2):
        return True
    return False

def LIC_14():
    return
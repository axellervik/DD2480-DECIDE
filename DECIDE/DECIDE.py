"""
Authors:

Linus Below Blomkvist <libl@kth.se>
Ali Asbai <asbai@kth.se>
 
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

def LIC_0():
    return

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

def LIC_12():
    return

def LIC_13():
    return

def LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS):
    if(NUMPOINTS < 5 or AREA2 < 0):
        return False
    
    finished_AREA1 = False
    finished_AREA2 = False
    for i in range(NUMPOINTS):
        if(finished_AREA1 and finished_AREA2):
            break
        x1 = POINTS[i][0]
        y1 = POINTS[i][1]
        for j in range(NUMPOINTS):
            if(abs(x1 - POINTS[j][0]) == E_PTS and abs(y1 - POINTS[j][1]) == F_PTS and (x1, y1) != POINTS[j]):
                x2 = POINTS[j][0]
                y2 = POINTS[j][1]
                for k in range(NUMPOINTS):
                     if(abs(x2 - POINTS[k][0]) == E_PTS and abs(y2 - POINTS[k][1]) == F_PTS and (x1, y1) != POINTS[k] and (x2, y2) != POINTS[k]):
                        x3 = POINTS[k][0]
                        y3 = POINTS[k][1]

                        s = (m.dist([x1,y1], [x2,y2]) + m.dist([x2,y2], [x3,y3]) + m.dist([x1,y1], [x3,y3])) / 2
                        area = (s*(s - m.dist([x1,y1], [x2,y2]))*(s - m.dist([x2,y2], [x3,y3]))*(s - m.dist([x1,y1], [x3,y3]))) ** 0.5

                        if(area > AREA1):
                            finished_AREA1 = True

                        if(area < AREA2):
                            finished_AREA2 = True

    if(finished_AREA1 and finished_AREA2):
        return True
    return False

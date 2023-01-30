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
from enum import Enum

class LOGICAL_CONNECTOR(Enum):
    NOTUSED = 777
    ANDD = 1
    ORR = 2

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
        if abc_div_2 == 0 or abc_div_2 == a or abc_div_2 == b or abc_div_2 == c:
            continue
        if float(radius1) >= a*b*c / (4*m.sqrt(abc_div_2*(abc_div_2-a)*(abc_div_2-b)*(abc_div_2-c))):
            result = True
            break
    return result

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

def LIC_3(points, area1) -> bool:
    result = False
    # Handle invalid data
    if area1 < 0 or len(points) < 3:
        return result
    for i in range(len(points) - 2):
        a = m.dist(points[i], points[i+1])
        b = m.dist(points[i+1], points[i+2])
        c = m.dist(points[i], points[i+2])
        abc_div_2 = (a+b+c) / 2
        area = m.sqrt((abc_div_2*(abc_div_2-a)*(abc_div_2-b)*(abc_div_2-c)))
        if area > area1:
            result = True
            break
    return result

def LIC_4(points, q_pts, quads):
    result = False
    # Handle invalid data
    if q_pts < 2 or len(points) < q_pts or quads < 1 or 3 < quads:
        return result
    for i in range(len(points) - q_pts + 1):
        quad_visited = [0,0,0,0]
        for point in points[i:(i+q_pts)]:
            if point[0] >= 0 and point[1] >= 0 and not quad_visited[0]:
                quad_visited[0] = 1
            if point[0] <= 0 and point[1] >= 0 and not quad_visited[1]:
                quad_visited[1] = 1
            if point[0] <= 0 and point[1] <= 0 and not quad_visited[2]:
                quad_visited[2] = 1
            if point[0] >= 0 and point[1] <= 0 and not quad_visited[3]:
                quad_visited[3] = 1
        if sum(quad_visited) > quads:
            result = True
            break
    return result

def LIC_5(points) -> bool:
    result = False
    # Handle invalid data
    if len(points) < 2:
        return result
    for i in range(len(points) - 1):
        x_dist = points[i + 1][0] - points[i][0]
        if x_dist == 0:
            result = True
            break
    return result

def LIC_6(points, n_pts, dist) -> bool:
    result = False 
    # Handle invalid data
    if n_pts < 3 or len(points) < 3 or dist <= 0:
        return result
    for i in range(len(points) - n_pts):
        for j in range(i, i + n_pts):
            if points[i] != points[i+n_pts-1]:
                p_line = m.dist(points[i], points[i+n_pts-1])
                num = (points[i+n_pts][0] - points[i][0])*(points[i][1] - points[j][1]) - (points[i][0] - points[j][0])*(points[i][1] - points[i + n_pts][1])
                denom = m.sqrt((points[i+n_pts][0] - points[i][0])**2 + (points[i+n_pts][1] - points[i][1])**2)
                if denom == 0:
                    continue
                dis_to_line = abs(num)/denom
                if dis_to_line > dist:
                    result = True
                    break   
            if points[i] == points[i+n_pts-1]:
                dis = m.dist(points[i], points[j])
                if dis > dist:
                    result = True
                    break
    
    return result

def LIC_7(points, k_pts, length1) -> bool:
    result = False
    # Handle invalid data
    if k_pts < 1 or len(points)-2 < k_pts or len(points) < 3 or length1 < 0:
        return result
    for i in range(len(points)-k_pts-1):
        if m.dist(points[i], points[i+1+k_pts]) > length1:
            result = True
            break
    return result

def LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1):
    if (NUMPOINTS < 5 or 1 > A_PTS or B_PTS > 1 or A_PTS + B_PTS > NUMPOINTS - 3):
        return False
    
    for i in range(NUMPOINTS):
        p1 = POINTS[i]
        p2 = POINTS[(i + A_PTS)%NUMPOINTS]
        p3 = POINTS[(i + A_PTS + B_PTS)%NUMPOINTS]
        
        d1 = m.dist(p1, p2)
        d2 = m.dist(p1, p3)
        d3 = m.dist(p2, p3)
        maxDistance = max(d1, d2, d3)

        if(maxDistance > RADIUS1*2):
            return True
    return False

def LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON):
    if(NUMPOINTS < 5 or C_PTS < 1 or D_PTS < 1 or C_PTS + D_PTS > NUMPOINTS - 3):
        return False
    
    for i in range(NUMPOINTS):
        p1 = POINTS[i]
        p2 = POINTS[(i + C_PTS)%NUMPOINTS]
        p3 = POINTS[(i + C_PTS + D_PTS)%NUMPOINTS]

        if(p1 != p2 and p3 != p2):
            angle = m.atan2(p3[1]-p2[1], p3[0]-p2[0]) - m.atan2(p1[1]-p2[1], p1[0]-p2[0])
            if(abs(angle) < m.pi - EPSILON or abs(angle) > m.pi + EPSILON):
                return True

    return False

def LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1):
    if (NUMPOINTS < 5 or 1 > E_PTS or 1 > F_PTS or E_PTS + F_PTS > NUMPOINTS - 3):
        return False

    for i in range(NUMPOINTS):
        p1 = POINTS[i]
        p2 = POINTS[(i + E_PTS)%NUMPOINTS]
        p3 = POINTS[(i + E_PTS + F_PTS)%NUMPOINTS]

        s = (m.dist(p1, p2) + m.dist(p2, p3) + m.dist(p1, p3)) / 2
        area = m.sqrt(s * (s - m.dist(p1, p2)) * (s - m.dist(p2, p3)) * (s - m.dist(p1, p3)))

        if (area > AREA1):
            return True
    return False

def LIC_11(NUMPOINTS, POINTS, G_PTS):
    if(NUMPOINTS < 3 or G_PTS < 1 or NUMPOINTS - 2 < G_PTS):
        return False
    
    for i in range(NUMPOINTS - G_PTS):
        p1 = POINTS[i]
        p2 = POINTS[(i + G_PTS)]

        if(p2[0] - p1[0] < 0):
            return True
    return False

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

        x2 = POINTS[(i+E_PTS)%NUMPOINTS][0]
        y2 = POINTS[(i+E_PTS)%NUMPOINTS][1]

        x3 = POINTS[(i+E_PTS+F_PTS)%NUMPOINTS][0]
        y3 = POINTS[(i+E_PTS+F_PTS)%NUMPOINTS][1]

        s = (m.dist([x1,y1], [x2,y2]) + m.dist([x2,y2], [x3,y3]) + m.dist([x1,y1], [x3,y3])) / 2
        area = m.sqrt(s * (s - m.dist([x1,y1], [x2,y2])) * (s - m.dist([x2,y2], [x3,y3])) * (s - m.dist([x1,y1], [x3,y3])))

        if (area > AREA1):
            finished_AREA1 = True
        if (area < AREA2):
            finished_AREA2 = True
    
    if(finished_AREA1 and finished_AREA2):
        return True
    return False

def CMV(points, length1, radius1, epsilon, area1, q_pts, quads, dist, n_pts, k_pts, a_pts, b_pts, c_pts, d_pts, e_pts, f_pts, g_pts, length2, radius2, area2):
    lic_vector = []
    lic_vector.append(LIC_0(points, length1))
    lic_vector.append(LIC_1(points, radius1))
    lic_vector.append(LIC_2(points, epsilon))
    lic_vector.append(LIC_3(points, area1))
    lic_vector.append(LIC_3(points, area1))
    lic_vector.append(LIC_4(points, q_pts, quads))
    lic_vector.append(LIC_5(points))
    lic_vector.append(LIC_6(points, n_pts, dist))
    lic_vector.append(LIC_7(points, k_pts, length1))
    lic_vector.append(LIC_8(len(points), points, a_pts, b_pts, radius1))
    lic_vector.append(LIC_9(len(points), points, c_pts, d_pts, epsilon))
    lic_vector.append(LIC_10(len(points), points, e_pts, f_pts, area1))
    lic_vector.append(LIC_11(len(points), points, g_pts))
    lic_vector.append(LIC_12(len(points), points, length1, length2, k_pts))
    lic_vector.append(LIC_13(len(points), points, a_pts, b_pts, radius1, radius2))
    lic_vector.append(LIC_14(points, len(points), area1, area2, e_pts, f_pts))
    return lic_vector

def PUM(LCM, CMV):
    result = [[False for i in range(15)] for j in range(15)]
    for i in range(15):
        for j in range(15):
            if LCM[i][j] == LOGICAL_CONNECTOR.ANDD:
                result[i][j] = CMV[i] and CMV[j]
            elif LCM[i][j] == LOGICAL_CONNECTOR.ORR:
                result[i][j] = CMV[i] or CMV[j]
            else:
                result[i][j] = True
    return result

def FUV(PUV, LCM, CMV):
    PUM_vector = PUM(LCM, CMV);
    FUV_vector = []
    for i in range(15):
       if PUV[i] == False:
           FUV_vector.append(True)
       elif PUV[i] == True: 
            for j in range(15):
                if PUM_vector[i][j] == False:
                    FUV_vector.append(False)
                    break
                else:
                    FUV_vector.append(True)
    
    return FUV_vector

def DECIDE(LCM, PUV, POINTS, LENGTH1, RADIUS1, EPSILON, AREA1, Q_PTS, QUADS, DIST, N_PTS, K_PTS, A_PTS, B_PTS, C_PTS, D_PTS, E_PTS, F_PTS, G_PTS, LENGTH2, RADIUS2, AREA2):
    cmv = CMV(POINTS, LENGTH1, RADIUS1, EPSILON, AREA1, Q_PTS, QUADS, DIST, N_PTS, K_PTS, A_PTS, B_PTS, C_PTS, D_PTS, E_PTS, F_PTS, G_PTS, LENGTH2, RADIUS2, AREA2)
    fuv = FUV(PUV, LCM, cmv)
    result = all(fuv)
    if result:
        print("YES!")
    else:
        print("NO!")
    return result

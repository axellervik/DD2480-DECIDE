import unittest
from enum import Enum
from DECIDE.DECIDE import *

class LOGICAL_CONNECTOR(Enum):
    NOTUSED = 777
    ANDD = 1
    ORR = 2

class TestDECIDE(unittest.TestCase):

    def test_DECIDE_pos(self):
        # Parameters:
        POINTS = [(1,1), (2,2), (4,4),(0,0), (0,1), (1,0), (1,1), (2,2), (3,3),(0,0), (0,1), (1,0), (1,1), (-1,1), (-1,-1), (1,-1), (1,1), (1,2), (3,3), (0,0), (1,2), (2,0), (5,5), (0,0), (1,2), (0,0), (5,5), (1,1), (2,2), (3,1), (4,4), (5,5), (6,4), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (1,1), (2,2), (3,3), (2,2), (3,3), (1,1), (4,4), (5,5), (1,1), (3,3), (3,1), (4,4), (5,5), (1,1), (3,2), (3,3), (4,4), (5,5), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (0,0), (5,5), (99,-99), (10,10)]
        LENGTH1 = 2
        RADIUS1 = 1
        EPSILON = (m.pi/2)
        AREA1 = 0.49
        Q_PTS = 4
        QUADS = 3
        DIST = 1
        N_PTS = 3
        K_PTS = 2
        A_PTS = 1 # A_PTS = 1 also works
        B_PTS = 1 # B_PTS = 1 also works
        C_PTS = 1
        D_PTS = 1
        E_PTS = 1
        F_PTS = 1
        G_PTS = 2
        LENGTH2 = 100
        RADIUS2 = 100
        AREA2 = 100
        # Relevant matrices and vectors:
        LCM = [[LOGICAL_CONNECTOR.ANDD for _ in range(15)] for _ in range(15)]
        PUV = [True for _ in range(15)]
        # Assert that decide launches the missile for the specified input:
        self.assertTrue(DECIDE(LCM, PUV, POINTS, LENGTH1, RADIUS1, EPSILON, AREA1, Q_PTS, QUADS, DIST, N_PTS, K_PTS, A_PTS, B_PTS, C_PTS, D_PTS, E_PTS, F_PTS, G_PTS, LENGTH2, RADIUS2, AREA2))
        
    def test_PUM_pos(self):
        CMV = [True, False, True, True, False, True, False, False, False, True, True, False, True, False, False]
        LCM = [
                [LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED]
            ]
        expected_result = [
            [True, True, True, True, False, True, True, True, True, True, True, False, True, True, True], 
            [False, False, False, True, False, False, False, False, False, True, False, True, True, False, True], 
            [True, False, True, True, True, True, True, True, False, True, True, True, True, True, True], 
            [True, False, True, True, True, True, False, False, True, True, True, True, True, True, True], 
            [True, False, True, True, False, True, False, False, False, False, True, False, True, False, False], 
            [True, True, True, True, True, True, True, False, True, True, True, False, True, True, False], 
            [False, False, True, True, False, True, True, True, True, True, True, False, True, False, False], 
            [False, False, False, True, False, False, True, True, True, True, True, False, True, False, True], 
            [True, True, True, True, True, True, True, False, False, False, True, False, True, True, False], 
            [True, True, True, True, True, True, True, False, True, True, True, True, True, True, True], 
            [True, False, True, True, True, True, True, True, True, True, True, True, True, True, True], 
            [True, True, True, True, False, True, False, False, False, True, False, False, False, False, True], 
            [True, True, True, True, True, True, True, True, True, True, True, False, True, True, True], 
            [True, False, True, True, False, False, False, True, True, True, True, False, True, True, True], 
            [False, False, True, True, False, True, True, False, False, False, True, False, True, True, True]
        ]
        result = PUM(LCM, CMV)
        self.assertEqual(result, expected_result)

    def test_PUM_neg(self):
        CMV = [True, False, True, True, False, True, False, False, False, True, True, False, True, False, False]
        LCM = [
                [LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR], 
                [LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED], 
                [LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ANDD, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.ORR, LOGICAL_CONNECTOR.NOTUSED, LOGICAL_CONNECTOR.NOTUSED]
            ]
        expected_result = [
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        ]
        result = PUM(LCM, CMV)
        self.assertNotEqual(result, expected_result)

    def test_LIC_0_pos(self):
        POINTS = [(1,1), (2,2), (4,4)]
        LENGTH1 = 2
        result = LIC_0(POINTS, LENGTH1)
        self.assertTrue(result)
    
    def test_LIC_0_neg(self):
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 2
        result = LIC_0(POINTS, LENGTH1)
        self.assertFalse(result)
        
    def test_LIC_0_invalid(self):
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = -2
        result = LIC_0(POINTS, LENGTH1)
        self.assertFalse(result)

    def test_LIC_1_pos(self):
        POINTS = [(0,0), (0,1), (1,0)]
        RADIUS1 = 1
        self.assertTrue(LIC_1(POINTS, RADIUS1))

    def test_LIC_1_neg(self):
        POINTS = [(0,0), (0,1), (1,0)]
        RADIUS1 = 0.5
        self.assertFalse(LIC_1(POINTS, RADIUS1))

    def test_LIC_1_invalid1(self):
        POINTS = [(0,0), (0,1), (1,0)]
        RADIUS1 = -1
        self.assertFalse(LIC_1(POINTS, RADIUS1))

    def test_LIC_1_invalid2(self):
        POINTS = [(0,0), (0,1)]
        RADIUS1 = 1
        self.assertFalse(LIC_1(POINTS, RADIUS1))

    def test_LIC_2_invalid(self):
        POINTS = [(1,1), (2,2), (3,3)]
        EPSILON = -1
        result = LIC_2(POINTS, EPSILON)
        self.assertFalse(result)

    def test_LIC_2_neg(self):
        POINTS = [(2,2), (2,2), (3,3)]
        EPSILON = (m.pi/2)
        result = LIC_2(POINTS, EPSILON)
        self.assertFalse(result)

    def test_LIC_2_pos(self):
        POINTS = [(1,1), (2,2), (3,3)]
        EPSILON = (m.pi/2)
        result = LIC_2(POINTS, EPSILON)
        self.assertTrue(result)
        
    def test_LIC_3_pos(self):
        # the following points form a triangle with area 0.5
        POINTS = [(0,0), (0,1), (1,0)]
        AREA1 = 0.49
        self.assertTrue(LIC_3(POINTS, AREA1))

    def test_LIC_3_neg(self):
        # the following points form a triangle with area 0.5
        POINTS = [(0,0), (0,1), (1,0)]
        AREA1 = 0.5
        self.assertFalse(LIC_3(POINTS, AREA1))

    def test_LIC_3_invalid1(self):
        POINTS = [(0,0), (0,1), (1,0)]
        AREA1 = -1
        self.assertFalse(LIC_3(POINTS, AREA1))

    def test_LIC_3_invalid2(self):
        POINTS = [(0,0), (0,1)]
        AREA1 = 1
        self.assertFalse(LIC_3(POINTS, AREA1))

    def test_LIC_4_pos(self):
        POINTS = [(1,1),(-1,1),(-1,-1),(1,-1)]
        Q_PTS = 4
        QUADS = 3
        self.assertTrue(LIC_4(POINTS, Q_PTS, QUADS))

    def test_LIC_4_neg(self):
        POINTS = [(1,1),(2,2),(-1,-1),(1,-1)]
        Q_PTS = 2
        QUADS = 3
        self.assertFalse(LIC_4(POINTS, Q_PTS, QUADS))

    def test_LIC_4_invalid(self):
        POINTS = [(1,1),(-1,1),(-1,-1),(1,-1)]
        Q_PTS = 1
        QUADS = 1
        self.assertFalse(LIC_4(POINTS, Q_PTS, QUADS))

    def test_LIC_5_pos(self):
        POINTS = [(1,1), (1,2), (3,3)]
        result = LIC_5(POINTS)
        self.assertTrue(result)
        
    def test_LIC_5_neg(self):
        POINTS = [(1,1), (2,2), (3,3)]
        result = LIC_5(POINTS)
        self.assertFalse(result)
        
    def test_LIC_5_invalid(self):
        POINTS = [(1,1)]
        result = LIC_5(POINTS)
        self.assertFalse(result)

    def test_LIC_6_pos_1(self):
        DIST = 1
        N_PTS = 3
        POINTS = [(0,0),(1,2),(2,0),(5,5)] 
        self.assertTrue(LIC_6(POINTS, N_PTS, DIST))
        
    def test_LIC_6_pos_2(self):
        DIST = 1
        N_PTS = 3
        POINTS = [(0,0),(1,2),(0,0),(5,5)] 
        self.assertTrue(LIC_6(POINTS, N_PTS, DIST))
    
    def test_LIC_6_neg(self):
        DIST = 10
        N_PTS = 3
        POINTS = [(0,0),(1,2),(2,0),(5,5)] 
        self.assertFalse(LIC_6(POINTS, N_PTS, DIST))    
            
    def test_LIC_6_invalid(self):
        DIST = 2
        N_PTS = 2
        POINTS = [(1,1),(2,2)]    
        self.assertFalse(LIC_6(POINTS, N_PTS, DIST))

    def test_LIC_7_pos(self):
        POINTS = [(0,0),(5,5),(99,-99),(10,10)]
        K_POINTS = 2
        LENGTH1 = 10
        self.assertTrue(LIC_7(POINTS, K_POINTS, LENGTH1))

    def test_LIC_7_neg(self):
        POINTS = [(0,0),(100,100),(2,2),(102,102)]
        K_POINTS = 1
        LENGTH1 = 100
        self.assertFalse(LIC_7(POINTS, K_POINTS, LENGTH1))

    def test_LIC_7_invalid(self):
        POINTS = [(0,0),(1,1)]
        K_POINTS = 1
        LENGTH1 = -1
        self.assertFalse(LIC_7(POINTS, K_POINTS, LENGTH1))

    def test_LIC_8_invalid(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = -1
        B_PTS = 1
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    def test_LIC_8_invalid2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = 1
        B_PTS = -1
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    def test_LIC_8_invalid3(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    def test_LIC_8_neg(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        A_PTS = 1
        B_PTS = 1
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    def test_LIC_8_neg2(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 1
        B_PTS = 1
        RADIUS1 = 100
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    def test_LIC_8_pos(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 1
        B_PTS = 1
        RADIUS1 = 1
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertTrue(result)

    def test_LIC_9_invalid(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        C_PTS = 0
        D_PTS = 1
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    def test_LIC_9_invalid2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        C_PTS = 1
        D_PTS = 0
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    def test_LIC_9_invalid3(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        C_PTS = 2
        D_PTS = 2
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    def test_LIC_9_neg(self):
        NUMPOINTS = 4
        POINTS = [(1,1), (2,2), (3,3), (4,4)]
        C_PTS = 1
        D_PTS = 1
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    def test_LIC_9_neg2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (3,1), (3,3), (4,4), (5,4)]
        C_PTS = 1
        D_PTS = 1
        EPSILON = m.pi - m.pi / 100
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)
    
    def test_LIC_9_pos(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (3,2), (3,3), (4,4), (5,5)]
        C_PTS = 1
        D_PTS = 1
        EPSILON = m.pi / 2
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertTrue(result)

    def test_LIC_10_invalid(self):
        #Checks if E_PTS => 1
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        E_PTS = 0
        F_PTS = 1
        AREA1 = 1
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    def test_LIC_10_invalid2(self):
        #Checks if F_PTS => 1
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        E_PTS = 1
        F_PTS = 0
        AREA1 = 1
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    def test_LIC_10_invalid3(self):
        #Checks if E_PTS + F_PTS <= NUMPPOINTS - 3
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        E_PTS = 2
        F_PTS = 2
        AREA1 = 2
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    def test_LIC_10_neg(self):
        #Checks if NUMPOINTS => 5
        NUMPOINTS = 4
        POINTS = [(1,1), (2,2), (3,3), (4,4)]
        E_PTS = 1
        F_PTS = 1
        AREA1 = 2
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    def test_LIC_10_neg2(self):
        #Checks a negative case of points
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (3,1)]
        E_PTS = 2
        F_PTS = 2
        AREA1 = 100
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    def test_LIC_10_pos(self):
        #Checks a positive case of points
        NUMPOINTS = 5
        POINTS = [(1,1), (3,3), (3,1), (4,4), (5,5)]
        E_PTS = 1
        F_PTS = 1
        AREA1 = 1
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertTrue(result)

    def test_LIC_11_invalid1(self):
        # tests is False if G_PTS > NUMPOINTS - 2 
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        G_PTS = 4
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)

    def test_LIC_11_invalid2(self):
        # tests is False if G_PTS < 1
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        G_PTS = 0
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)
        
    def test_LIC_11_pos(self):
        NUMPOINTS = 5
        POINTS = [(2,2), (3,3), (1,1), (4,4), (5,5)]
        G_PTS = 2
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertTrue(result)

    def test_LIC_11_neg(self):
        # tests is False if NUMPOINTS <= 3
        NUMPOINTS = 2
        POINTS = [(1,1), (2,2)]
        G_PTS = 0
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)

    def test_LIC_12_invalid(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 5
        LENGTH2 = -1
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertFalse(result)

    def test_LIC_12_neg(self):
        NUMPOINTS = 1
        POINTS = [(1,1)]
        LENGTH1 = 100
        LENGTH2 = 1
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertFalse(result)

    def test_LIC_12_neg2(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 100
        LENGTH2 = 1
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertFalse(result)

    def test_LIC_12_pos(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 1
        LENGTH2 = 100
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertTrue(result)

    def test_LIC_13_invalid(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 4
        RADIUS2 = -1
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertFalse(result)

    def test_LIC_13_pos(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 1
        RADIUS2 = 100
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertTrue(result)

    def test_LIC_13_neg(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 4
        RADIUS2 = 4
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertFalse(result)

    def test_LIC_13_neg2(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 100
        RADIUS2 = 1
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertFalse(result)

    def test_LIC_14_invalid(self):
        AREA1 = 1
        AREA2 = -1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        NUMPOINTS = 5
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))

    def test_LIC_14_pos(self):
        AREA1 = 1
        AREA2 = 100
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,1), (4,4), (5,5), (6,4)]
        NUMPOINTS = 6
        self.assertTrue(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))

    def test_LIC_14_neg(self):
        # tests if False if numpoints is less than 5
        AREA1 = 1
        AREA2 = 1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,3)]
        NUMPOINTS = 3
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))

    def test_LIC_14_neg_2(self):
        # tests if False if wrong areas
        AREA1 = 100
        AREA2 = 1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,1), (4,4), (5,5), (6,4)]
        NUMPOINTS = 6
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))
        
if __name__ == '__main__':
    unittest.main()

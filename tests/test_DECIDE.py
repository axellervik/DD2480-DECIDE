import unittest
from DECIDE.DECIDE import *


class TestDECIDE(unittest.TestCase):

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

    def test_LIC_2(self):
        pass

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

    def test_LIC_4(self):
        pass

    def test_LIC_5(self):
        pass

    def test_LIC_6(self):
        pass

    def test_LIC_7(self):
        pass

    def test_LIC_8(self):
        pass

    def test_LIC_9(self):
        pass

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
        # tests is false if G_PTS > NUMPOINTS - 2 
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        G_PTS = 4
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)

    def test_LIC_11_invalid2(self):
        # tests is false if G_PTS < 1
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
        # tests is false if NUMPOINTS <= 3
        NUMPOINTS = 2
        POINTS = [(1,1), (2,2)]
        G_PTS = 0
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)

    def test_LIC_12(self):
        pass

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
        # tests if false if numpoints is less than 5
        AREA1 = 1
        AREA2 = 1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,3)]
        NUMPOINTS = 3
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))

    def test_LIC_14_neg_2(self):
        # tests if false if wrong areas
        AREA1 = 100
        AREA2 = 1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,1), (4,4), (5,5), (6,4)]
        NUMPOINTS = 6
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))
        
if __name__ == '__main__':
    unittest.main()

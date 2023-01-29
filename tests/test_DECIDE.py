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

    def test_LIC_1(self):
        pass

    def test_LIC_2(self):
        pass

    def test_LIC_3(self):
        pass

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

    def test_LIC_10(self):
        pass

    def test_LIC_11(self):
        pass

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

    def test_LIC_14(self):
        pass

if __name__ == '__main__':
    unittest.main()
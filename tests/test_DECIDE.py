import unittest
from DECIDE.DECIDE import *


class TestDECIDE(unittest.TestCase):

    def test_LIC_0(self):
        pass

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

    def test_LIC_13(self):
        pass

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
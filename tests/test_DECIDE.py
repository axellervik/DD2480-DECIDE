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

    def test_LIC_13(self):
        pass

    def test_LIC_14(self):
        pass

if __name__ == '__main__':
    unittest.main()
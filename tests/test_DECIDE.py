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

    def test_LIC_10(self):
        pass

    def test_LIC_11(self):
        pass

    def test_LIC_12(self):
        pass

    def test_LIC_13(self):
        pass

    def test_LIC_14(self):
        pass

if __name__ == '__main__':
    unittest.main()
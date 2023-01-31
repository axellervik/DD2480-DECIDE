import unittest
from DECIDE.DECIDE import *


class TestDECIDE(unittest.TestCase):

    '''Test the PUM funciton with a positive and correct example'''
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

    '''Test the PUM funciton with a negative example which still has the correct input format'''
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
        
    def test_FUV(self):
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
    
        PUV = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        result = FUV(PUV, LCM, CMV)
        expected_result = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True];
        self.assertEqual(result, expected_result)
       
        

    '''
    Testing a positive input case for LIC0:
    There should exist two consecutive data points that are 
    further apart than LENGTH1.
    '''
    def test_LIC_0_pos(self):
        POINTS = [(1,1), (2,2), (4,4)]
        LENGTH1 = 2
        result = LIC_0(POINTS, LENGTH1)
        self.assertTrue(result)
    
    '''
    Testing a negative input case for LIC0:
    There does NOT exist two consecutive data points that are 
    further apart than LENGTH1.
    '''
    def test_LIC_0_neg(self):
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 2
        result = LIC_0(POINTS, LENGTH1)
        self.assertFalse(result)
    
    '''
    Testing an input case with invalid input for LIC0:
    Invalid input for LENGTH1, meaning LENGTH1 < 0.
    '''
    def test_LIC_0_invalid(self):
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = -2
        result = LIC_0(POINTS, LENGTH1)
        self.assertFalse(result)

    '''
    Testing a positive input case for LIC1:
    There should exist three consecutive data points that cannot 
    all be contained within or on a circle of radius RADIUS1.
    '''
    def test_LIC_1_pos(self):
        POINTS = [(0,0), (0,1), (1,0)]
        RADIUS1 = 1
        self.assertTrue(LIC_1(POINTS, RADIUS1))

    '''
    Testing a negative input case for LIC1:
    There does NOT exist three consecutive data points that 
    cannot all be contained within or on a circle of radius RADIUS1.
    '''
    def test_LIC_1_neg(self):
        POINTS = [(0,0), (0,1), (1,0)]
        RADIUS1 = 0.5
        self.assertFalse(LIC_1(POINTS, RADIUS1))

    '''
    Testing an input case with invalid input for LIC1:
    Invalid input for RADIUS1, meaning RADIUS1 < 0.
    '''
    def test_LIC_1_invalid1(self):
        POINTS = [(0,0), (0,1), (1,0)]
        RADIUS1 = -1
        self.assertFalse(LIC_1(POINTS, RADIUS1))

    '''
    Testing an input case with invalid input for LIC1:
    Invalid input for POINTS, meaning there are less than 3 points.
    '''
    def test_LIC_1_invalid2(self):
        POINTS = [(0,0), (0,1)]
        RADIUS1 = 1
        self.assertFalse(LIC_1(POINTS, RADIUS1))

    '''
    Testing an input case with invalid input for LIC2:
    Invalid input for EPSILON, meaning EPSILON < 0.
    '''
    def test_LIC_2_invalid(self):
        POINTS = [(1,1), (2,2), (3,3)]
        EPSILON = -1
        result = LIC_2(POINTS, EPSILON)
        self.assertFalse(result)

    '''
    Testing a positive input case for LIC2:
    There does NOT exist an angle formed by three consecutive 
    data points that meet the requirements, angle < (PI−EPSILON) 
    and angle > (PI+EPSILON).
    '''
    def test_LIC_2_neg(self):
        POINTS = [(2,2), (2,2), (3,3)]
        EPSILON = (m.pi/2)
        result = LIC_2(POINTS, EPSILON)
        self.assertFalse(result)

    '''
    Testing a positive input case for LIC2:
    There should exist an angle formed by three consecutive 
    data points that meet the requirements, angle < (PI−EPSILON) 
    and angle > (PI+EPSILON).
    '''
    def test_LIC_2_pos(self):
        POINTS = [(1,1), (2,2), (3,3)]
        EPSILON = (m.pi/2)
        result = LIC_2(POINTS, EPSILON)
        self.assertTrue(result)
    
    '''
    Testing a positive input case for LIC3:
    There should exist three consecutive data points forming a 
    triangle with area greater than AREA1.
    '''
    def test_LIC_3_pos(self):
        # the following points form a triangle with area 0.5
        POINTS = [(0,0), (0,1), (1,0)]
        AREA1 = 0.49
        self.assertTrue(LIC_3(POINTS, AREA1))

    '''
    Testing a negative input case for LIC3:
    There does NOT exist three consecutive data points forming a
    triangle with area greater than AREA1.
    '''
    def test_LIC_3_neg(self):
        # the following points form a triangle with area 0.5
        POINTS = [(0,0), (0,1), (1,0)]
        AREA1 = 0.5
        self.assertFalse(LIC_3(POINTS, AREA1))
    
    '''
    Testing an input case with invalid input for LIC3:
    Invalid input for AREA1, meaning AREA1 < 0.
    '''
    def test_LIC_3_invalid1(self):
        POINTS = [(0,0), (0,1), (1,0)]
        AREA1 = -1
        self.assertFalse(LIC_3(POINTS, AREA1))

    '''
    Testing an input case with invalid input for LIC3:
    Invalid input for POINTS, meaning there are less than 3 points.
    '''
    def test_LIC_3_invalid2(self):
        POINTS = [(0,0), (0,1)]
        AREA1 = 1
        self.assertFalse(LIC_3(POINTS, AREA1))

    '''
    Testing a positive input case for LIC4:
    There should exist at least one set of Q_PTS consecutive data 
    points which lie in more than QUADS quadrants.
    '''
    def test_LIC_4_pos(self):
        POINTS = [(1,1),(-1,1),(-1,-1),(1,-1)]
        Q_PTS = 4
        QUADS = 3
        self.assertTrue(LIC_4(POINTS, Q_PTS, QUADS))

    '''
    Testing a negative input case for LIC4:
    There does NOT exist at least one set of Q_PTS consecutive 
    data points which lie in more than QUADS quadrants.
    '''
    def test_LIC_4_neg(self):
        POINTS = [(1,1),(2,2),(-1,-1),(1,-1)]
        Q_PTS = 2
        QUADS = 3
        self.assertFalse(LIC_4(POINTS, Q_PTS, QUADS))

    '''
    Testing an input case with invalid input for LIC4:
    Invalid input for Q_PTS, meaning Q_PTS < 2.
    '''
    def test_LIC_4_invalid(self):
        POINTS = [(1,1),(-1,1),(-1,-1),(1,-1)]
        Q_PTS = 1
        QUADS = 1
        self.assertFalse(LIC_4(POINTS, Q_PTS, QUADS))

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """ 
    def test_LIC_5_pos(self):
        POINTS = [(1,1), (1,2), (3,3)]
        result = LIC_5(POINTS)
        self.assertTrue(result)

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """    
    def test_LIC_5_neg(self):
        POINTS = [(1,1), (2,2), (3,3)]
        result = LIC_5(POINTS)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the number of datapoints is too low.
    """        
    def test_LIC_5_invalid(self):
        POINTS = [(1,1)]
        result = LIC_5(POINTS)
        self.assertFalse(result)

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """ 
    def test_LIC_6_pos_1(self):
        DIST = 1
        N_PTS = 3
        POINTS = [(0,0),(1,2),(2,0),(5,5)] 
        self.assertTrue(LIC_6(POINTS, N_PTS, DIST))

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """         
    def test_LIC_6_pos_2(self):
        DIST = 1
        N_PTS = 3
        POINTS = [(0,0),(1,2),(0,0),(5,5)] 
        self.assertTrue(LIC_6(POINTS, N_PTS, DIST))

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """  
    def test_LIC_6_neg(self):
        DIST = 10
        N_PTS = 3
        POINTS = [(0,0),(1,2),(2,0),(5,5)] 
        self.assertFalse(LIC_6(POINTS, N_PTS, DIST))    

    """
    Invalid test: 
    Checks wether the method recognizes that the variable N_PTS is less that 3.
    """        
    def test_LIC_6_invalid(self):
        DIST = 2
        N_PTS = 2
        POINTS = [(1,1),(2,2)]    
        self.assertFalse(LIC_6(POINTS, N_PTS, DIST))

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """ 
    def test_LIC_7_pos(self):
        POINTS = [(0,0),(5,5),(99,-99),(10,10)]
        K_POINTS = 2
        LENGTH1 = 10
        self.assertTrue(LIC_7(POINTS, K_POINTS, LENGTH1))

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """ 
    def test_LIC_7_neg(self):
        POINTS = [(0,0),(100,100),(2,2),(102,102)]
        K_POINTS = 1
        LENGTH1 = 100
        self.assertFalse(LIC_7(POINTS, K_POINTS, LENGTH1))

    """
    Invalid test: 
    Checks wether the method recognizes that the given length is too short.
    """
    def test_LIC_7_invalid(self):
        POINTS = [(0,0),(1,1)]
        K_POINTS = 1
        LENGTH1 = -1
        self.assertFalse(LIC_7(POINTS, K_POINTS, LENGTH1))

    """
    Invalid test: 
    Checks wether the method recognizes that the variable A_PTS is less than 1.
    """
    def test_LIC_8_invalid(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = -1
        B_PTS = 1
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variable B_PTS is less than 1.
    """
    def test_LIC_8_invalid2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = 1
        B_PTS = -1
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variables A_PTS and B_PTS added together is more the the number of datapoints - 3.
    """
    def test_LIC_8_invalid3(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the number of datapoints is too low.
    """   
    def test_LIC_8_neg(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        A_PTS = 1
        B_PTS = 1
        RADIUS1 = 4
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """   
    def test_LIC_8_neg2(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 1
        B_PTS = 1
        RADIUS1 = 100
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertFalse(result)

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """   
    def test_LIC_8_pos(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 1
        B_PTS = 1
        RADIUS1 = 1
        result = LIC_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1)
        self.assertTrue(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variable C_PTS is less than 1.
    """
    def test_LIC_9_invalid(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        C_PTS = 0
        D_PTS = 1
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variable D_PTS is less than 1.
    """
    def test_LIC_9_invalid2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        C_PTS = 1
        D_PTS = 0
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variables C_PTS and D_PTS added together is more the the number of datapoints - 3.
    """
    def test_LIC_9_invalid3(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        C_PTS = 2
        D_PTS = 2
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the number of datapoints is too low.
    """
    def test_LIC_9_neg(self):
        NUMPOINTS = 4
        POINTS = [(1,1), (2,2), (3,3), (4,4)]
        C_PTS = 1
        D_PTS = 1
        EPSILON = 1
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """
    def test_LIC_9_neg2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (3,1), (3,3), (4,4), (5,4)]
        C_PTS = 1
        D_PTS = 1
        EPSILON = m.pi - m.pi / 100
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertFalse(result)

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """    
    def test_LIC_9_pos(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (3,2), (3,3), (4,4), (5,5)]
        C_PTS = 1
        D_PTS = 1
        EPSILON = m.pi / 2
        result = LIC_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON)
        self.assertTrue(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variable E_PTS is less than 1.
    """
    def test_LIC_10_invalid(self):
        #Checks if E_PTS => 1
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        E_PTS = 0
        F_PTS = 1
        AREA1 = 1
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variable F_PTS is less than 1.
    """
    def test_LIC_10_invalid2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        E_PTS = 1
        F_PTS = 0
        AREA1 = 1
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variables E_PTS and F_PTS added together is more the the number of datapoints - 3.
    """
    def test_LIC_10_invalid3(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        E_PTS = 2
        F_PTS = 2
        AREA1 = 2
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the number of datapoints is less too low.
    """
    def test_LIC_10_neg(self):
        NUMPOINTS = 4
        POINTS = [(1,1), (2,2), (3,3), (4,4)]
        E_PTS = 1
        F_PTS = 1
        AREA1 = 2
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """
    def test_LIC_10_neg2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (3,1)]
        E_PTS = 2
        F_PTS = 2
        AREA1 = 100
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertFalse(result)

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """
    def test_LIC_10_pos(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (3,3), (3,1), (4,4), (5,5)]
        E_PTS = 1
        F_PTS = 1
        AREA1 = 1
        result = LIC_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1)
        self.assertTrue(result)

    """
    Invalid test: 
    Checks wether the method recognizes that tthe variable G_PTS is more than the number of datapoints - 2.
    """
    def test_LIC_11_invalid(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        G_PTS = 4
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the variable G_PTS is less than 1.
    """
    def test_LIC_11_invalid2(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        G_PTS = 0
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """    
    def test_LIC_11_pos(self):
        NUMPOINTS = 5
        POINTS = [(2,2), (3,3), (1,1), (4,4), (5,5)]
        G_PTS = 2
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertTrue(result)

    """
    Negative test: 
    Checks wether the method recognizes that the number of datapoints is too low.
    """
    def test_LIC_11_neg(self):
        NUMPOINTS = 2
        POINTS = [(1,1), (2,2)]
        G_PTS = 0
        result = LIC_11(NUMPOINTS, POINTS, G_PTS)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the given length is less than zero.
    """
    def test_LIC_12_invalid(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 5
        LENGTH2 = -1
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the number of datapoints is too low.
    """
    def test_LIC_12_neg(self):
        NUMPOINTS = 1
        POINTS = [(1,1)]
        LENGTH1 = 100
        LENGTH2 = 1
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """
    def test_LIC_12_neg2(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 100
        LENGTH2 = 1
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertFalse(result)

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """
    def test_LIC_12_pos(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        LENGTH1 = 1
        LENGTH2 = 100
        K_PTS = 2
        result = LIC_12(NUMPOINTS, POINTS, LENGTH1, LENGTH2, K_PTS)
        self.assertTrue(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the given radius is less than zero.
    """
    def test_LIC_13_invalid(self):
        NUMPOINTS = 5
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 4
        RADIUS2 = -1
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertFalse(result)

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """
    def test_LIC_13_pos(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 1
        RADIUS2 = 100
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertTrue(result)

    """
    Negative test: 
    Checks wether the method recognizes that the number of datapoints is too low.
    """
    def test_LIC_13_neg(self):
        NUMPOINTS = 3
        POINTS = [(1,1), (2,2), (3,3)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 4
        RADIUS2 = 4
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertFalse(result)

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """
    def test_LIC_13_neg2(self):
        NUMPOINTS = 6
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        A_PTS = 2
        B_PTS = 2
        RADIUS1 = 100
        RADIUS2 = 1
        result = LIC_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2)
        self.assertFalse(result)

    """
    Invalid test: 
    Checks wether the method recognizes that the given area is less than zero.
    """
    def test_LIC_14_invalid(self):
        AREA1 = 1
        AREA2 = -1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        NUMPOINTS = 5
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))

    """
    Positive test: 
    Checks wether the method recognizes that the set of datapoints meet the requirements of the LIC.
    """ 
    def test_LIC_14_pos(self):
        AREA1 = 1
        AREA2 = 100
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,1), (4,4), (5,5), (6,4)]
        NUMPOINTS = 6
        self.assertTrue(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))

    """
    Negative test:
    Checks wether the method recognizes that the number of datapoints is too low.
    """
    def test_LIC_14_neg(self):
        AREA1 = 1
        AREA2 = 1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,3)]
        NUMPOINTS = 3
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))

    """
    Negative test: 
    Checks wether the method recognizes that the set of datapoints don't meet the requirements of the LIC.
    """
    def test_LIC_14_neg_2(self):
        AREA1 = 100
        AREA2 = 1
        E_PTS = 1
        F_PTS = 1
        POINTS = [(1,1), (2,2), (3,1), (4,4), (5,5), (6,4)]
        NUMPOINTS = 6
        self.assertFalse(LIC_14(POINTS, NUMPOINTS, AREA1, AREA2, E_PTS, F_PTS))
        
if __name__ == '__main__':
    unittest.main()

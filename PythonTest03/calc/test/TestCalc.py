'''
Created on 8/8/2014

@author: Jean Carlos
'''
import unittest 
from calc.calculator import Calculator

class TestCalc(unittest.TestCase):
    def testAdd(self):
        calculator=Calculator()
        result=calculator.Add(2, 3)
        self.assertEquals(result,5,"Addition failed") 
        
        
'''
Created on 18 de mai de 2016

@author: Anderson Macedo
'''
import unittest

from Grafos.GrafosUtil import Vertice



class Test(unittest.TestCase):

    def setUp(self):
        self.vertice_A = Vertice("SP", 1)
        self.vertice_B = Vertice("RJ", 2)
        self.vertice_C = Vertice("SC", 3)
        self.vertice_A.add_adjacentes(self.vertice_B, 10)
        self.vertice_A.add_adjacentes(self.vertice_C, 20)
        pass
    def testVerticeAdj(self):
        expected = dict()
        expected[self.vertice_B] = 10
        expected[self.vertice_C] = 20
        adj = self.vertice_A.get_adjacentes()
        self.assertDictContainsSubset(expected,adj, '')                

    def testVerticeAdjPeso(self):
        adj = self.vertice_A.get_adjacentes()
        self.assert_(1 == adj[self.vertice_B], '')
        pass
    def tearDown(self):        
        pass
    

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    vertice_test_suite = unittest.TestSuite()
    vertice_test_suite.addTest(Test('testVerticeAdj'))
    vertice_test_suite.addTest(Test('testVerticeAdjPeso'))
    runner = unittest.TextTestRunner()
    runner.run(vertice_test_suite)
    
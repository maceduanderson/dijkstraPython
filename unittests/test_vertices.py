'''
Created on 20 de abr de 2016

@author: Anderson Macedo
'''
import unittest
from Grafo import Vertice

class Test_Vertices(unittest.TestCase):


    def setUp(self):
        self.verticeSP = Vertice('SP')
        self.verticeRJ = Vertice('RJ')
        self.verticeES = Vertice('ES')                     
        pass


    def tearDown(self):
        expected = {'RJ' : 10, 'ES' : 20, 'RS' : 30}
        self.assertDictContainsSubset(expected, self.verticeSP.get_adjacentes(), self.verticeSP.get_adjacentes())
        pass


    def testVertices(self):
        self.verticeSP.add_adjacentes('RJ', 10)
        self.verticeSP.add_adjacentes('ES', 20)
        self.verticeSP.add_adjacentes('RS', 30)       
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
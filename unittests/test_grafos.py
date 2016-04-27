'''
Created on 27 de abr de 2016

@author: Anderson Macedo
'''
import unittest

from Grafos.GrafosUtil import Grafo



class Test(unittest.TestCase):


    def setUp(self):
        self.grafo = Grafo()
        self.grafo.add_vertice('SP')
        self.grafo.add_vertice('RJ')
        self.grafo.add_vertice('ES')
        self.grafo.add_vertice('MG')
        self.grafo.add_vertice('SC')
        
        self.grafo.add_aresta('SP', 'RJ', 100)
        self.grafo.add_aresta('SP', 'ES', 200)
        self.grafo.add_aresta('ES', 'MG', 50)
        self.grafo.add_aresta('MG', 'SC', 156)
        self.grafo.add_aresta('RJ', 'SC', 10)
        self.grafo.add_aresta('SP', 'SC', 1000)          
        pass


    def tearDown(self):
        pass


    def testUpdateList(self):
        v1 = self.grafo.list_vertices['SP']
        dv1 = v1.get_adjacentes()
        for adj in dv1.keys():
            adj.set_distancia(10)
        v2 = self.grafo.list_vertices['RJ']
        dv2 = v2.get_adjacentes()
        for adj2 in dv2.keys():
            print (str(adj2.get_distancia()))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
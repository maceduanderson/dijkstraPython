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

    
    def testMatrizAdj(self):
        
        matriz = self.grafo.get_matriz_distancia()
        print(matriz)
    
    def testAddVertice(self):    
        expected = ['SP', 'RJ', 'ES', 'MG', 'SC']
        actual = self.grafo.list_vertices.keys()
        self.assertItemsEqual(expected, actual, str(expected) + ' '+ str(actual))
        pass
    
    def testAdj(self):
        expected = ['RJ', 'ES', 'SC']
        adj = self.grafo.list_vertices['SP'].get_adjacentes()
        actual = [v.get_nome() for v in adj.keys()]
        self.assertItemsEqual(expected, actual, str(expected) + ' '+ str(actual))        
        pass
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
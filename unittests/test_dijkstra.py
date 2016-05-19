'''
Created on 20 de abr de 2016

@author: Anderson Macedo
'''
import unittest

from Grafos.Dijkstra import djikstraAlg, menorCaminho
from Grafos.GrafosUtil import Grafo


class Test_Dijkstra(unittest.TestCase):
    
    
    def setUp(self):

        print("iniciando Teste Test_Dijkstra")
                              
        pass


    def tearDown(self):
        
        print('Finalizando Teste Test_Dijkstra')
        pass


    def testDijkstra(self):
        grafo = Grafo()
        grafo.add_vertice('SP')
        grafo.add_vertice('RJ')
        grafo.add_vertice('ES')
        grafo.add_vertice('MG')
        grafo.add_vertice('SC')        
        grafo.add_aresta('SP', 'RJ', 100)
        grafo.add_aresta('SP', 'ES', 200)
        grafo.add_aresta('ES', 'MG', 50)
        grafo.add_aresta('MG', 'SC', 156)
        grafo.add_aresta('RJ', 'SC', 10)
        grafo.add_aresta('SP', 'SC', 1000)           
                          
        djikstraAlg(grafo, 'SP')
        scVertice = grafo.get_vertice('SC')
        self.assertTrue(scVertice.get_distancia() == 110, 'distance to SC is '+ str(scVertice.get_distancia()))      
                        
        pass
    
    def testMinimoCaminho(self):
        grafo = Grafo()
        grafo.add_vertice('SP')
        grafo.add_vertice('RJ')
        grafo.add_vertice('ES')
        grafo.add_vertice('MG')
        grafo.add_vertice('SC')        
        grafo.add_aresta('SP', 'RJ', 100)
        grafo.add_aresta('SP', 'ES', 200)
        grafo.add_aresta('ES', 'MG', 50)
        grafo.add_aresta('MG', 'SC', 156)
        grafo.add_aresta('RJ', 'SC', 10)
        grafo.add_aresta('SP', 'SC', 1000)
          
        djikstraAlg(grafo, 'SP')
        expected =  list([grafo.get_vertice('SP'), grafo.get_vertice('RJ'), grafo.get_vertice('SC')])
        actual = menorCaminho(grafo.get_vertice('SC'))
        actual.sort(cmp=None, key=None, reverse=False)
        self.assertListEqual(expected, actual,  str(expected) + ' '+ str(actual))
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
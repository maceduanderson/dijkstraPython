'''
Created on 19 de mai de 2016

@author: Anderson Macedo
'''
from ctypes.test.test_array_in_pointer import Test
import unittest

from Grafos.Dijkstra import djikstraAlg, menorCaminho
from Grafos.GrafosUtil import Grafo
from unittests.test_dijkstra import Test_Dijkstra
from unittests.test_grafos import Test_Grafos
from unittests.test_queue import Test_Queue


if __name__ == '__main__':
    
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test_Dijkstra))
    test_suite.addTest(unittest.makeSuite(Test_Grafos))
    test_suite.addTest(unittest.makeSuite(Test_Queue))
    test_suite.addTest(unittest.makeSuite(Test))
    
    
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
    
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
    menorCaminho(grafo.get_vertice('SC'))
    pass
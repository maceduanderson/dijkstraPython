'''
Created on 19 de abr de 2016

@author: Anderson Macedo
'''
import sys





class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = {}
                            
    def add_adjacentes(self, new_vertice , peso):
        self.adjacentes[new_vertice] = peso
        
    def get_adjacentes(self):
        return self.adjacentes         
        
class Grafo:
    def __init__(self, grafoOrientado):
        self.grafoOrientado = grafoOrientado
        self.vertices = {}
    
    def add_vertice(self, nome):
        novo = Vertice(nome)
        self.vertices[nome] = novo
    
    def add_aresta(self, de, para, peso):
        if not de in self.vertices:
            self.add_vertice(de)
        if not para in self.vertices:
            self.add_vertice(para)
        self.vertices[de].add_adjacentes(para)
        if not self.grafoOrientado:
            self.vertices[para].add_adjacentes(de)
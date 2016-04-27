'''
Created on 19 de abr de 2016

@author: Anderson Macedo
'''
import sys, random






class Vertice:
    def __init__(self, nome, id):
        self.id =  id       
        self.nome = nome        
        self.ligacoes = ()
        self.visitado = False
        self.distancia = sys.maxint        
        self.adjacentes = {}
    
    def __cmp__(self, other):
        return cmp(self.distancia, other.distancia)
    def __hash__(self):
        return  self.id
                                     
    def add_adjacentes(self, new_vertice, peso):
        self.adjacentes[new_vertice] = peso
        
    def get_adjacentes(self):
        return self.adjacentes         
    
    def get_peso(self, adj):
        return self.adjacentes[adj]
    
    def set_distancia(self, distancia):
        self.distancia = distancia
        
    def get_distancia(self):
        return self.distancia
        
    def set_ligacao(self, ant, prox):        
        self.ligacoes = (ant,prox)
    
    def get_ligacao(self):
        return self.ligacoes
    
    def get_nome(self):
        return self.nome
    def get_id(self):
        return self.id
    
    def __str__(self):
        return 'id :' + str(self.id) +' ' + self.nome + ' disntacia: '+ str(self.distancia) +  ' adjs : ' + str([x.nome for x in self.adjacentes])   
   
class Grafo:
    def __init__(self):
        self.nVertice = 0
        self.list_vertices = {}
        self.list_arestas = {}
                
    def __iter__(self):
        return iter(self.list_vertices.values())
    
    def add_vertice(self, nome):
        self.nVertice = self.nVertice + 1
        vertice = Vertice(nome, self.nVertice)
        self.list_vertices[nome] = vertice
        
    def add_aresta(self, de, para, peso):        
        if not de in self.list_vertices:
            self.list_vertices.add_vertice(de)
        if not para in self.list_vertices:
            self.list_vertices.add_vertice(para)
        self.list_vertices[de].add_adjacentes(self.list_vertices[para], peso)
        

        
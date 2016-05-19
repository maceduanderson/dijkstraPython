'''
Created on 19 de abr de 2016

@author: Anderson Macedo
'''
import sys


class Vertice:
    def __init__(self, nome, _id):
        self.id =  _id       
        self.nome = nome        
        self.anterior = None        
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
        
    def set_anterior(self, anterior):        
        self.anterior = anterior
    
    def get_anterior(self):
        return self.anterior
    
    def get_nome(self):
        return self.nome
    
    def get_id(self):
        return self.id
    
    def __str__(self):
        #return 'id :' + str(self.id) +' ' + self.nome + ' disntacia: '+ str(self.distancia) +  ' adjs : ' + str([x.nome for x in self.adjacentes])   
        return 'id:{0} nome:{1} distancia:{2} adj:{3}'.format(self.id, self.nome,self.distancia, [ (x.nome, p)  for x,p in self.adjacentes.iteritems()])
class Grafo:
    def __init__(self):
        self.nVertice = 0
        self.list_vertices = {}        
        self.matriz_adjacencia = []
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
    
    def get_vertice(self, nome):
        if nome in self.list_vertices:
            return self.list_vertices[nome]
    
    def get_list_vertices(self):
        return self.list_vertices
    
    def get_matriz_distancia(self):        
        if self.list_vertices:
            for nome, verticeI in self.list_vertices.items():
                linha = []
                for nomeJ, verticeJ in self.list_vertices.items():
                    adjs = verticeI.get_adjacentes()
                    inAdj = 0                                        
                    for verticeAdj, peso in adjs.items():
                        if nomeJ == verticeAdj.get_nome():
                            inAdj = peso
                         
                    linha = linha +[inAdj]
                self.matriz_adjacencia = self.matriz_adjacencia + [linha]
            return self.matriz_adjacencia            
                                                            
    
    def __str__(self):
        return '{0}'.format([x.__str__() for x in self.list_vertices.values()])
        
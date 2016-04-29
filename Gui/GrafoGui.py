'''
Created on 28 de abr de 2016

@author: Anderson Macedo
'''
import math
import random

import pygame

from Grafos.GrafosUtil import Vertice, Grafo




class VerticeGui(Vertice):
    
    def __init__(self, nome, _id, x, y, size): 
        self.x = x
        self.y = y
        self.size = size       
        self.color = list([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        self.font = pygame.font.SysFont("monospace", 15)

        Vertice.__init__(self, nome, _id)    
    def drawVertice(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
        label = self.font.render(self.nome, 1, [0,0,0])
        screen.blit(label,[self.x, self.y+6])
    
    def drawArestas(self, screen):
        for adjs in self.adjacentes.keys():
            pygame.draw.line(screen, [0, 0, 0], [self.x, self.y], [adjs.x, adjs.y])
            label = self.font.render(self.nome, 1, [0,0,0])
            screen.blit(label,[self.x, self.y])
class GrafoGui(Grafo):
    
     
    def add_vertice(self, nome, x, y, size):
        self.nVertice = self.nVertice + 1
        vertice = VerticeGui(nome, self.nVertice, x, y, size)
        self.list_vertices[nome] = vertice
    
        
    
    
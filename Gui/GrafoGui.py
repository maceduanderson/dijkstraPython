'''
Created on 28 de abr de 2016

@author: Anderson Macedo
'''
import random

import pygame


class VerticeGui():
    
    def __init__(self, coordX , coordY):
        self.x = coordX
        self.y = coordY
        self.size = 10
        
        self.color = list([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
class GrafoGui():
    
    def __init__(self, grafo):
        self.grafo = grafo
    
    
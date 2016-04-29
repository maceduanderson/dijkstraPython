'''
Created on 28 de abr de 2016

@author: Anderson Macedo
'''
import pygame
from Gui.GrafoGui import VerticeGui, GrafoGui
from pygame.constants import MOUSEBUTTONDOWN

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)

def mainLoop():
    # Define some colors

     
    pygame.init()
     
    

    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Algoritmo de Dijkstra")
     
    done = False
     
    clock = pygame.time.Clock()
     
    sizeMatriz = 4
    posX = size[0]/sizeMatriz
    posY = size[1]/sizeMatriz
    
    x = 10
    y = size[1]/2
    grafo = GrafoGui()
    grafo.add_vertice('SP', x, y, 10)
    y = y + posY
    x = x + posX
    grafo.add_vertice('ES', x, y, 10)
    y = y - posY
    x = x + posX
    grafo.add_vertice('RJ', x, y, 10)
    y = y + posY
    x = x + posX
    grafo.add_vertice('MG', x, y, 10)
    y = y - posY
    x = x + posX
    grafo.add_aresta('SP', 'RJ', 440)
    grafo.add_aresta('SP', 'ES', 1063)
    grafo.add_aresta('SP', 'MG', 768)
    grafo.add_aresta('RJ', 'MG', 639)
    grafo.add_aresta('RJ', 'ES', 698)
    grafo.add_aresta('MG', 'ES', 740)
    

    screen.fill(WHITE)
    # -------- Main Program Loop -----------
    while not done:    
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == MOUSEBUTTONDOWN:
                for n,v in grafo.get_list_vertices().items():
                    v.drawVertice(screen)
                for n,v in grafo.get_list_vertices().items():
                    v.drawArestas(screen)  
            
        
        #screen.fill(WHITE)
                
        # --- Drawing code should go here
          
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()

if __name__ == '__main__':
    mainLoop()
    pass
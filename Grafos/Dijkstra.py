'''
Created on 26 de abr de 2016

@author: Anderson Macedo
'''

from DataStruct.PriorityQueue import PriorityQueue


def djikstraAlg( grafo, inicial ):
    
    # Os valores d[v], pi[v] sao instanciados com os valores corretos
    
    grafo.list_vertices[inicial].set_distancia(0) # Distancia do no inicial
    
    to_list = [v for v in grafo.list_vertices.itervalues()]
    queue = PriorityQueue(to_list)

        
    
    while not queue.empty():
        q = queue.pop()
        vertice = None
        
        for v in grafo.list_vertices.itervalues(): #gambi
            if q.get_id() == v.get_id():
                vertice = v
                
        for vertice_adj in vertice.get_adjacentes():
            if not vertice_adj in queue.get_queue():
                continue
            min_dist = vertice.get_distancia() + vertice.get_peso(vertice_adj)
            if vertice.get_distancia() <  min_dist:
                vertice_adj.set_distancia(min_dist)
                vertice_adj.set_anterior(vertice) # seta pi[v]
                queue.update(vertice_adj)# gambi
            
                            
        print(vertice)

#calcula o menor caminho navegando por #pi[v]             
def menorCaminho(final):
    lista_menor_caminho =[]
    vertice = final
    while vertice:
        lista_menor_caminho.append(vertice)
        vertice = vertice.get_anterior()
    
    return lista_menor_caminho                        
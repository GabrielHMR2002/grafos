from grafo import Grafo


def criar_grafo_exemplo():
    grafo = Grafo()
    
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertice in vertices:
        grafo.adicionar_vertice(vertice)
    
    grafo.adicionar_aresta('a', 'b')  # e1
    grafo.adicionar_aresta('a', 'c')  # e2
    grafo.adicionar_aresta('b', 'd')  # e3
    grafo.adicionar_aresta('b', 'e')  # e4
    grafo.adicionar_aresta('b', 'c')  # e5
    grafo.adicionar_aresta('c', 'd')  # e6
    grafo.adicionar_aresta('d', 'e')  # e7
    
    return grafo

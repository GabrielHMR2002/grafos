class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            for adjacente in self.vertices[vertice]:
                self.vertices[adjacente].remove(vertice)
            del self.vertices[vertice]

    def remover_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            if vertice2 in self.vertices[vertice1]:
                self.vertices[vertice1].remove(vertice2)
            if vertice1 in self.vertices[vertice2]:
                self.vertices[vertice2].remove(vertice1)

    def mostrar_vertices(self):
        return list(self.vertices.keys())

    def mostrar_arestas(self):
        arestas = []
        for vertice in self.vertices:
            for adjacente in self.vertices[vertice]:
                if {vertice, adjacente} not in arestas:
                    arestas.append({vertice, adjacente})
        return arestas

class Graph:
    def __init__(self, qtd_vertices, direcionado=False):
        self.vertices = {}
        self.direcionado = direcionado
        self.matriz_adjacencia = None
        self.matriz_incidencia = None

        for i in range(qtd_vertices):
            # Gera vértices com nomes 'a', 'b', 'c', etc.
            vertice = chr(97 + i)
            self.adicionar_vertice(vertice)

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append(vertice2)
            if not self.direcionado:
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
            if not self.direcionado and vertice1 in self.vertices[vertice2]:
                self.vertices[vertice2].remove(vertice1)

    def mostrar_vertices(self):
        return list(self.vertices.keys())

    def mostrar_arestas(self):
        arestas = []
        for vertice in self.vertices:
            for adjacente in self.vertices[vertice]:
                if self.direcionado or {vertice, adjacente} not in arestas:
                    arestas.append({vertice, adjacente})
        return arestas


# GRAFOS NAO DIRECIONAIS


    def criar_matriz_adjacencia_grafo_nao_direcional(self):
        num_vertices = len(self.vertices)
        self.matriz_adjacencia = [
            [0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        vertices_list = list(self.vertices.keys())

        for i, vertice1 in enumerate(vertices_list):
            for adjacente in self.vertices[vertice1]:
                j = vertices_list.index(adjacente)
                self.matriz_adjacencia[i][j] = 1
                if not self.direcionado:
                    self.matriz_adjacencia[j][i] = 1

    def mostrar_matriz_adjacencia_grafo_nao_direcional(self):
        if self.matriz_adjacencia:
            for linha in self.matriz_adjacencia:
                print(linha)

    def criar_matriz_incidencia_grafo_nao_direcional(self):
        arestas = self.mostrar_arestas()
        num_vertices = len(self.vertices)
        num_arestas = len(arestas)
        self.matriz_incidencia = [
            [0 for _ in range(num_arestas)] for _ in range(num_vertices)]
        vertices_list = list(self.vertices.keys())

        for e, aresta in enumerate(arestas):
            v1, v2 = tuple(aresta)
            i = vertices_list.index(v1)
            j = vertices_list.index(v2)
            self.matriz_incidencia[i][e] = 1
            if not self.direcionado:
                self.matriz_incidencia[j][e] = 1

    def mostrar_matriz_incidencia_grafo_nao_direcional(self):
        if self.matriz_incidencia:
            for linha in self.matriz_incidencia:
                print(linha)

    def mostrar_lista_adjacencia_grafo_nao_direcional(self):
        for vertice in self.vertices:
            print(f'{vertice}: {self.vertices[vertice]}')

# GRAFOS  DIRECIONAIS

    def criar_matriz_adjacencia_grafo_direcional(self):
        print('Não Implementado')

    def mostrar_matriz_adjacencia_grafo_direcional(self):
        print('Não Implementado')

    def criar_matriz_incidencia_grafo_direcional(self):
        print('Não Implementado')

    def mostrar_matriz_incidencia_grafo_direcional(self):
        print('Não Implementado')

    def mostrar_lista_adjacencia_grafo_direcional(self):
        print('Não Implementado')

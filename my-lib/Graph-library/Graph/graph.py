import os
import subprocess
import networkx as nx  # Certifique-se de que o NetworkX esteja instalado


class GraphNotDirected:
    def __init__(self, qtd_vertices, direcionado=False):
        self.vertices = {}
        self.direcionado = direcionado
        self.matriz_adjacencia = None
        self.matriz_incidencia = None
        self.num_vertices = qtd_vertices  # Adiciona num_vertices para ser usado no exportGraph

        for i in range(qtd_vertices):
            vertice = chr(97 + i)  # Gera vértices com nomes 'a', 'b', 'c', etc.
            self.adicionar_vertice(vertice)

    # GRAFOS NAO DIRECIONAIS

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

    # GRAFOS DIRECIONAIS

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

 # EXPORTAÇÃO
    def exportGraph(self):
        G = nx.Graph()

        # Converte a matriz de adjacência em um grafo NetworkX
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz_adjacencia[i][j] != 0:
                    G.add_edge(i, j, weight=self.matriz_adjacencia[i][j], label=str(self.matriz_adjacencia[i][j]))

        # Exporta o grafo para o formato GEXF
        gexf_file = "grafo.gexf"
        nx.write_gexf(G, gexf_file)

        # Caminho do executável do Gephi
        gephi_path = r"C:\Users\gabri\OneDrive\Área de Trabalho\appgrafos\gephi.lnk" # Altere para o caminho correto do Gephi
        gexf_path = os.path.abspath(gexf_file)  # Caminho absoluto do arquivo GEXF

        # Abre o Gephi com o arquivo GEXF usando o caminho absoluto
        try:
            subprocess.run([gephi_path, gexf_path], check=True)
            print("Gephi aberto com sucesso com o arquivo:", gexf_path)
        except FileNotFoundError:
            print("Erro: Não foi possível encontrar o executável do Gephi.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar abrir o Gephi: {e}")
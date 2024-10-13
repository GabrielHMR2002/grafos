from Interface import interface
from Graph.graph import GraphNotDirected


def criar_grafo_nao_direcional_exemplo():
    qtd_vertices = 5
    direcionado = False
    grafo = GraphNotDirected(qtd_vertices, direcionado)

    grafo.adicionar_aresta('a', 'b')  # e1
    grafo.adicionar_aresta('a', 'c')  # e2
    grafo.adicionar_aresta('b', 'd')  # e3
    grafo.adicionar_aresta('b', 'e')  # e4
    grafo.adicionar_aresta('b', 'c')  # e5
    grafo.adicionar_aresta('c', 'd')  # e6
    grafo.adicionar_aresta('d', 'e')  # e7

    # Exportar o grafo para Gephi
    grafo.criar_matriz_adjacencia_grafo_nao_direcional()
    grafo.exportGraph()

    return grafo


def criar_grafo_nao_direcional_exemplo():
    qtd_vertices = 5
    direcionado = False
    grafo = GraphNotDirected(qtd_vertices, direcionado)

    grafo.adicionar_aresta('a', 'b')  # e1
    grafo.adicionar_aresta('a', 'c')  # e2
    grafo.adicionar_aresta('b', 'd')  # e3
    grafo.adicionar_aresta('b', 'e')  # e4
    grafo.adicionar_aresta('b', 'c')  # e5
    grafo.adicionar_aresta('c', 'd')  # e6
    grafo.adicionar_aresta('d', 'e')  # e7

    # Exportar o grafo para Gephi
    grafo.criar_matriz_adjacencia_grafo_nao_direcional()
    grafo.exportGraph()

    return grafo


def mostrar_menu_principal():
    grafo = criar_grafo_nao_direcional_exemplo()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Visualizar grafo na interface gráfica")
        print("2. Ver representações do grafo")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            interface.iniciar_interface_grafica(grafo)
        elif escolha == '2':
            mostrar_representacao_opcoes(grafo)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


def mostrar_representacao_opcoes(grafo):
    while True:
        print("\n--- Representações de Grafos ---")
        print("1. Matriz de Adjacência")
        print("2. Matriz de Incidência")
        print("3. Lista de Adjacência")
        print("4. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\n--- Matriz de Adjacência ---")
            grafo.criar_matriz_adjacencia_grafo_nao_direcional()
            grafo.mostrar_matriz_adjacencia_grafo_nao_direcional()
        elif escolha == '2':
            print("\n--- Matriz de Incidência ---")
            grafo.criar_matriz_incidencia_grafo_nao_direcional()
            grafo.mostrar_matriz_incidencia_grafo_nao_direcional()
        elif escolha == '3':
            print("\n--- Lista de Adjacência ---")
            grafo.mostrar_lista_adjacencia_grafo_nao_direcional()
        elif escolha == '4':
            break
        else:
            print("Opção inválida, tente novamente.")

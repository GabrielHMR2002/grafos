import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.manipulacao import criar_grafo_exemplo
import tkinter as tk

def desenhar_grafo(canvas, grafo):
    vertices = grafo.mostrar_vertices()
    posicoes = {
        'a': (100, 100),
        'b': (200, 100),
        'c': (100, 200),
        'd': (200, 200),
        'e': (300, 100)
    }
    
    arestas = grafo.mostrar_arestas()

    for aresta in arestas:
        v1, v2 = tuple(aresta)
        x1, y1 = posicoes[v1]
        x2, y2 = posicoes[v2]
        canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)

    for vertice, (x, y) in posicoes.items():
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="skyblue")
        canvas.create_text(x, y, text=str(vertice), font=("Arial", 16))

def iniciar_interface_grafica():
    grafo = criar_grafo_exemplo()

    root = tk.Tk()
    root.title("Visualização do Grafo")

    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack()

    desenhar_grafo(canvas, grafo)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interface_grafica()

import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:
    def __init__(self, graph, positions, initial, goal):
        self.graph = graph  # Grafo representado como un diccionario
        self.positions = positions  # Diccionario con posiciones de los nodos
        self.initial = initial  # Nodo inicial
        self.goal = goal  # Nodo objetivo
        self.nx_graph = nx.Graph()  # Grafo de NetworkX

        # Añadimos las aristas al grafo de NetworkX
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                self.nx_graph.add_edge(node, neighbor)

    def draw_graph(self, path=None):
        plt.figure(figsize=(10, 10))

        # Usamos las posiciones de los nodos proporcionadas
        pos = self.positions

        # Definir colores: verde para initial, rojo para final, azul para el resto
        color_map = []
        for node in self.nx_graph:
            if node == self.initial:
                color_map.append('green')  # Nodo inicial
            elif node == self.goal:
                color_map.append('red')  # Nodo final
            else:
                color_map.append('blue')  # Otros nodos

        # Dibujar el grafo con colores personalizados para los nodos y las posiciones
        nx.draw(self.nx_graph, pos, with_labels=True, node_size=50, font_size=8,
                node_color=color_map, font_weight='light', edge_color='gray')

        if path:
            # Destacar el camino encontrado en rojo
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(self.nx_graph, pos, edgelist=path_edges, edge_color='r', width=2)

        plt.title("Grafo con Camino Resaltado")
        plt.show()

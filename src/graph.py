import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, intersections, segments, solution_path):
        self.intersections = intersections
        self.segments = segments
        self.solution_path = solution_path
        self.graph = nx.Graph()
        
        self.create_graph()

    def create_graph(self):
        for state_id, state in self.intersections.items():
            self.graph.add_node(state_id, pos=(state.longitude, state.latitude))
        
        for segment in self.segments:
            self.graph.add_edge(segment.origin.identifier, segment.destination.identifier, weight=segment.distance)

    def show_graph(self):
        pos = nx.get_node_attributes(self.graph, 'pos')
        
        plt.figure(figsize=(10, 10))
        nx.draw(self.graph, pos, node_size=5, node_color="skyblue", font_size=10, with_labels=False, font_weight="normal", edge_color="gray")

        if self.solution_path:
            solution_edges = [(self.solution_path[i], self.solution_path[i+1]) for i in range(len(self.solution_path) - 1)]
            nx.draw_networkx_edges(self.graph, pos, edgelist=solution_edges, edge_color="red", width=2.5)
        
        plt.title("Grafo de Intersecciones y Camino de Solución")
        plt.show()

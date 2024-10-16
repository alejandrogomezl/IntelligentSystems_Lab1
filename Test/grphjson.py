import json
import networkx as nx
import matplotlib.pyplot as plt

# Clase para leer el archivo JSON y crear el grafo
class GraphBuilder:
    def __init__(self, json_file):
        self.graph = nx.Graph()  # Grafo de NetworkX
        self.data = self.load_json(json_file)
        self.intersections = self.data['intersections']
        self.segments = self.data['segments']
        self.initial = str(self.data['initial'])  # Identificador inicial
        self.final = str(self.data['final'])  # Identificador final
        
        self.graph_dict = {}  # Diccionario para representar el grafo
        self.create_graph()

    def load_json(self, json_file):
        # Carga el archivo JSON desde la ruta proporcionada
        with open(json_file, 'r') as file:
            return json.load(file)

    def create_graph(self):
        # Añadimos nodos (intersecciones)
        for intersection in self.intersections:
            identifier = str(intersection['identifier'])  # Convertimos a string para que el diccionario coincida
            longitude = intersection['longitude']
            latitude = intersection['latitude']
            self.graph.add_node(identifier, pos=(longitude, latitude))
            self.graph_dict[identifier] = []  # Inicializamos el diccionario de vecinos

        # Añadimos aristas (segmentos)
        for segment in self.segments:
            origin = str(segment['origin'])
            destination = str(segment['destination'])
            distance = segment['distance']
            self.graph.add_edge(origin, destination, weight=distance)

            # Actualizamos el diccionario de representación del grafo
            self.graph_dict[origin].append(destination)
            self.graph_dict[destination].append(origin)

    def draw_graph(self):
        # Dibuja el grafo usando las posiciones de los nodos
        pos = nx.get_node_attributes(self.graph, 'pos')
        plt.figure(figsize=(10, 10))

        # Definir colores: verde para initial, rojo para final, azul para el resto
        color_map = []
        for node in self.graph:
            if node == self.initial:
                color_map.append('green')  # Verde para el inicial
            elif node == self.final:
                color_map.append('red')  # Rojo para el final
            else:
                color_map.append('blue')  # Azul para el resto de los nodos

        # Dibujar el grafo con colores personalizados
        nx.draw(self.graph, pos, with_labels=True, node_size=50, font_size=8, node_color=color_map, font_weight='light', edge_color='gray')

        plt.title("Grafo con Initial (verde) y Final (rojo)")
        plt.show()

    def print_graph_dict(self):
        # Imprimir el diccionario que representa el grafo
        print("Diccionario que representa el grafo:")
        for node, neighbors in self.graph_dict.items():
            print(f"'{node}': {neighbors},")

# Ruta completa del archivo JSON en tu sistema local
json_file = r'C:\Users\aleja\OneDrive\Universidad\Inteligent Systems\Lab\Lab 1\pr1_SSII_English\problems\small\calle_agustina_aroca_albacete_250_0.json'

# Crear el grafo y dibujarlo
builder = GraphBuilder(json_file)

# Imprimir el diccionario que representa el grafo
builder.print_graph_dict()

# Dibujar el grafo con nodos inicial y final coloreados
builder.draw_graph()

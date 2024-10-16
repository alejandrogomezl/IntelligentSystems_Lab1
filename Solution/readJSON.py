import json

class JsonReader:
    def __init__(self, json_file):
        self.data = self.load_json(json_file)
        self.intersections = self.data['intersections']
        self.segments = self.data['segments']
        self.initial = str(self.data['initial'])
        self.final = str(self.data['final'])
        
        self.graph_dict = {}  # Diccionario que representará el grafo
        self.positions = {}   # Diccionario para las posiciones de los nodos
        self.create_graph()

    def load_json(self, json_file):
        with open(json_file, 'r') as file:
            return json.load(file)

    def create_graph(self):
        # Añadimos nodos (intersecciones) y guardamos sus posiciones
        for intersection in self.intersections:
            identifier = str(intersection['identifier'])  # Convertimos el identificador a string
            longitude = intersection['longitude']
            latitude = intersection['latitude']
            self.graph_dict[identifier] = []  # Inicializamos con una lista vacía de vecinos
            self.positions[identifier] = (longitude, latitude)  # Guardamos la posición

        # Añadimos las conexiones (segmentos) entre las intersecciones
        for segment in self.segments:
            origin = str(segment['origin'])
            destination = str(segment['destination'])
            # Añadimos el destino a la lista de vecinos del origen y viceversa
            self.graph_dict[origin].append(destination)
            self.graph_dict[destination].append(origin)

    def get_graph(self):
        return self.graph_dict

    def get_positions(self):
        return self.positions

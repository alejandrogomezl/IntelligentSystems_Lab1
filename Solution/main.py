from readJSON import JsonReader
from search import Search
from problem import Problem
from graph import GraphVisualizer

# Cargar el archivo JSON
file = "./problems/small/calle_agustina_aroca_albacete_250_0.json"

# Leer el archivo JSON y obtener el grafo y las posiciones
json_reader = JsonReader(file)
graph = json_reader.get_graph()
positions = json_reader.get_positions()
initial_state = json_reader.initial
goal_state = json_reader.final

# Definir el problema con estado inicial y objetivo
problem = Problem(initial=initial_state, goal=goal_state, graph=graph)

# Ejecutar el algoritmo de búsqueda
search_instance = Search(problem)
path = search_instance.bfs()

# Mostrar el resultado
if path:
    print(f"Camino encontrado: {path}")
    visualizer = GraphVisualizer(graph, positions, initial_state, goal_state)
    visualizer.draw_graph(path)
else:
    print("No se encontró solución.")

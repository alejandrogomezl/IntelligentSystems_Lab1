import networkx as nx
import matplotlib.pyplot as plt

# Clase State: Representa un estado del problema (en este caso, una ciudad)
class State:
    def __init__(self, name):
        self.name = name  # Nombre del estado (ciudad)

    # Método __eq__ para comparar dos objetos de tipo State
    def __eq__(self, other):
        return isinstance(other, State) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


# Clase Action: Representa una acción entre dos estados (ir de una ciudad a otra)
class Action:
    def __init__(self, origin, destination):
        self.origin = origin  # Ciudad de origen
        self.destination = destination  # Ciudad de destino

    def __repr__(self):
        return f"Action({self.origin} -> {self.destination})"


# Clase Node: Representa un nodo en el espacio de búsqueda
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # Estado del nodo (ciudad actual)
        self.parent = parent  # Nodo padre (desde donde venimos)
        self.action = action  # Acción que nos llevó a este nodo (ir de una ciudad a otra)
        self.path_cost = path_cost  # Costo acumulado hasta este nodo
        self.depth = 0 if parent is None else parent.depth + 1  # Profundidad del nodo

    def __repr__(self):
        return f"Node({self.state})"

    def path(self):
        # Devuelve el camino desde el nodo inicial hasta el actual
        node, path_back = self, []
        while node:
            path_back.append(node.state.name)
            node = node.parent
        return path_back[::-1]  # Se invierte para obtener el camino correcto


# Clase Problem: Define el problema de búsqueda
class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = State(initial)  # Estado inicial
        self.goal = State(goal)  # Estado objetivo
        self.graph = graph  # El grafo que contiene las conexiones entre las ciudades

    def actions(self, state):
        # Devuelve todas las acciones posibles desde un estado (ciudad actual)
        neighbors = self.graph[state.name]  # Vecinos de la ciudad actual
        print(f"Acciones posibles desde {state.name}: {neighbors}")
        return [Action(state.name, neighbor) for neighbor in neighbors]

    def result(self, state, action):
        # Retorna el estado resultante después de aplicar una acción
        print(f"Aplicando acción: {action}")
        return State(action.destination)

    def goal_test(self, state):
        # Usamos __eq__ para comparar el estado actual con el objetivo
        is_goal = state == self.goal
        print(f"¿Estado actual ({state.name}) es el objetivo ({self.goal.name})? {'Sí' if is_goal else 'No'}")
        return is_goal

    def step_cost(self, state, action):
        # Define el costo de moverse de un estado a otro (puede ser una distancia)
        print(f"Costo de moverse de {action.origin} a {action.destination}: 1")
        return 1  # Para simplificar, cada movimiento cuesta 1


# Función que implementa el algoritmo de búsqueda básica en grafos (versión simple)
def graph_search(problem):
    # Inicializamos la lista de nodos abiertos (open list) con el nodo inicial
    node = Node(problem.initial)
    print(f"Comenzando búsqueda desde: {node.state.name}")
    
    if problem.goal_test(node.state):  # Si el estado inicial es el objetivo
        return node.path()  # Retornamos el camino

    open_list = [node]  # Lista de nodos por explorar
    explored = set()  # Conjunto de estados explorados

    while open_list:  # Mientras haya nodos por explorar
        node = open_list.pop(0)  # Extraemos el nodo más antiguo (BFS)
        print(f"Explorando nodo: {node.state.name}, con costo acumulado: {node.path_cost}")
        
        if node.state not in explored:  # Solo procesamos nodos no explorados
            explored.add(node.state)  # Marcamos el estado como explorado
            print(f"Estados explorados: {[s.name for s in explored]}")

            # Expandimos el nodo actual, generando sus sucesores
            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)
                child_node = Node(child_state, node, action, node.path_cost + problem.step_cost(node.state, action))

                if problem.goal_test(child_state):  # Si encontramos el objetivo
                    return child_node.path()  # Retornamos el camino encontrado

                open_list.append(child_node)  # Añadimos el sucesor a la lista de nodos abiertos
                print(f"Nodos abiertos: {[n.state.name for n in open_list]}")

    return None  # Si no se encuentra solución, retornamos None

# Clase para visualizar el grafo y resaltar el camino más corto
class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph  # Grafo representado como un diccionario
        self.nx_graph = nx.Graph()  # Grafo de NetworkX

        # Convertir el diccionario de grafo a NetworkX
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                self.nx_graph.add_edge(node, neighbor)

    def draw_graph(self, path=None):
        plt.figure(figsize=(12, 8))

        # Definir la disposición del grafo (layout) para los nodos
        pos = nx.spring_layout(self.nx_graph, seed=42)

        # Dibujar el grafo con nodos y aristas
        nx.draw(self.nx_graph, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")

        if path:
            # Destacar el camino más corto
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(self.nx_graph, pos, edgelist=path_edges, edge_color='r', width=3)

        plt.title("Grafo de Ciudades y Camino Más Corto (en rojo)")
        plt.show()


# Definir un grafo más sencillo para pruebas
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Definir el problema con estado inicial y objetivo
problem = Problem(initial="A", goal="F", graph=graph)

# Ejecutar el algoritmo de búsqueda
path = graph_search(problem)

# Mostrar el resultado
if path:
    print(f"Camino encontrado: {path}")
    visualizer = GraphVisualizer(graph)
    visualizer.draw_graph(path)
else:
    print("No se encontró solución.")

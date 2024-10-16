class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0 if parent is None else parent.depth + 1

    def __repr__(self):
        return f"Node({self.state})"

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return path_back[::-1]


class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def goal_test(self, state):
        return state == self.goal

    def expand(self, node):
        return [Node(state=child, parent=node) for child in self.graph[node.state]]


def graph_search(problem):
    open_list = [Node(problem.initial)]
    explored = set()

    while open_list:
        node = open_list.pop(0)

        if node.state not in explored:
            if problem.goal_test(node.state):
                return node.path()
            
            explored.add(node.state)

            for successor in problem.expand(node):
                open_list.append(successor)

    return None


nodes = [
    ["arad", ["zerind", "sibiu", "timisoara"]],
    ["zerind", ["arad", "oradea"]],
    ["oradea", ["fagaras"]],
    ["timisoara", ["arad", "lugoj"]],
    ["sibiu", ["arad", "fagaras"]]
]

# Convertir la lista de nodos a un diccionario para facilitar el acceso
graph = {city: neighbors for city, neighbors in nodes}

# Definir el problema con un estado inicial (ciudad de inicio) y un estado objetivo (ciudad de destino)
problem = Problem(initial="arad", goal="fagaras", graph=graph)

# Ejecutar la búsqueda
path = graph_search(problem)

# Mostrar el resultado
if path:
    print(f"Camino encontrado: {path}")
else:
    print("No se encontró solución.")

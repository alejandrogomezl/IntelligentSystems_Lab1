from collections import deque
from node import Node

class Search:
    def __init__(self, problem):
        self.problem = problem

    def bfs(self):  
        frontier = deque([Node(self.problem.get_initial_state())])
        explored = set()

        while frontier:
            # Extraer el nodo de la frontera
            node = frontier.popleft()            

            # Verificar si es el objetivo
            if self.problem.is_goal(node.state):
                solution_path = node.path()
                return solution_path

            # Marcar como explorado
            explored.add(node.state)

            # Expandir los nodos hijos
            for child, action in node.state.neighbors:
                if child not in explored and child not in frontier:
                    child = Node(child, node, action, node.path)
                    frontier.append(child)

        return None  # Si no se encuentra una solución

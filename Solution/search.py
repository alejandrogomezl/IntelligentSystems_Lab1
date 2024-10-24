from collections import deque
from node import Node
import time

class Search:
    def __init__(self, problem):
        self.problem = problem

    def bfs(self):  
        start_time = time.perf_counter()
        frontier = deque([Node(self.problem.get_initial_state())])
        explored = set()
        nodes_generated = 1
        nodes_explored = 0
        
        while frontier:
            # Extraer el nodo de la frontera
            node = frontier.popleft()    
            nodes_explored += 1        

            # Verificar si es el objetivo
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                solution_path = node.path()
                print(f'Nodos generados: {nodes_generated}')
                print(f'Nodos expandidos: {nodes_explored}')
                print(f'Profundidad de la solución: {node.depth}')
                print(f'Costo de la solución: {node.cost}')
                print(f'Tiempo de ejecución: {execution_time*1000000000:.6f} nanoSeconds')
                return solution_path

            # Marcar como explorado
            explored.add(node.state)

            # Expandir los nodos hijos
            for child, action in node.state.neighbors:
                if child not in explored and child not in frontier:
                    child = Node(child, node, action, node.cost + action.cost())
                    frontier.append(child)
                    nodes_generated += 1

        return None  # Si no se encuentra una solución

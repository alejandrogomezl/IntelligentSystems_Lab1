from collections import deque
import heapq
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

    def dfs(self):  
        start_time = time.perf_counter()
        frontier = [Node(self.problem.get_initial_state())]
        explored = set()
        nodes_generated = 1
        nodes_explored = 0
        
        while frontier:
            # Extraer el nodo de la frontera
            node = frontier.pop()    
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

    

    def heuristic(self, state, goal):
        x = state.latitude - goal.latitude
        y = state.longitude - goal.longitude
        return (x**2 + y**2)**0.5

    def a_star(self):
        start_time = time.perf_counter()

        frontier = []
        start = Node(self.problem.get_initial_state())
        f = self.heuristic(start.state, self.problem.goal_state)
        heapq.heappush(frontier, (f, start))
        explored = set()
        frontier_state_cost = {self.problem.initial_state: 0}
        nodes_generated = 1
        nodes_explored = 0

        while frontier:
            _, node = heapq.heappop(frontier)
            nodes_explored += 1

            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                solution_path = node.path()
                print(f'Nodos generados: {nodes_generated}')
                print(f'Nodos expandidos: {nodes_explored}')
                print(f'Profundidad de la solución: {node.depth}')
                print(f'Costo de la solución: {node.cost}')
                print(f'Tiempo de ejecución: {execution_time*1000000000:.6f} nanoSegundos')
                return solution_path

            explored.add(node.state)

            for child, action in node.state.neighbors:
                new_cost = node.cost + action.cost()
                if child not in explored and (child not in frontier_state_cost or new_cost < frontier_state_cost[child]):
                    child_node = Node(child, node, action, new_cost)
                    f = new_cost + self.heuristic(child, self.problem.goal_state)
                    heapq.heappush(frontier, (f, child_node))
                    frontier_state_cost[child] = new_cost
                    nodes_generated += 1

        return None
    
    def best_first(self):
        start_time = time.perf_counter()
        frontier = []
        start_node = Node(self.problem.get_initial_state())
        h_cost = self.heuristic(start_node.state, self.problem.goal_state)
        heapq.heappush(frontier, (h_cost, start_node))
        explored = set()
        nodes_generated = 1
        nodes_explored = 0

        while frontier:
            _, node = heapq.heappop(frontier)
            nodes_explored += 1

            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                solution_path = node.path()
                print(f'Nodos generados: {nodes_generated}')
                print(f'Nodos expandidos: {nodes_explored}')
                print(f'Profundidad de la solución: {node.depth}')
                print(f'Costo de la solución: {node.cost}')
                print(f'Tiempo de ejecución: {execution_time*1000000000:.6f} nanoSegundos')
                return solution_path

            explored.add(node.state)

            for child, action in node.state.neighbors:
                if child not in explored:
                    child = Node(child, node, action, node.cost + action.cost())
                    h_cost = self.heuristic(child.state, self.problem.goal_state)
                    heapq.heappush(frontier, (h_cost, child))
                    nodes_generated += 1
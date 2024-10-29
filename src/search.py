from collections import deque
import heapq
from node import Node
import time
import geopy.distance
import itertools

class Search:
    def __init__(self, problem):
        self.problem = problem
        self.counter = itertools.count()

    #Breath First Search
    def bfs(self):
        start_time = time.perf_counter()
        frontier = deque([Node(self.problem.get_initial_state())])  # Queue for nodes in frontier (First In Firs Out)
        explored = set()    # Set of explored states
        nodes_generated = 1
        nodes_explored = 0
        
        while frontier:
            node = frontier.popleft()    # Remove the first node from the queue
            nodes_explored += 1        

            # Check if the current node is the goal
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children of the current node
            for child, action in node.state.neighbors:
                # Add child nodes if they are not explored or in the frontier
                if child not in explored and child not in frontier:
                    child = Node(child, node, action, node.cost + action.cost())
                    frontier.append(child)
                    nodes_generated += 1

        return None

    #Depth First Search
    def dfs(self):  
        start_time = time.perf_counter()
        frontier = [Node(self.problem.get_initial_state())] # Stack for nodes in frontier (Last In First Out)
        explored = set()
        nodes_generated = 1
        nodes_explored = 0
        
        while frontier:
            node = frontier.pop()    # Remove the last node from the stack (Last In First Out)
            nodes_explored += 1        

            # Check if the current node is the goal
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children of the current node
            for child, action in node.state.neighbors:
                if child not in explored and child not in frontier:
                    child = Node(child, node, action, node.cost + action.cost())
                    frontier.append(child)
                    nodes_generated += 1

        return None

    

    def heuristic(self, state, goal):
        # Calculates the Euclidean distance between the current state and the goal state.
        current = (state.latitude, state.longitude)
        dest = (goal.latitude, goal.longitude)
        dist = geopy.distance.distance(current, dest).meters
        speed = 120 / 3.6
        return dist / speed

    # A* Search
    def a_star(self):
        # comparar por heuristica y si empata por nodo mas viejo (Usar el numero de nodo generado)
        start_time = time.perf_counter()

        # Initialize the frontier with the start node and its f(n) = g(n) + h(n)
        frontier = []
        start_node = Node(self.problem.get_initial_state())
        g_cost = 0
        h_cost = self.heuristic(start_node.state, self.problem.goal_state)
        f_cost = g_cost + h_cost
        heapq.heappush(frontier, (f_cost, next(self.counter), start_node))

        explored = set()
        nodes_generated = 1
        nodes_explored = 0

        while frontier:
            _, _, node = heapq.heappop(frontier)   # Remove the node with the lowest f(n)
            nodes_explored += 1

            # Check if the current node is the goal
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children
            for child_state, action in node.state.neighbors:
                # Add to frontier if it's a shorter path to the child
                if child_state not in explored:
                    g = node.cost + action.cost()    # Calculate new g(n) cost
                    h = self.heuristic(child_state, self.problem.goal_state)    # Calculate new h(n) cost
                    f = g + h    # Calculate new f(n) cost

                    child_node = Node(child_state, node, action, g)
                    heapq.heappush(frontier, (f, next(self.counter), child_node))
                    nodes_generated += 1

        return None
    
    # Greedy Best First Search
    def best_first(self):
        start_time = time.perf_counter()
        # Initialize frontier with start node using only h(n)
        frontier = []
        start_node = Node(self.problem.get_initial_state())
        h_cost = self.heuristic(start_node.state, self.problem.goal_state)
        heapq.heappush(frontier, (h_cost, start_node))  
        explored = set()
        nodes_generated = 1
        nodes_explored = 0

        while frontier:
            _, node = heapq.heappop(frontier)   # Remove the node with the lowest h(n)
            nodes_explored += 1

            # Check if the current node is the goal
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children
            for next, action in node.state.neighbors:
                if next not in explored:
                    child = Node(next, node, action, node.cost + action.cost())
                    h_cost = self.heuristic(child.state, self.problem.goal_state)
                    heapq.heappush(frontier, (h_cost, child))
                    nodes_generated += 1
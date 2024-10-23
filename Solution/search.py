from node import Node
import time
from collections import deque

class Search:
    def bfs(problem):
        start_time = time.perf_counter()
        open_list = deque([Node(problem.initial)])
        explored = set()
        nodes_generated = 1
        nodes_explored = 0

        while open_list:
            node = open_list.popleft()
            nodes_explored += 1

            if problem.goal_test(node.state):
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                print("Iniitial state: ", problem.initial.node)
                print("Goal state: ", problem.goal)
                print(f"Execution time: {execution_time:.6f} seconds")
                print(f"Nodes generated: {nodes_generated}")
                print(f"Nodes explored: {nodes_explored}")
                return child_node.path()

            explored.add(node.state)

            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)
                if child_state not in explored and all(front_node.state != child_state for front_node in open_list):
                    child_node = Node(child_state, node, action, node.path_cost + problem.step_cost(node.state, action))
                    open_list.append(child_node)
                    nodes_generated += 1

        return None            
















    # def dfs(self):
    #     start_time = time.perf_counter()
    #     open_list = [Node(self.problem.initial)]
    #     explored = set()
    #     self.nodes_generated = 1
    #     self.nodes_explored = 0

    #     while open_list:
    #         node = open_list.pop()  # LIFO stack
    #         self.nodes_explored += 1

    #         if self.problem.goal_test(node.state):
    #             end_time = time.perf_counter()
    #             execution_time = end_time - start_time
    #             print(f"Execution time: {execution_time:.6f} seconds")
    #             print(f"Nodes generated: {self.nodes_generated}")
    #             print(f"Nodes explored: {self.nodes_explored}")
    #             return node.path()

    #         explored.add(node.state)

    #         # for action in sorted(self.problem.actions(node.state), reverse=True):
    #         for action in self.problem.actions(node.state):
    #             child_state = self.problem.result(node.state, action)
    #             if child_state not in explored and all(front_node.state != child_state for front_node in open_list):
    #                 child_node = Node(child_state, node, action, node.path_cost + self.problem.step_cost(node.state, action))
    #                 open_list.append(child_node)
    #                 self.nodes_generated += 1

    #     end_time = time.perf_counter()
    #     execution_time = end_time - start_time
    #     print(f"Execution time: {execution_time:.6f} seconds")
    #     print(f"Nodes generated: {self.nodes_generated}")
    #     print(f"Nodes explored: {self.nodes_explored}")
    #     return None
    
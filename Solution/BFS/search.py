from node import Node
import time

def Search(problem):
    start = time.perf_counter()
    nodes_generated = 0
    nodes_explored = 0

    node = Node(problem.initial)
    
    if problem.goal_test(node.state):
        return node.path()

    open_list = [node]
    explored = set()

    while open_list:
        node = open_list.pop(0)
        nodes_explored += 1
        
        if node.state not in explored:
            explored.add(node.state)

            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)
                child_node = Node(child_state, node, action, node.path_cost + problem.step_cost(node.state, action))
                open_list.append(child_node)
                
                nodes_generated += 1

                if problem.goal_test(child_state):
                    end = time.perf_counter()
                    execution= end-start
                    print(f"Execution time: {execution:.6f} seconds")
                    print(f"Nodes generated: {nodes_generated}")
                    print(f"Nodes explored: {nodes_explored}")

                    return child_node.path()

                

    return None
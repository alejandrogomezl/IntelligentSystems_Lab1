from node import Node

def Search(problem):
    node = Node(problem.initial)
    
    if problem.goal_test(node.state):
        return node.path()

    open_list = [node]
    explored = set()

    while open_list:
        node = open_list.pop(0)
        
        if node.state not in explored:
            explored.add(node.state)

            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)
                child_node = Node(child_state, node, action, node.path_cost + problem.step_cost(node.state, action))

                if problem.goal_test(child_state):
                    return child_node.path()

                open_list.append(child_node)

    return None
from node import Node

def Search(problem):
    node = Node(problem.initial)
    print(f"Comenzando búsqueda desde: {node.state.name}")
    
    if problem.goal_test(node.state):
        return node.path()

    open_list = [node]
    explored = set()

    while open_list:
        node = open_list.pop(0)
        print(f"Explorando nodo: {node.state.name}, con costo acumulado: {node.path_cost}")
        
        if node.state not in explored:
            explored.add(node.state)
            print(f"Estados explorados: {[s.name for s in explored]}")

            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)
                child_node = Node(child_state, node, action, node.path_cost + problem.step_cost(node.state, action))

                if problem.goal_test(child_state):
                    return child_node.path()

                open_list.append(child_node)
                print(f"Nodos abiertos: {[n.state.name for n in open_list]}")

    return None
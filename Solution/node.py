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
            path_back.append(node.state.name)
            node = node.parent
        return path_back[::-1]